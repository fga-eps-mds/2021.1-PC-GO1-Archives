from django.db import models
from django.contrib.postgres.fields import ArrayField
from archives_app.fields_models import (BoxAbbreviations, DocumentType,
                                        DocumentSubject, Shelf,
                                        Unity, Rack)
from django.core.validators import MinValueValidator


class Document(models.Model):
    process_number = models.CharField(max_length=20)
    sender_unity = models.ForeignKey(Unity, on_delete=models.PROTECT)
    abbreviation_id = models.ForeignKey(BoxAbbreviations, on_delete=models.PROTECT,
                                        blank=True, null=True)
    shelf_id = models.ForeignKey(Shelf, on_delete=models.PROTECT, blank=True,
                                 null=True)
    rack_id = models.ForeignKey(Rack, on_delete=models.PROTECT, blank=True,
                                null=True)
    notes = models.CharField(max_length=300, blank=True, null=True)
    filer_user = models.CharField(max_length=150)


class Relation(Document):
    document_type_id = models.ManyToManyField(DocumentType)
    number = models.CharField(max_length=20)
    received_date = models.DateField()


class OriginBoxSubject(models.Model):
    name = models.CharField(max_length=100)
    dates = ArrayField(models.DateField())


class OriginBox(models.Model):
    number = models.CharField(max_length=20)
    year = models.IntegerField(validators=[MinValueValidator(1900)])
    subject = models.ManyToManyField(OriginBoxSubject)


class ArchivalRelation(Relation):
    number_of_boxes = models.IntegerField(validators=[MinValueValidator(0)],
                                          blank=True, null=True)
    origin_box_id = models.ManyToManyField(OriginBox)
    document_url = models.URLField(blank=True, null=True)
    cover_sheet = models.CharField(max_length=100, blank=True, null=True)


class FrequencyRelation(Relation):
    reference_period = ArrayField(models.DateField())


class FrequencySheet(models.Model):
    person_name = models.CharField(max_length=150)
    cpf = models.CharField(max_length=11)
    role = models.CharField(max_length=100)
    category = models.CharField(max_length=100, blank=True, null=True)
    workplace = models.CharField(max_length=100)
    municipal_area = models.CharField(max_length=100)
    reference_period = models.DateField()
    abbreviation_id = models.ForeignKey(BoxAbbreviations, on_delete=models.PROTECT,
                                        blank=True, null=True)
    shelf_id = models.ForeignKey(Shelf, on_delete=models.PROTECT, blank=True,
                                 null=True)
    rack_id = models.ForeignKey(Rack, on_delete=models.PROTECT, blank=True,
                                null=True)
    notes = models.CharField(max_length=300, blank=True, null=True)
    process_number = models.CharField(max_length=20, blank=True, null=True)


class AdministrativeProcess(Document):
    notice_date = models.DateField()
    interested = models.CharField(max_length=150)
    cpf_cnpj = models.CharField(max_length=15, blank=True, null=True)
    subject_id = models.ForeignKey(DocumentSubject, on_delete=models.PROTECT)
    dest_unity_id = models.ForeignKey(Unity, on_delete=models.PROTECT, blank=True,
                                      null=True, related_name='unity')
    reference_month_year = models.DateField(blank=True, null=True)
    sender_user = models.CharField(max_length=150, blank=True, null=True)
    archiving_date = models.DateField(blank=True, null=True)
    is_filed = models.BooleanField(blank=True, null=True)
    is_eliminated = models.BooleanField(blank=True, null=True)
    send_date = models.DateField(blank=True, null=True)
    administrative_process_number = models.CharField(max_length=15, blank=True, null=True)
    unity_id = models.ForeignKey(Unity, on_delete=models.PROTECT, blank=True,
                                 null=True, related_name='unfiled_unity')
