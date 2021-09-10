from rest_framework import serializers
from archives_app.documents_models import (FrequencyRelation, ArchivalRelation,
                                           AdministrativeProcess, OriginBox,
                                           FrequencySheet)


class ArchivalRelationSerializer(serializers.ModelSerializer):

    class Meta:
        model = ArchivalRelation
        fields = '__all__'


class FrequencyRelationSerializer(serializers.ModelSerializer):

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

    class Meta:
        model = FrequencySheet
        fields = '__all__'
