from rest_framework import serializers
from .models import BoxAbbreviations
from .models import PublicWorker


class BoxAbbreviationsSerializer(serializers.ModelSerializer):
    number = serializers.IntegerField(required=False)
    abbreviation = serializers.CharField(max_length=20, required=False)
    name = serializers.CharField(max_length=100, required=False)
    year = serializers.IntegerField(required=False)

    class Meta:
        model = BoxAbbreviations
        fields = ['number', 'abbreviation', 'name', 'year']

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