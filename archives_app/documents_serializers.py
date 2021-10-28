from rest_framework import serializers
from archives_app.documents_models import (FrequencyRelation, BoxArchiving,
                                           AdministrativeProcess, OriginBox,
                                           FrequencySheet, DocumentTypes)


class FrequencySupport(serializers.ModelSerializer):
    def get_document_type(self, obj):
        if obj.document_type_id is not None:
            return obj.document_type_id.document_name
        return None


class BoxArchivingSerializer(serializers.ModelSerializer):

    def get_shelf_number(self, obj):
        if obj.shelf_id is not None:
            return obj.shelf_id.number
        return None

    def get_rack_number(self, obj):
        if obj.rack_id is not None:
            return obj.rack_id.number
        return None

    def get_abbreviation_name(self, obj):
        if obj.abbreviation_id is not None:
            return obj.abbreviation_id.name
        return ""

    def get_sender_unity(self, obj):
        if obj.sender_unity is not None:
            return obj.sender_unity.unity_name
        return ""

    shelf_number = serializers.SerializerMethodField('get_shelf_number')
    rack_number = serializers.SerializerMethodField('get_rack_number')
    abbreviation_name = serializers.SerializerMethodField('get_abbreviation_name')
    sender_unity_name = serializers.SerializerMethodField('get_sender_unity')

    class Meta:
        model = BoxArchiving
        fields = (
            "id",
            "process_number",
            "sender_unity",
            "notes",
            "received_date",
            "document_url",
            "cover_sheet",
            "filer_user",
            "abbreviation_name",
            "shelf_number",
            "rack_number",
            "origin_box_id",
            "abbreviation_id",
            "shelf_id",
            "rack_id",
            "document_types",
            "sender_unity_name"
        )


class FrequencyRelationSerializer(FrequencySupport):

    def get_sender_unity(self, obj):
        if obj.sender_unity is not None:
            return obj.sender_unity.unity_name
        return ""

    document_type_name = serializers.SerializerMethodField(
        'get_document_type'
    )
    sender_unity_name = serializers.SerializerMethodField('get_sender_unity')

    class Meta:
        model = FrequencyRelation
        fields = (
            "id",
            "process_number",
            "notes",
            "document_date",
            "received_date",
            "temporality_date",
            "reference_period",
            "filer_user",
            "sender_unity",
            "document_type_id",
            "document_type_name",
            "sender_unity_name"
        )


class AdministrativeProcessSerializer(serializers.ModelSerializer):

    def get_document_subject(self, obj):
        if obj.subject_id is not None:
            return obj.subject_id.subject_name
        return None

    def get_sender_unity(self, obj):
        if obj.sender_unity is not None:
            return obj.sender_unity.unity_name
        return ""

    sender_unity_name = serializers.SerializerMethodField('get_sender_unity')
    document_subject_name = serializers.SerializerMethodField(
        'get_document_subject'
    )

    class Meta:
        model = AdministrativeProcess
        fields = ("id",
                  "process_number",
                  "notes",
                  "filer_user",
                  "notice_date",
                  "interested",
                  "cpf_cnpj",
                  "reference_month_year",
                  "sender_user",
                  "archiving_date",
                  "is_filed",
                  "is_eliminated",
                  "temporality_date",
                  "send_date",
                  "administrative_process_number",
                  "sender_unity",
                  "subject_id",
                  "dest_unity_id",
                  "unity_id",
                  "document_subject_name",
                  "sender_unity_name"
                  )


class OriginBoxSerializer(serializers.ModelSerializer):

    class Meta:
        model = OriginBox
        fields = '__all__'


class DocumentTypesSerializer(serializers.ModelSerializer):

    class Meta:
        model = DocumentTypes
        fields = '__all__'


class FrequencySheetSerializer(FrequencySupport):

    document_type_name = serializers.SerializerMethodField(
        'get_document_type'
    )

    class Meta:
        model = FrequencySheet
        fields = ("id",
                  "person_id",
                  "cpf",
                  "role",
                  "category",
                  "workplace",
                  "municipal_area",
                  "reference_period",
                  "notes",
                  "process_number",
                  "document_type_id",
                  "temporality_date",
                  "document_type_name"
                  )
