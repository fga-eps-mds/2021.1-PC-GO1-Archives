from rest_framework import serializers
from .models import BoxAbbreviations, FrontCover, PublicWorker, DocumentSubjetc, DocumentType, ShelfE, ShelfP, Status, Unity



class DocumentSubjetcSerializer(serializers.ModelSerializer):
    name_of_subeject = serializers.CharField(max_length=100, required = False)
    temporality = serializers.DateField(required = False) #em anos, tem que ver se essa DateField vai prestar
    
    class Meta:
        model = DocumentSubjetc
        fields = '__all__'

class DocumentTypeSerializer(serializers.ModelSerializer):
    name_of_document = serializers.CharField(max_length=100,required = False)
    temporality = serializers.DateField(required = False) #em anos, tem que ver se essa DateField vai prestar
    
    class Meta:
        model = DocumentType
        fields = '__all__'


class PublicWorkerSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100, required=False)
    cpf = serializers.CharField(max_length=11, required=False)
    office = serializers.CharField(max_length=100, required=False)
    class_worker = serializers.CharField(required=False)
    capacity = serializers.CharField(required=False)
    county = serializers.CharField(required=False)

    class Meta:
        model = PublicWorker
        fields = '__all__'



class UnitySerializer(serializers.ModelSerializer): 
    name_of_unity = serializers.CharField(max_length=100, required=False)
    unity_abbreviation = serializers.CharField(max_length=20, required=False)
    administrative_bond = serializers.CharField(max_length=100, required=False)
    bond_abbreviation = serializers.CharField(max_length=20, required=False)
    type_of_unity = serializers.CharField(max_length=30, required=False)
    municipality = serializers.CharField(max_length=100, required=False)
    telephone_number = serializers.CharField(max_length=8, required=False)
    note = serializers.CharField(max_length= 100, required=False)

    class Meta:
        model = Unity
        fields = '__all__'

class BoxAbbreviationsSerializer(serializers.ModelSerializer):
    number = serializers.IntegerField(required=False)
    abbreviation = serializers.CharField(max_length=20, required=False)
    name = serializers.CharField(max_length=100, required=False)
    year = serializers.IntegerField(required=False)

    class Meta:
        model = BoxAbbreviations
        fields = ['number', 'abbreviation', 'name', 'year']

class ShelfESerializer(serializers.ModelSerializer): 
    number = serializers.IntegerField(required = False)

    class Meta:
        model = ShelfE
        fields = '__all__'

class ShelfPSerializer(serializers.ModelSerializer): 
    number = serializers.IntegerField(required = False)

    class Meta: 
        model = ShelfP
        fields = '__all__'


#status


class FrontCoverSerializer(serializers.ModelSerializer):
    box_abbreviation = serializers.CharField(max_length=30, required = False)

    class Meta: 
        model = FrontCover
        fields = '__all__'

class StatusSerializer(serializers.ModelSerializer):
    filed = serializers.BooleanField(required = False)
    unity_that_forwarded = serializers.CharField(max_length = 100, required = False)
    document_requested = serializers.CharField(max_length = 100, required = False)
    send_date = serializers.DateField(required = False)

    class Meta:
        model = Status
        fields = '__all__'
