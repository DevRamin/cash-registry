from datetime import date

from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models


class Occasion(models.Model):
    """Registry categories"""

    title = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title


class DefaultMessage(models.Model):
    """Registry default message"""

    title = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title


class Registry(models.Model):
    """Registry model"""

    occasion = models.ForeignKey(Occasion, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    image = models.ImageField(default="default.jpg", upload_to="registry_images")
    addressed_to = models.CharField(max_length=100)
    event_date = models.DateField(default=date.today)
    message = models.TextField()
    default_messages = models.ManyToManyField(DefaultMessage, blank=True)
    custom_link = models.CharField(
        max_length=50,
        unique=True,
        validators=[
            RegexValidator(
                regex="^[A-Za-z0-9-_\.]+$",
                message="Invalid link. Not blank spaces or special characters.",
                code="invalid_link",
            ),
        ],
    )
    show_who_has_sent_gifts = models.BooleanField(default=True)
    dark_mode = models.BooleanField(default=False)
    is_draft = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def link(self):
        """Create a unique link for registry"""
        return "sendbirdie.com/r/" + self.custom_link

    class Meta:
        """Modify plural name"""

        verbose_name_plural = "registries"

    def __str__(self) -> str:
        return self.title
