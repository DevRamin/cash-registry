from django.contrib import admin
from registry.models import DefaultMessage, Occasion, Registry


@admin.register(DefaultMessage)
class DefaultMessageAdmin(admin.ModelAdmin):
    """Registering the DefaultMessage model in the admin panel."""

    list_display = [
        "title",
        "created_at",
        "updated_at",
    ]
    search_fields = [
        "title",
        "message",
    ]


@admin.register(Occasion)
class OccasionAdmin(admin.ModelAdmin):
    """Registering the Occasion model in the admin panel."""

    list_display = [
        "title",
        "created_at",
        "updated_at",
    ]
    search_fields = [
        "title",
    ]


@admin.register(Registry)
class RegistryAdmin(admin.ModelAdmin):
    """Registering the Registry model in the admin panel."""

    list_display = [
        "title",
        "user",
        "occasion",
        "event_date",
        "show_who_has_sent_gifts",
        "dark_mode",
        "is_draft",
    ]
    search_fields = [
        "title",
        "message",
    ]
    list_filter = [
        "show_who_has_sent_gifts",
        "dark_mode",
        "is_draft",
    ]
