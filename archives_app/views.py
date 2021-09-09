from rest_framework import viewsets
from rest_framework import permissions
from .fields_serializers import BoxAbbreviationsSerializer, PublicWorkerSerializer
from .fields_serializers import DocumentSubjectSerializer, DocumentTypeSerializer, UnitySerializer
from .fields_serializers import FrontCoverSerializer, StatusSerializer, ShelfSerializer
from .fields_models import BoxAbbreviations, PublicWorker, DocumentSubject, DocumentType
from .fields_models import Unity, Shelf, FrontCover, Status
from .documents_models import AdministrativeProcess, FrequencyDocument, FrequencyRelation
from .documents_models import ArchivingRelation
from .documents_serializers import AdministrativeProcessSerializer, FrequencyDocumentSerializer
from .documents_serializers import FrequencyRelationSerializer, ArchivingRelationSerializer


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


class AdministrativeProcessSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = AdministrativeProcess.objects.all()
    serializer_class = AdministrativeProcessSerializer
    permission_classes = [permissions.AllowAny]


class FrequencyDocumentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = FrequencyDocument.objects.all()
    serializer_class = FrequencyDocumentSerializer
    permission_classes = [permissions.AllowAny]


class FrequencyRelationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = FrequencyRelation.objects.all()
    serializer_class = FrequencyRelationSerializer
    permission_classes = [permissions.AllowAny]


class ArchivingRelationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = ArchivingRelation.objects.all()
    serializer_class = ArchivingRelationSerializer
    permission_classes = [permissions.AllowAny]
