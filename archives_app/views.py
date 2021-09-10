from rest_framework import viewsets
from rest_framework import permissions
from .fields_serializers import BoxAbbreviationsSerializer, PublicWorkerSerializer
from .fields_serializers import (DocumentSubjectSerializer, DocumentTypeSerializer,
                                 UnitySerializer)
from .fields_serializers import FrontCoverSerializer, StatusSerializer, ShelfSerializer
from .fields_models import BoxAbbreviations, PublicWorker, DocumentSubject, DocumentType
from .fields_models import Unity, Shelf, FrontCover, Status
from .documents_models import (ArchivalRelation, FrequencyRelation, AdministrativeProcess,
                               OriginBox, FrequencySheet)
from .documents_serializers import (FrequencySheetSerializer, OriginBoxSerializer,
                                    AdministrativeProcessSerializer,
                                    FrequencyRelationSerializer,
                                    ArchivalRelationSerializer)


class DocumentSubjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = DocumentSubject.objects.all()
    serializer_class = DocumentSubjectSerializer
    permission_classes = [permissions.AllowAny]


class DocumentTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = DocumentType.objects.all()
    serializer_class = DocumentTypeSerializer
    permission_classes = [permissions.AllowAny]


class PublicWorkerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = PublicWorker.objects.all()
    serializer_class = PublicWorkerSerializer
    permission_classes = [permissions.AllowAny]


class UnityViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Unity.objects.all()
    serializer_class = UnitySerializer
    permission_classes = [permissions.AllowAny]


class BoxAbbreviationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = BoxAbbreviations.objects.all()
    serializer_class = BoxAbbreviationsSerializer
    permission_classes = [permissions.AllowAny]


class ShelfViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Shelf.objects.all()
    serializer_class = ShelfSerializer
    permission_classes = [permissions.AllowAny]


class FrontCoverViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = FrontCover.objects.all()
    serializer_class = FrontCoverSerializer
    permission_classes = [permissions.AllowAny]


class StatusViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    permission_classes = [permissions.AllowAny]


class ArchivalRelationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows archival relations document type
    to be viewed or edited.
    """
    queryset = ArchivalRelation.objects.all()
    serializer_class = ArchivalRelationSerializer
    permission_classes = [permissions.AllowAny]


class FrequencyRelationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows frequency relations document type
    to be viewed or edited.
    """
    queryset = FrequencyRelation.objects.all()
    serializer_class = FrequencyRelationSerializer
    permission_classes = [permissions.AllowAny]


class AdministrativeProcessViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows administrative process document type
    to be viewed or edited.
    """
    queryset = AdministrativeProcess.objects.all()
    serializer_class = AdministrativeProcessSerializer
    permission_classes = [permissions.AllowAny]


class OriginBoxViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows origin box subtype
    to be viewed or edited.
    """
    queryset = OriginBox.objects.all()
    serializer_class = OriginBoxSerializer
    permission_classes = [permissions.AllowAny]


class FrequencySheetViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows frequency sheet document type
    to be viewed or edited.
    """
    queryset = FrequencySheet.objects.all()
    serializer_class = FrequencySheetSerializer
    permission_classes = [permissions.AllowAny]
