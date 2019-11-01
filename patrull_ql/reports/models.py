from django.db import models

# Create your models here.


class Report(models.Model):
    message = models.TextField(blank=True)
    publicKey = models.CharField(max_length=140)
