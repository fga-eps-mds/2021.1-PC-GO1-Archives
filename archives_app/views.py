from rest_framework import viewsets
from rest_framework import permissions
from .serializers import  BoxAbbreviationsSerializer, PublicWorkerSerializer, DocumentSubjetcSerializer, DocumentTypeSerializer, UnitySerializer
from .serializers import ShelfESerializer, ShelfPSerializer, FrontCoverSerializer, StatusSerializer
from .models import BoxAbbreviations, PublicWorker, DocumentSubjetc, DocumentType, Unity, ShelfE, ShelfP, FrontCover, Status


class DocumentSubjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = DocumentSubjetc.objects.all()
    serializer_class = DocumentSubjetcSerializer
    permission_classes = [permissions.AllowAny]

class DocumentTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
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

class ShelfEViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = ShelfE.objects.all()
    serializer_class = ShelfESerializer
    permission_classes = [permissions.AllowAny]

class ShelfPViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = ShelfP.objects.all()
    serializer_class = ShelfPSerializer
    permission_classes = [permissions.AllowAny]

    #status

class FrontCoverViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = FrontCover.objects.all()
    serializer_class = FrontCoverSerializer
    permission_classes = [permissions.AllowAny]

class StatusViewSet(viewsets.ModelViewSet):

    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    permission_classes = [permissions.AllowAny]










