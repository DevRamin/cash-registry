from django.urls import include, path
from rest_framework import routers

from . import views

app_name = "api_v1"

router = routers.DefaultRouter()
router.register("default-message", views.DefaultMessageViewSet, basename="default_message")
router.register("occasion", views.OccasionViewSet, basename="occasion")
router.register("registry", views.RegistryViewSet, basename="registry")

urlpatterns = [
    path("", include(router.urls), name="api"),
]
