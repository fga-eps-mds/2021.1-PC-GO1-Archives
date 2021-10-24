from rest_framework import viewsets, views
from rest_framework.response import Response
from .fields_serializers import BoxAbbreviationsSerializer
from .fields_serializers import (DocumentSubjectSerializer, DocumentTypeSerializer,
                                 UnitySerializer, RackSerializer, PublicWorkerSerializer)
from .fields_serializers import FrontCoverSerializer, ShelfSerializer
from .fields_models import BoxAbbreviations, DocumentSubject, DocumentType
from .fields_models import Unity, Shelf, FrontCover, Rack, PublicWorker
from .documents_models import (BoxArchiving, FrequencyRelation, AdministrativeProcess,
                               OriginBox, FrequencySheet, OriginBoxSubject, DocumentTypes)
from .documents_serializers import (FrequencySheetSerializer,
                                    AdministrativeProcessSerializer,
                                    FrequencyRelationSerializer,
                                    BoxArchivingSerializer)
import json


class DocumentSubjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows document subjects to be viewed or edited.
    """
    queryset = DocumentSubject.objects.all()
    serializer_class = DocumentSubjectSerializer


class DocumentTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows document types to be viewed or edited.
    """
    queryset = DocumentType.objects.all()
    serializer_class = DocumentTypeSerializer


class UnityViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows unitys to be viewed or edited.
    """
    queryset = Unity.objects.all()
    serializer_class = UnitySerializer


class PublicWorkerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows public workers to be viewed or edited.
    """
    queryset = PublicWorker.objects.all()
    serializer_class = PublicWorkerSerializer


class BoxAbbreviationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows abbreviations to be viewed or edited.
    """
    queryset = BoxAbbreviations.objects.all()
    serializer_class = BoxAbbreviationsSerializer


class ShelfViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows shelfs to be viewed or edited.
    """
    queryset = Shelf.objects.all()
    serializer_class = ShelfSerializer


class RackViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows racks to be viewed or edited.
    """
    queryset = Rack.objects.all()
    serializer_class = RackSerializer


class FrontCoverViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = FrontCover.objects.all()
    serializer_class = FrontCoverSerializer


class FrequencyRelationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows frequency relations document type
    to be viewed or edited.
    """
    queryset = FrequencyRelation.objects.all()
    serializer_class = FrequencyRelationSerializer


class AdministrativeProcessViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows administrative process document type
    to be viewed or edited.
    """
    queryset = AdministrativeProcess.objects.all()
    serializer_class = AdministrativeProcessSerializer


class FrequencySheetViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows frequency sheet document type
    to be viewed or edited.
    """
    queryset = FrequencySheet.objects.all()
    serializer_class = FrequencySheetSerializer


class BoxArchivingView(views.APIView):

    def get(self, request):
        queryset = BoxArchiving.objects.all()
        serializer = BoxArchivingSerializer(queryset, many=True)
        return Response(serializer.data, status=200)

    def post(self, request):
        origin_box = request.data['origin_box_id']

        box = OriginBox.objects.create(number=origin_box['number'], year=origin_box['year'])
        for subject in origin_box['subjects_list']:
            sub = OriginBoxSubject.objects.create(name=subject['name'],
                                                  dates=subject['dates'])
            box.subject.add(sub.id)

        documents_list = request.data['document_types']
        docs = list()

        for doc_n in documents_list:
            d_id = DocumentType.objects.get(pk=doc_n['document_type_id'])
            d_t = DocumentTypes.objects.create(
                document_type_id=d_id,
                year=doc_n['year'],
                month=doc_n['month'],
                temporality_date=doc_n['temporality_date'])
            docs.append(d_t)

        sender_unity_id = Unity.objects.get(pk=request.data['sender_unity'])

        box_archiving = BoxArchiving.objects.create(
            process_number=request.data['process_number'],
            sender_unity=sender_unity_id,
            notes=request.data['notes'],
            received_date=request.data['received_date'],
            document_url=request.data['document_url'],
            cover_sheet=request.data['cover_sheet'],
            filer_user=request.data['filer_user']
        )

        if request.data['abbreviation_id'] != '':
            box_abbreviation_id = BoxAbbreviations.objects.get(
                pk=request.data['abbreviation_id']
            )
            box_archiving.abbreviation_id = box_abbreviation_id
            box_archiving.save()

        if request.data['shelf_id'] != '':
            shelf_number_id = Shelf.objects.get(pk=request.data['shelf_id'])
            box_archiving.shelf_id = shelf_number_id
            box_archiving.save()

        if box is not None:
            print(box.id)
            box_archiving.origin_box_id = box
            box_archiving.save()

        for doc in docs:
            box_archiving.document_types.add(doc.id)

        return Response(status=201)


