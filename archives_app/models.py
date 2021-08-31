from django.db import models

class BoxAbbreviations(models.Model):
    number = models.IntegerField(blank=True)
    abbreviation = models.CharField(max_length=20, blank=True)
    name = models.CharField(max_length=100, blank=True)
    year = models.IntegerField(blank=True)

class PublicWorker(models.Model):
    name = models.CharField(max_length=100, blank=True)
    cpf = models.CharField(max_length=11, blank=True)
    office = models.CharField(max_length=100, blank=True)
    class_worker = models.CharField(max_length=100, blank=True)
    capacity = models.CharField(max_length=100, blank=True)
    county = models.CharField(max_length=100, blank=True)