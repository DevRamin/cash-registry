from rest_framework import serializers

from registry.models import DefaultMessage, Occasion, Registry


class DefaultMessageSerializer(serializers.ModelSerializer):
    """DefaultMessage model serializer"""

    class Meta:
        model = DefaultMessage
        fields = [
            "title",
            "message",
        ]


class OccasionSerializer(serializers.ModelSerializer):
    """Occasion model serializer"""

    class Meta:
        model = Occasion
        fields = [
            "title",
        ]


class RegistrySerializer(serializers.ModelSerializer):
    """Registry model serializer"""

    link = serializers.URLField(read_only=True)

    class Meta:
        model = Registry
        fields = [
            "id",
            "occasion",
            "user",
            "title",
            "image",
            "addressed_to",
            "event_date",
            "message",
            "default_messages",
            "custom_link",
            "link",
            "show_who_has_sent_gifts",
            "dark_mode",
            "is_draft",
            "created_at",
            "updated_at",
        ]
        read_only_fields = [
            "id",
            "default_messages",
            "link",
            "created_at",
            "updated_at",
        ]