class BoxArchivingDetailsView(views.APIView):

    def delete(self, request, pk):
        try:
            obj = BoxArchiving.objects.get(pk=pk)
            obj.delete()
            return Response(status=204)
        except BoxArchiving.DoesNotExist:
            error_dict = {"detail": "Not found."}
            return Response(error_dict, status=404)

    def get(self, request, pk):
        try:
            queryset = BoxArchiving.objects.get(pk=pk)
            serializer = BoxArchivingSerializer(queryset)

            doc_types = serializer.data['document_types']
            docs = list()
            for doc in doc_types:
                docs_dict = {}
                doc_n = DocumentTypes.objects.get(pk=doc)
                doc_type = DocumentTypeSerializer(doc_n.document_type_id)
                doc_type = doc_type.data
                docs_dict['document_type_id'] = doc_type['id']
                docs_dict['document_type_name'] = doc_type['document_name']
                docs_dict['year'] = doc_n.year
                docs_dict['month'] = doc_n.month
                docs_dict['temporality_date'] = doc_n.temporality_date
                docs.append(docs_dict)

            box_id = serializer.data['origin_box_id']
            box_dict = {}
            box = OriginBox.objects.get(pk=box_id)
            box_dict['number'] = box.number
            box_dict['year'] = box.year
            box_dict['subject_list'] = list()
            for subject in box.subject.all():
                box_dict['subject_list'].append({
                    'name': subject.name,
                    'date': subject.dates
                })

            final_dict = serializer.data
            final_dict['origin_box'] = box_dict
            final_dict['document_types'] = docs
            return Response(final_dict, status=200)

        except BoxArchiving.DoesNotExist:
            error_dict = {"detail": "Not found."}
            return Response(error_dict, status=404)


class SearchView(views.APIView):
    archival_relation_fields = [field.name for field in
                                BoxArchiving._meta.get_fields()]
    frequency_relation_fields = [field.name for field in
                                 FrequencyRelation._meta.get_fields()]
    frequency_sheet_fields = [field.name for field in
                              FrequencySheet._meta.get_fields()]
    administrative_process_fields = [field.name for field in
                                     AdministrativeProcess._meta.get_fields()]

    def get(self, request):
        query = request.query_params.get("filter")
        box_archiving = BoxArchiving.objects.all()
        frequency_sheet = FrequencySheet.objects.all()
        administrative_process = AdministrativeProcess.objects.all()
        frequency_relation = FrequencyRelation.objects.all()
        return_dict = {
            "box_archiving": [],
            "frequecy_relation": [],
            "frequency_sheet": [],
            "administrative_process": []
        }

        if query:
            filter_dict = json.loads(query)
            filter_dict_fk = {}

            if 'id' in list(filter_dict.keys())[0]:
                if 'abbreviation_id' in list(filter_dict.keys())[0]:
                    contains = 'abbreviation_id__name__icontains'
                else:
                    contains = '{}__number__icontains'.format(
                        list(filter_dict.keys())[0])
                filter_dict_fk = {
                    contains: list(filter_dict.values())[0]
                }

            if list(filter_dict.keys())[0] in self.archival_relation_fields:
                if not filter_dict_fk:
                    box_archiving = box_archiving.filter(**filter_dict)
                else:
                    box_archiving = box_archiving.filter(**filter_dict_fk)
                return_dict['box_archiving'] = BoxArchivingSerializer(
                    box_archiving, many=True).data

            if list(filter_dict.keys())[0] in self.frequency_relation_fields:
                if not filter_dict_fk:
                    frequency_relation = frequency_relation.filter(**filter_dict)
                else:
                    frequency_relation = frequency_relation.filter(**filter_dict_fk)
                return_dict['frequecy_relation'] = FrequencyRelationSerializer(
                    frequency_relation,
                    many=True).data

            if list(filter_dict.keys())[0] in self.frequency_sheet_fields:
                if not filter_dict_fk:
                    frequency_sheet = frequency_sheet.filter(**filter_dict)
                else:
                    frequency_sheet = frequency_sheet.filter(**filter_dict_fk)
                return_dict['frequency_sheet'] = FrequencySheetSerializer(
                    frequency_sheet,
                    many=True).data

            if list(filter_dict.keys())[0] in self.administrative_process_fields:
                if not filter_dict_fk:
                    administrative_process = administrative_process.filter(**filter_dict)
                else:
                    administrative_process = administrative_process.filter(**filter_dict_fk)
                return_dict['administrative_process'] = AdministrativeProcessSerializer(
                    administrative_process,
                    many=True).data

        return Response(return_dict, status=200)


class YearByAbbreviation(views.APIView):
    def get(self, request, abvt):
        queryset = BoxAbbreviations.objects.filter(
            abbreviation=abvt)
        if not queryset:
            return Response('Nao foi encontrado objeto com este valor', status=204)
        serializer = BoxAbbreviationsSerializer(queryset, many=True)
        return Response(serializer.data, status=200)


class NumberByYearAndAbbreviation(views.APIView):
    def get(self, request, abvt, year):
        queryset = BoxAbbreviations.objects.filter(
            abbreviation=abvt, year=year)
        if not queryset:
            return Response('Nao foi encontrado objeto com este valor', status=204)
        serializer = BoxAbbreviationsSerializer(queryset, many=True)
        return Response(serializer.data, status=200)
