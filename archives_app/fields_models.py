from django.db import models


class DocumentSubject(models.Model):
    subject_name = models.CharField(max_length=100, blank=True, null=True)
    temporality = models.DateField(blank=True, null=True)


class DocumentType(models.Model):
    document_name = models.CharField(max_length=100, blank=True, null=True)
    temporality = models.DateField(blank=True, null=True)


class Unity(models.Model):
    unity_name = models.CharField(max_length=100, blank=True, null=True)
    unity_abbreviation = models.CharField(max_length=20, blank=True, null=True)
    administrative_bond = models.CharField(max_length=100, blank=True, null=True)
    bond_abbreviation = models.CharField(max_length=20, blank=True, null=True)
    type_of_unity = models.CharField(max_length=30, blank=True, null=True)
    municipality = models.CharField(max_length=100, blank=True, null=True)
    telephone_number = models.CharField(max_length=11, blank=True, null=True)
    notes = models.CharField(max_length=300, blank=True, null=True)


class BoxAbbreviations(models.Model):
    number = models.IntegerField(blank=True, null=True)
    abbreviation = models.CharField(max_length=20, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)


class Shelf(models.Model):
    number = models.IntegerField()


class Rack(models.Model):
    number = models.IntegerField()


class FrontCover(models.Model):
    box_abbreviation = models.CharField(max_length=30, blank=True, null=True)


class Status(models.Model):
    is_filed = models.BooleanField(blank=True, null=True)
    eliminated = models.BooleanField(blank=True, null=True)
    sent_from = models.CharField(max_length=100, blank=True, null=True)
    requested_document = models.CharField(max_length=100, blank=True, null=True)
    send_date = models.DateField(blank=True, null=True)
