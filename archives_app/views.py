from rest_framework import viewsets
from rest_framework import permissions
from .serializers import  BoxAbbreviationsSerializer, PublicWorkerSerializer
from .models import BoxAbbreviations, PublicWorker


class BoxAbbreviationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = BoxAbbreviations.objects.all()
    serializer_class = BoxAbbreviationsSerializer
    permission_classes = [permissions.AllowAny]

class PublicWorkerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = PublicWorker.objects.all()
    serializer_class = PublicWorkerSerializer
    permission_classes = [permissions.AllowAny]