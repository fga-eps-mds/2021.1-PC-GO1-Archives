from rest_framework import serializers
from .documents_models import AdministrativeProcess, FrequencyDocument, FrequencyRelation
from .documents_models import ArchivingRelation


class AdministrativeProcessSerializer(serializers.ModelSerializer):
    process_number = serializers.IntegerField(max_length=100, required=True)
    booked_date = serializers.DateField(required=True, null=True)
    interested = serializers.CharField(max_length=100, required=True)
    cpf_cnpj = serializers.CharField(max_length=11, required=False)
    subject = serializers.CharField(max_length=100, required=True)
    destination_unity = serializers.CharField(max_length=100, required=False)
    refrence_date = serializers.CharField(max_length=30, required=False)
    unity_forwarded_for_archiving = serializers.CharField(max_length=100, required=False)
    forwarded_by = serializers.CharField(max_length=100, required=False)
    arquiving_date = serializers.DateField(required=False, null=True)
    box_abbreviation = serializers.CharField(max_length=30, required=False)
    shelfe_number = serializers.IntegerField(max_length=20, required=False)
    shelfp_number = serializers.IntegerField(max_length=20, required=False)
    worker_who_registered = serializers.CharField(max_length=100, required=False)
    status = serializers.BooleanField(required=False)
    notes = serializers.CharField(max_length=200, required=False)

    class Meta:
        model = AdministrativeProcess
        fields = '__all__'


class FrequencyRelationSerializer(serializers.ModelSerializer):
    process_number = serializers.IntegerField(max_length=20, required=True)
    document_type = serializers.CharField(max_length=100, required=True)
    document_number = serializers.IntegerField(max_length=20, required=True)
    unity_forwarded_for_archiving = serializers.CharField(max_length=100, required=True)
    time_course = serializers.JSONField(max_length=300, blank=False)
    worker_who_recieved_frequencies = serializers.CharField(max_length=100, required=True)
    receipt_date = serializers.DateField(required=True)
    box_abbreviation = serializers.CharField(max_length=30, required=False)
    shelfe_number = serializers.IntegerField(max_length=20, required=False)
    shelfp_number = serializerss.IntegerField(max_length=20, required=False)
    notes = serializers.CharField(max_length=200, required=False)

    class Meta:
        model = FrequencyRelation
        fields = '__all__'


class FrequencyDocumentSerializer(serializers.ModelSerializer):
    worker_name = serializers.CharField(max_length=100, required=True)
    cpf = serializers.CharField(max_length=11, required=True)
    workload = serializers.CharField(max_length=100, required=True)
    worker_class = serializers.CharField(max_length=100, required=True)
    time_course = serializers.CharField(max_length=100, required=True)
    capacity = serializers.CharField(max_length=100, required=True)
    municipality = serializers.CharField(max_length=100, required=True)
    process_number_that_sent_frequency = models.IntegerField(max_length=20, required=False)
    box_abbreviation = serializers.CharField(max_length=30, required=False)
    shelfe_number = serializers.IntegerField(max_length=20, required=False)
    shelfp_number = serializers.IntegerField(max_length=20, brequired=False)
    notes = serializers.CharField(max_length=200, required=False)

    class Meta:
        model = FrequencyDocument
        fields = '__all__'


class ArchivingRelationSerializer(serializers.ModelSerializer):
    process_number = serializers.IntegerField(max_length=20, required=True)
    document_type = serializers.CharField(max_length=100, required=True)
    document_number = serializers.IntegerField(max_length=20, required=True)
    unity_forwarded_for_archiving = serializers.CharField(max_length=100, required=True)
    receipt_date = serializers.DateField(required=True)
    worker_who_recieved_box = serializers.CharField(max_length=100, required=True)
    number_of_boxes_received_for_archiving = serializers.ImageField(max_length=3, required=False)
    origin_box = serializers.JSONField(max_length=300, required=False)
    subjects = serializers.JSONField(max_length=300, required=False)
    dates = serializers.JSONField(max_length=300, required=False)
    box_abbreviation = serializers.CharField(max_length=30, required=False)
    shelfe_number = serializers.IntegerField(max_length=20, required=False)
    shelfp_number = serializers.IntegerField(max_length=20, required=False)
    notes = serializers.CharField(max_length=200, required=False)
    document_to_attach = serializers.ImageField(required=False)

    class Meta:
        model = ArchivingRelation
        fields = '__all__'