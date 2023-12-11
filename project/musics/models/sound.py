from django.db import models

from project.accounts.models.profile import Profile
from project.bases.models import BaseModel
from project.medias.models.audio import Audio
from project.medias.models.image import Image
from project.musics.models.album import Album


class Sound(BaseModel):
    name = models.CharField(
        max_length=255,
    )
    description = models.TextField(
        max_length=1255,
        blank=True,
        null=True,
    )
    author = models.ForeignKey(
        Profile,
        related_name="sounds",
        on_delete=models.PROTECT,
    )
    audio = models.ForeignKey(
        Audio,
        related_name="sounds",
        on_delete=models.PROTECT,
    )
    image = models.ForeignKey(
        Image,
        related_name="sounds",
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )
    album = models.ForeignKey(
        Album,
        related_name="sounds",
        on_delete=models.PROTECT,
    )
