from django.db import models

from project.accounts.models.profile import Profile
from project.bases.models import BaseModel
from project.medias.models.image import Image


class Album(BaseModel):
    name = models.CharField(
        max_length=255,
    )
    description = models.TextField(
        max_length=1255,
        blank=True,
        null=True,
    )
    coordinator = models.ForeignKey(
        Profile,
        related_name="albums_coordinator",
        on_delete=models.CASCADE,
    )
    image = models.ForeignKey(
        Image,
        related_name="albums",
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )
    listeners = models.ManyToManyField(
        Profile,
        related_name="albums_listeners",
        blank=True,
    )

    def __str__(self) -> str:
        return f"{self.name}"
