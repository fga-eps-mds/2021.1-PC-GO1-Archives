from rest_framework import serializers
from .fields_models import BoxAbbreviations, FrontCover, PublicWorker, DocumentSubject
from .fields_models import DocumentType, Shelf, Status, Unity


class DocumentSubjectSerializer(serializers.ModelSerializer):
    subject_name = serializers.CharField(max_length=100, required=False)
    temporality = serializers.DateField(required=False)

    class Meta:

        model = DocumentSubject
        fields = '__all__'


class DocumentTypeSerializer(serializers.ModelSerializer):
    document_name = serializers.CharField(max_length=100, required=False)
    temporality = serializers.DateField(required=False)

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
    telephone_number = serializers.CharField(max_length=8, required=False)
    note = serializers.CharField(max_length=100, required=False)

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


class ShelfSerializer(serializers.ModelSerializer):
    shelfe_number = serializers.IntegerField(required=False)
    shelfp_number = serializers.IntegerField(required=False)

    class Meta:
        model = Shelf
        fields = '__all__'


class FrontCoverSerializer(serializers.ModelSerializer):
    box_abbreviation = serializers.CharField(max_length=30, required=False)

    class Meta:
        model = FrontCover
        fields = '__all__'


class StatusSerializer(serializers.ModelSerializer):
    filed = serializers.BooleanField(required=False)
    eliminated = serializers.BooleanField(required=False)
    sent_from = serializers.CharField(max_length=100, required=False)
    document_requested = serializers.CharField(max_length=100, required=False)
