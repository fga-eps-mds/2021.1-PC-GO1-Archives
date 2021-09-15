from django.urls import include, path
from rest_framework import routers
from archives_app import views


router = routers.DefaultRouter()
router.register(r'box-abbreviation', views.BoxAbbreviationViewSet)
router.register(r'public-worker', views.PublicWorkerViewSet)
router.register(r'document-subject', views.DocumentSubjectViewSet)
router.register(r'document-type', views.DocumentTypeViewSet)
router.register(r'unity', views.UnityViewSet)
router.register(r'shelf', views.ShelfViewSet)
router.register(r'front-cover', views.FrontCoverViewSet)
router.register(r'status', views.StatusViewSet)
router.register(r'administrative-process', views.AdministrativeProcessViewSet)
router.register(r'frequency-relation', views.FrequencyRelationViewSet)
router.register(r'frequency-sheet', views.FrequencySheetViewSet)
router.register(r'archival-relation', views.ArchivalRelationViewSet)
router.register(r'origin-box', views.OriginBoxViewSet)
router.register(r'reference-period', views.ReferencePeriod)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
