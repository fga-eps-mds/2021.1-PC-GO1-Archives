from rest_framework import serializers
from archives_app.documents_models import (FrequencyRelation, BoxArchiving,
                                           AdministrativeProcess, OriginBox,
                                           FrequencySheet, DocumentTypes)


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

    shelf_number = serializers.SerializerMethodField('get_shelf_number')
    rack_number = serializers.SerializerMethodField('get_rack_number')
    abbreviation_name = serializers.SerializerMethodField('get_abbreviation_name')

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
            "document_types"
        )


class FrequencyRelationSerializer(serializers.ModelSerializer):

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
        )


class AdministrativeProcessSerializer(serializers.ModelSerializer):

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
                  )


class OriginBoxSerializer(serializers.ModelSerializer):

    class Meta:
        model = OriginBox
        fields = '__all__'


class DocumentTypesSerializer(serializers.ModelSerializer):

    class Meta:
        model = DocumentTypes
        fields = '__all__'


class FrequencySheetSerializer(serializers.ModelSerializer):

    class Meta:
        model = FrequencySheet
        fields = ("id",
                  "person_name",
                  "cpf",
                  "role",
                  "category",
                  "workplace",
                  "municipal_area",
                  "reference_period",
                  "notes",
                  "process_number",
                  "document_type_id"
                  )
