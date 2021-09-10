from django.db import models
from archives_app.fields_models import (BoxAbbreviations, DocumentType, PublicWorker,
                                        DocumentSubject, Status, Shelf, Unity)


class Document(models.Model):
    process_number = models.CharField(max_length=100)
    sender_unity = models.CharField(max_length=100)
    abbreviation_id = models.ForeignKey(BoxAbbreviations, on_delete=models.PROTECT)
    shelf_id = models.ForeignKey(Shelf, on_delete=models.PROTECT)
    notes = models.CharField(max_length=300)


class Relation(Document):
    document_type = models.ForeignKey(DocumentType, on_delete=models.PROTECT)
    number = models.CharField(max_length=1000)
    received_date = models.DateField()


class OriginBox(models.Model):
    number = models.CharField(max_length=100)
    year = models.IntegerField()
    subject = models.CharField(max_length=150)
    date = models.DateField()


class ArchivalRelation(Relation):
    box_receiver = models.ForeignKey(PublicWorker, on_delete=models.PROTECT) # Will be replaced by User when user is created
    number_of_boxes = models.IntegerField()
    origin_box_id = models.ManyToManyField(OriginBox)
    document_url = models.URLField()
    cover_sheet = models.CharField(max_length=100)


class FrequencyRelation(Relation):
    due_date = models.DateField()
    frequency_receiver_id = models.ForeignKey(PublicWorker, on_delete=models.PROTECT) # Will be replaced by User when user is created


class FrequencySheet(models.Model):
    public_worker_id = models.ForeignKey(PublicWorker, on_delete=models.PROTECT) # Will be replaced by User when user is created
    due_date = models.DateField()
    abbreviation_id = models.ForeignKey(BoxAbbreviations, on_delete=models.PROTECT)
    shelf_id = models.ForeignKey(Shelf, on_delete=models.PROTECT)
    notes = models.CharField(max_length=300)
    process_number = models.CharField(max_length=1000)


class AdministrativeProcess(Document):
    notice_date = models.DateField()
    interested = models.CharField(max_length=150)
    cpf_cnpj = models.CharField(max_length=15)
    subject = models.ForeignKey(DocumentSubject, on_delete=models.PROTECT)
    dest_unity = models.ForeignKey(Unity, on_delete=models.PROTECT)
    reference_month_year = models.FloatField()
    sender_worker = models.ForeignKey(PublicWorker, on_delete=models.PROTECT) # Will be replaced by User when user is created
    archiving_date = models.DateField()
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    # user = will be created as a foreignkey to the User class whe the user class is created
