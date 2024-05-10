from django.db import models
from datetime import datetime


class List(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)
    date1 = models.CharField(max_length=30, blank=True, null=True)
    date2 = models.CharField(max_length=30, blank=True, null=True)
    year1 = models.IntegerField(max_length=4, blank=False, null=False)
    year2 = models.IntegerField(max_length=4, blank=False, null=False)
    profession = models.CharField(max_length=30, blank=True, null=True)
    country = models.CharField(max_length=30, blank=True, null=True)
    photo = models.CharField(max_length=30, blank=True, null=True)
    wiki = models.CharField(max_length=30, blank=True, null=True)


