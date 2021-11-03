from django.db import models
from django.core.validators import MinValueValidator


class DocumentSubject(models.Model):
    subject_name = models.CharField(max_length=100, blank=True, null=True)
    temporality = models.IntegerField(blank=True, null=True)


class DocumentType(models.Model):
    document_name = models.CharField(max_length=100, blank=True, null=True)
    temporality = models.IntegerField(blank=True, null=True)


class PublicWorker(models.Model):
    name = models.CharField(max_length=150)
    cpf = models.CharField(max_length=11)


class Unity(models.Model):
    unity_name = models.CharField(max_length=100, blank=True, null=True)
    unity_abbreviation = models.CharField(max_length=20, blank=True, null=True)
    administrative_bond = models.CharField(max_length=100, blank=True, null=True)
    bond_abbreviation = models.CharField(max_length=20, blank=True, null=True)
    municipality = models.CharField(max_length=100, blank=True, null=True)
    telephone_number = models.CharField(max_length=11, blank=True, null=True)
    notes = models.CharField(max_length=300, blank=True, null=True)


class BoxAbbreviations(models.Model):
    number = models.CharField(max_length=100, blank=True, null=True)
    abbreviation = models.CharField(max_length=20, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1900)])


class Shelf(models.Model):
    number = models.IntegerField(validators=[MinValueValidator(0)])


class Rack(models.Model):
    number = models.IntegerField(validators=[MinValueValidator(0)])


class FrontCover(models.Model):
    box_abbreviation = models.CharField(max_length=30, blank=True, null=True)
