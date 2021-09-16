from django.db import models
from archives_app.fields_models import (BoxAbbreviations, DocumentType,
                                        DocumentSubject, Status, Shelf,
                                        Unity)


class Document(models.Model):
    process_number = models.CharField(max_length=20)
    sender_unity = models.ForeignKey(Unity, on_delete=models.PROTECT)
    abbreviation_id = models.ForeignKey(BoxAbbreviations, on_delete=models.PROTECT,
                                        blank=True, null=True)
    shelf_id = models.ForeignKey(Shelf, on_delete=models.PROTECT, blank=True,
                                 null=True)
    notes = models.CharField(max_length=300, blank=True, null=True)
    filer_user = models.CharField(max_length=150)


class Relation(Document):
    document_type_id = models.ForeignKey(DocumentType, on_delete=models.PROTECT)
    number = models.CharField(max_length=20)
    received_date = models.DateField()


class ReferencePeriod(models.Model):
    period_month_year = models.DateField()


class OriginBox(models.Model):
    number = models.CharField(max_length=20)
    year = models.IntegerField()
    subject = models.CharField(max_length=150)
    date = models.DateField()


class ArchivalRelation(Relation):
    number_of_boxes = models.IntegerField(blank=True, null=True)
    origin_box_id = models.ManyToManyField(OriginBox)
    document_url = models.URLField(blank=True, null=True)
    cover_sheet = models.CharField(max_length=100, blank=True, null=True)


class FrequencyRelation(Relation):
    reference_period = models.ManyToManyField(ReferencePeriod)


class FrequencySheet(models.Model):
    person_name = models.CharField(max_length=150)
    cpf = models.CharField(max_length=11)
    role = models.CharField(max_length=100)
    category = models.CharField(max_length=100, blank=True, null=True)
    workplace = models.CharField(max_length=100)
    municipal_area = models.CharField(max_length=100)
    reference_period = models.ManyToManyField(ReferencePeriod)
    abbreviation_id = models.ForeignKey(BoxAbbreviations, on_delete=models.PROTECT,
                                        blank=True, null=True)
    shelf_id = models.ForeignKey(Shelf, on_delete=models.PROTECT, blank=True,
                                 null=True)
    notes = models.CharField(max_length=300, blank=True, null=True)
    process_number = models.CharField(max_length=20, blank=True, null=True)


class AdministrativeProcess(Document):
    notice_date = models.DateField()
    interested = models.CharField(max_length=150)
    cpf_cnpj = models.CharField(max_length=15, blank=True, null=True)
    subject_id = models.ForeignKey(DocumentSubject, on_delete=models.PROTECT)
    dest_unity_id = models.ForeignKey(Unity, on_delete=models.PROTECT, blank=True,
                                      null=True)
    reference_month_year = models.DateField(blank=True, null=True)
    sender_user = models.CharField(max_length=150, blank=True, null=True)
    archiving_date = models.DateField(blank=True, null=True)
    status_id = models.ForeignKey(Status, on_delete=models.PROTECT)
