from rest_framework import serializers

from registry.models import DefaultMessage, Occasion, Registry


class DefaultMessageSerializer(serializers.ModelSerializer):
    """DefaultMessage model serializer"""

    class Meta:
        model = DefaultMessage
        fields = [
            "id",
            "title",
            "message",
        ]


class OccasionSerializer(serializers.ModelSerializer):
    """Occasion model serializer"""

    class Meta:
        model = Occasion
        fields = [
            "id",
            "title",
            "default_messages",
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
            "custom_link",
            "link",
            "show_who_has_sent_gifts",
            "dark_mode",
            "is_draft",
            "created_at",
            "updated_at",
        ]
        read_only_fields = [
            "link",
            "created_at",
            "updated_at",
        ]
    
    def to_representation(self, instance):
        """Add default_messages to serializer"""
        data = super(RegistrySerializer, self).to_representation(instance)
        default_messages = instance.occasion.default_messages.all()
        data["default_messages"] = [messages.message for messages in default_messages]
        return data
