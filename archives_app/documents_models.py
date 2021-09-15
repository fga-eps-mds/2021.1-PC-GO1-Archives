from django.db import models
from archives_app.fields_models import (BoxAbbreviations, DocumentType, PublicWorker,
                                        DocumentSubject, Status, Shelf,
                                        Unity)


class Document(models.Model):
    process_number = models.CharField(max_length=20)
    sender_unity = models.CharField(max_length=100)
    abbreviation_id = models.ForeignKey(BoxAbbreviations, on_delete=models.PROTECT,
                                        blank=True)
    shelf_id = models.ForeignKey(Shelf, on_delete=models.PROTECT, blank=True)
    notes = models.CharField(max_length=300, blank=True)
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
    number_of_boxes = models.IntegerField()
    origin_box_id = models.ManyToManyField(OriginBox)
    document_url = models.URLField()
    cover_sheet = models.CharField(max_length=100)


class FrequencyRelation(Relation):
    reference_period = models.ManyToManyField(ReferencePeriod)


class FrequencySheet(models.Model):
    person_name = models.CharField(max_length=150)
    reference_period = models.ManyToManyField(ReferencePeriod)
    abbreviation_id = models.ForeignKey(BoxAbbreviations, on_delete=models.PROTECT)
    shelf_id = models.ForeignKey(Shelf, on_delete=models.PROTECT)
    notes = models.CharField(max_length=300)
    process_number = models.CharField(max_length=20)


class AdministrativeProcess(Document):
    notice_date = models.DateField()
    interested = models.CharField(max_length=150)
    cpf_cnpj = models.CharField(max_length=15)
    subject_id = models.ForeignKey(DocumentSubject, on_delete=models.PROTECT)
    dest_unity_id = models.ForeignKey(Unity, on_delete=models.PROTECT)
    reference_month_year = models.DateField()
    sender_user = models.CharField(max_length=150)
    archiving_date = models.DateField()
    status_id = models.ForeignKey(Status, on_delete=models.PROTECT)
