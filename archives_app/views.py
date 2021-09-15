from rest_framework import viewsets
from .fields_serializers import BoxAbbreviationsSerializer, PublicWorkerSerializer
from .fields_serializers import (DocumentSubjectSerializer, DocumentTypeSerializer,
                                 UnitySerializer)
from .fields_serializers import FrontCoverSerializer, StatusSerializer, ShelfSerializer
from .fields_models import BoxAbbreviations, PublicWorker, DocumentSubject, DocumentType
from .fields_models import Unity, Shelf, FrontCover, Status
from .documents_models import (ArchivalRelation, FrequencyRelation, AdministrativeProcess,
                               OriginBox, FrequencySheet, ReferencePeriod)
from .documents_serializers import (FrequencySheetSerializer, OriginBoxSerializer,
                                    AdministrativeProcessSerializer,
                                    FrequencyRelationSerializer,
                                    ArchivalRelationSerializer,
                                    ReferencePeriodSerializer)


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


class PublicWorkerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = PublicWorker.objects.all()
    serializer_class = PublicWorkerSerializer


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


class ArchivalRelationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows archival relations document type
    to be viewed or edited.
    """
    queryset = ArchivalRelation.objects.all()
    serializer_class = ArchivalRelationSerializer


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


class OriginBoxViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows origin box subtype
    to be viewed or edited.
    """
    queryset = OriginBox.objects.all()
    serializer_class = OriginBoxSerializer


class FrequencySheetViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows frequency sheet document type
    to be viewed or edited.
    """
    queryset = FrequencySheet.objects.all()
    serializer_class = FrequencySheetSerializer


class ReferencePeriod(viewsets.ModelViewSet):
    """
    API endpoint that allows origin box subtype
    to be viewed or edited.
    """
    queryset = ReferencePeriod.objects.all()
    serializer_class = ReferencePeriodSerializer
