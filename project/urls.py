from django.urls import include, path
from rest_framework import routers
from archives_app import views

router = routers.DefaultRouter()
router.register(r'box_abbreviation', views.BoxAbbreviationViewSet)
router.register(r'public_worker', views.PublicWorkerViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]