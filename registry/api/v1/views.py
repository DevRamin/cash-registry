from rest_framework.viewsets import ModelViewSet
from registry.api.v1.serializers import (DefaultMessageSerializer,
                                         OccasionSerializer,
                                         RegistrySerializer)
from registry.models import DefaultMessage, Occasion, Registry


class DefaultMessageViewSet(ModelViewSet):
    """DefaultMessage ViewSet"""

    serializer_class = DefaultMessageSerializer

    def get_queryset(self):
        return DefaultMessage.objects.all()


class OccasionViewSet(ModelViewSet):
    """Occasion ViewSet"""

    serializer_class = OccasionSerializer

    def get_queryset(self):
        return Occasion.objects.all()


class RegistryViewSet(ModelViewSet):
    """Registry ViewSet"""

    serializer_class = RegistrySerializer

    def get_queryset(self):
        return Registry.objects.all()
