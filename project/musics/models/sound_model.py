from accounts.models.profile_model import ProfileModel
from bases.models import BaseModel
from django.db import models
from medias.models.audio_model import AudioModel
from medias.models.image_model import ImageModel
from musics.models.album_model import AlbumModel


class SoundModel(BaseModel):
    name = models.CharField(
        max_length=255,
    )
    description = models.CharField(
        max_length=1255,
        blank=True,
        null=True,
    )
    author = models.ForeignKey(
        ProfileModel,
        related_name="sounds",
        on_delete=models.PROTECT,
    )
    audio = models.ForeignKey(
        AudioModel,
        related_name="sounds",
        on_delete=models.PROTECT,
    )
    image = models.ForeignKey(
        ImageModel,
        related_name="sounds",
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )

    album = models.ForeignKey(
        AlbumModel,
        related_name="sounds",
        on_delete=models.PROTECT,
    )
