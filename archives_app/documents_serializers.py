from rest_framework import serializers
from archives_app.documents_models import (FrequencyRelation, ArchivalRelation,
                                           AdministrativeProcess, OriginBox,
                                           FrequencySheet)


class ArchivalRelationSerializer(serializers.ModelSerializer):
    # abbreviation_id = serializers.ForeignKey(BoxAbbreviations, on_delete=models.PROTECT,
    #                                     required=False)
    # shelf_id = serializers.ForeignKey(Shelf, on_delete=models.PROTECT, required=False)
    # notes = serializers.CharField(max_length=300, required=False)
    # number_of_boxes = serializers.IntegerField(required=False)
    # document_url = serializers.URLField(required=False)
    # cover_sheet = serializers.CharField(max_length=100, required=False)

    class Meta:
        model = ArchivalRelation
        fields = '__all__'


class FrequencyRelationSerializer(serializers.ModelSerializer):
    # abbreviation_id = serializers.ForeignKey(BoxAbbreviations, on_delete=models.PROTECT,
    #                                     required=False)
    # shelf_id = serializers.ForeignKey(Shelf, on_delete=models.PROTECT, required=False)
    # notes = serializers.CharField(max_length=300, required=False)

    class Meta:
        model = FrequencyRelation
        fields = '__all__'


class AdministrativeProcessSerializer(serializers.ModelSerializer):

    class Meta:
        model = AdministrativeProcess
        fields = '__all__'


class OriginBoxSerializer(serializers.ModelSerializer):

    class Meta:
        model = OriginBox
        fields = '__all__'


class FrequencySheetSerializer(serializers.ModelSerializer):
    # abbreviation_id = serializers.ForeignKey(BoxAbbreviations, on_delete=models.PROTECT,
    #                                         required=False)
    # shelf_id = serializers.ForeignKey(Shelf, on_delete=models.PROTECT, required=False)
    # notes = serializers.CharField(max_length=300, required=False)
    # process_number = serializers.CharField(max_length=20, required=False)

    class Meta:
        model = FrequencySheet
        fields = '__all__'
