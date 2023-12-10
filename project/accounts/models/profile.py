from django.conf import settings
from django.db import models

from project.bases.models import BaseModel
from project.medias.models.image import Image


class Profile(BaseModel):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        related_name="profile",
        on_delete=models.PROTECT,
    )
    name = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )
    description = models.CharField(
        max_length=1255,
        blank=True,
        null=True,
    )
    is_coordinator = models.BooleanField(default=False)
    photo = models.ForeignKey(
        Image,
        related_name="profiles",
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )

    def __str__(self) -> str:
        return f"{self.name}"
