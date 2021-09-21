from rest_framework import viewsets, views
from rest_framework.response import Response
from .fields_serializers import BoxAbbreviationsSerializer
from .fields_serializers import (DocumentSubjectSerializer, DocumentTypeSerializer,
                                 UnitySerializer)
from .fields_serializers import FrontCoverSerializer, StatusSerializer, ShelfSerializer
from .fields_models import BoxAbbreviations, DocumentSubject, DocumentType
from .fields_models import Unity, Shelf, FrontCover, Status
from .documents_models import (ArchivalRelation, FrequencyRelation, AdministrativeProcess,
                               OriginBox, FrequencySheet, OriginBoxSubject)
from .documents_serializers import (FrequencySheetSerializer,
                                    AdministrativeProcessSerializer,
                                    FrequencyRelationSerializer,
                                    ArchivalRelationSerializer)


class DocumentSubjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = DocumentSubject.objects.all()
    serializer_class = DocumentSubjectSerializer


class DocumentTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = DocumentType.objects.all()
    serializer_class = DocumentTypeSerializer


class UnityViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Unity.objects.all()
    serializer_class = UnitySerializer


class BoxAbbreviationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = BoxAbbreviations.objects.all()
    serializer_class = BoxAbbreviationsSerializer


class ShelfViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Shelf.objects.all()
    serializer_class = ShelfSerializer


class FrontCoverViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = FrontCover.objects.all()
    serializer_class = FrontCoverSerializer


class StatusViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Status.objects.all()
    serializer_class = StatusSerializer


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


class ArchivalRelationView(views.APIView):

    def get(self, request):
        queryset = ArchivalRelation.objects.all()
        serializer = ArchivalRelationSerializer(queryset, many=True)
        return Response(serializer.data, status=200)

    def post(self, request):
        box_list = request.data['box_list']
        boxes = list()

        for box_n in box_list:
            box = OriginBox.objects.create(number=box_n['number'], year=box_n['year'])
            for subject in box_n['subjects_list']:
                sub = OriginBoxSubject.objects.create(name=subject['name'],
                                                      dates=subject['dates'])
                box.subject.add(sub.id)
            boxes.append(box)

        sender_unity_id = Unity.objects.get(pk=request.data['sender_unity'])
        document_id = DocumentType.objects.get(pk=request.data['document_type_id'])

        archival_relation = ArchivalRelation.objects.create(
            process_number=request.data['process_number'],
            sender_unity=sender_unity_id,
            notes=request.data['notes'],
            number=request.data['number'],
            received_date=request.data['received_date'],
            number_of_boxes=request.data['number_of_boxes'],
            document_url=request.data['document_url'],
            cover_sheet=request.data['cover_sheet'],
            filer_user=request.data['filer_user'],
            document_type_id=document_id,
        )

        if request.data['abbreviation_id'] != '':
            box_abbreviation_id = BoxAbbreviations.objects.get(
                pk=request.data['abbreviation_id']
            )
            archival_relation.abbreviation_id = box_abbreviation_id
            archival_relation.save()

        if request.data['shelf_id'] != '':
            shelf_number_id = Shelf.objects.get(pk=request.data['shelf_id'])
            archival_relation.shelf_id = shelf_number_id
            archival_relation.save()

        for box in boxes:
            archival_relation.origin_box_id.add(box.id)

        return Response(status=201)


class ArchivalRelationDetailsView(views.APIView):

    def get(self, request, pk):
        queryset = ArchivalRelation.objects.get(pk=pk)
        serializer = ArchivalRelationSerializer(queryset)

        origin_box = serializer.data['origin_box_id']
        boxes = list()
        for box in origin_box:
            boxes_dict = {}
            box_n = OriginBox.objects.get(pk=box)
            boxes_dict['number'] = box_n.number
            boxes_dict['year'] = box_n.year
            boxes_dict['subjects_list'] = list()
            for subjects in box_n.subject.all():
                boxes_dict['subjects_list'].append({
                    'name': subjects.name,
                    'date': subjects.dates
                })
            boxes.append(boxes_dict)

        final_dict = serializer.data
        final_dict['origin_box'] = boxes
        return Response(final_dict, status=200)
