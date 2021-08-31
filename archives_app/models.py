from django.db import models
from django.db.models.deletion import SET_DEFAULT


class DocumentSubjetc(models.Model):
    name_of_subeject = models.CharField(max_length=100, blank= True)
    temporality = models.DateField(blank = True) #em anos, tem que ver se essa DateField vai prestar

class DocumentType(models.Model):
    name_of_document = models.CharField(max_length=100,blank = True)
    temporality = models.DateField() #em anos, tem que ver se essa DateField vai prestar

class PublicWorker(models.Model):
    name = models.CharField(max_length=100, blank=True)
    cpf = models.CharField(max_length=11, blank=True)
    office = models.CharField(max_length=100, blank=True)
    class_worker = models.CharField(max_length=100, blank=True)
    capacity = models.CharField(max_length=100, blank=True)
    county = models.CharField(max_length=100, blank=True)

class Unity(models.Model):

    
    name_of_unity = models.CharField(max_length=100, blank= True)
    unity_abbreviation = models.CharField(max_length=20, blank= True)
    administrative_bond = models.CharField(max_length=100, blank= True)
    bond_abbreviation = models.CharField(max_length=20, blank = True)
    type_of_unity = models.CharField(max_length=30, blank = True)
    municipality = models.CharField(max_length=100, blank = True)
    telephone_number = models.CharField(max_length=8, blank = True)
    note = models.CharField(max_length= 100, blank = True)

class BoxAbbreviations(models.Model):
    number = models.IntegerField(blank=True)
    abbreviation = models.CharField(max_length=20, blank=True)
    name = models.CharField(max_length=100, blank=True)
    year = models.IntegerField(blank=True) #talvez um DateField??

class ShelfE(models.Model): # 'E' estante
    number = models.IntegerField(blank=True)

class ShelfP(models.Model): # 'P' prateleira
    number = models.IntegerField(blank= True)


class FrontCover(models.Model):
    box_abbreviation = models.CharField(max_length=30, blank=True)



class Status(models.Model):
    filed = models.BooleanField(blank=True)
    unity_that_forwarded = models.CharField(max_length = 100, blank= True)
    document_requested = models.CharField(max_length = 100, blank = True)
    send_date = models.DateField(blank=True)