import graphene

import reports.schema


class Query(reports.schema.Query, graphene.ObjectType):
    pass


class Mutation(reports.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
