import graphene
from graphene_django import DjangoObjectType

from .models import Report
from django.db.models import Q


class ReportType(DjangoObjectType):
    class Meta:
        model = Report


class Query(graphene.ObjectType):
    reports = graphene.List(ReportType, publicKey=graphene.String(
    ), first=graphene.Int(), skip=graphene.Int())

    def resolve_reports(self, info, publicKey=None, first=None, skip=None, **kwargs):
        all_reports = Report.objects.all()

        if publicKey:
            filter = (
                Q(publicKey__icontains=publicKey)
            )
            return Report.objects.filter(filter)

        if skip:
            all_reports = all_reports[skip:]

        if first:
            all_reports = all_reports[first:]

        return all_reports


class CreateReport(graphene.Mutation):
    id = graphene.Int()
    message = graphene.String()
    publicKey = graphene.String()

    class Arguments:
        message = graphene.String()
        publicKey = graphene.String()

    def mutate(self, info, message, publicKey):
        report = Report(message=message, publicKey=publicKey)
        if not report:
            raise Exception('Invalid report')
        report.save()

        return CreateReport(
            id=report.id,
            message=report.message,
            publicKey=report.publicKey
        )


class Mutation(graphene.ObjectType):
    create_report = CreateReport.Field()
