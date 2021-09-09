from django.db import models
from django.db.models.fields import CharField

class AdministrativeProcess(models.Model):
    process_number = models.IntegerField(max_length=100, blank=False)
    booked_date = models.DateField(blank=False, null=True)
    interested = models.CharField(max_length=100, blank=False)
    cpf_cnpj = models.CharField(max_length=11, blank=True)
    subject = models.CharField(max_length=100, blank=False)
    destination_unity = models.CharField(max_length=100, blank=True)
    refrence_date = models.CharField(max_length=30, blank=True)
    unity_forwarded_for_archiving = models.CharField(max_length=100, blank=True)
    forwarded_by = models.CharField(max_length=100, blank=True)
    arquiving_date = models.DateField(blank=True, null=True)
    box_abbreviation = models.CharField(max_length=30, blank=True)
    shelfe_number = models.IntegerField(max_length=20, blank=True)
    shelfp_number = models.IntegerField(max_length=20, blank=True)
    worker_who_registered = models.CharField(max_length=100, blank=True)
    status = models.BooleanField(blank=False)
    notes = models.CharField(max_length=200, blank=True)


class FrequencyRelation(models.Model):
    process_number = models.IntegerField(max_length=20, blank=False)
    document_type = models.CharField(max_length=100, blank=False)
    document_number = models.IntegerField(max_length=20, blank=False)
    unity_forwarded_for_archiving = models.CharField(max_length=100, blank=False)
    time_course = models.JSONField(max_length=300, blank=False)
    worker_who_recieved_frequencies = models.CharField(max_length=100, blank=False)
    receipt_date = models.DateField(blank=False)
    box_abbreviation = models.CharField(max_length=30, blank=True)
    shelfe_number = models.IntegerField(max_length=20, blank=True)
    shelfp_number = models.IntegerField(max_length=20, blank=True)
    notes = models.CharField(max_length=200, blank=True)


class FrequencyDocument(models.Model):  #frequencys
    worker_name = models.CharField(max_length=100, blank=False)
    cpf = models.CharField(max_length=11, blank=True)
    workload = models.CharField(max_length=100, blank=False)
    worker_class = models.CharField(max_length=100, blank=True)
    time_course = models.CharField(max_length=100, blank=False)
    capacity = models.CharField(max_length=100, blank=False)
    municipality = models.CharField(max_length=100, blank=False)
    process_number_that_sent_frequency = models.IntegerField(max_length=20, blank=True)
    box_abbreviation = models.CharField(max_length=30, blank=True)
    shelfe_number = models.IntegerField(max_length=20, blank=True)
    shelfp_number = models.IntegerField(max_length=20, blank=True)
    notes = models.CharField(max_length=200, blank=True)


class ArchivingRelation(models.Model):
    process_number = models.IntegerField(max_length=20, blank=False)
    document_type = models.CharField(max_length=100, blank=False)
    document_number = models.IntegerField(max_length=20, blank=False)
    unity_forwarded_for_archiving = models.CharField(max_length=100, blank=False)
    receipt_date = models.DateField(blank=False)
    worker_who_recieved_box = models.CharField(max_length=100, blank=False)
    number_of_boxes_received_for_archiving = models.ImageField(max_length=3, blank=True)
    origin_box = models.JSONField(max_length=300, blank=True) #numero e ano
    subjects = models.JSONField(max_length=300, blank=True) #por caixa de origem
    dates = models.JSONField(max_length=300, blank=True) #dos assuntos por caixa de origem 
    box_abbreviation = models.CharField(max_length=30, blank=True)
    shelfe_number = models.IntegerField(max_length=20, blank=True)
    shelfp_number = models.IntegerField(max_length=20, blank=True)
    notes = models.CharField(max_length=200, blank=True)
    document_to_attach = models.ImageField(blank=True)
