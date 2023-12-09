from accounts.models.profile_model import ProfileModel
from bases.models import BaseModel
from django.db import models
from medias.models.image_model import ImageModel


class AlbumModel(BaseModel):
    name = models.CharField(
        max_length=255,
    )
    description = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )
    coordinator = models.ForeignKey(
        ProfileModel,
        related_name="albums_coordinator",
        on_delete=models.CASCADE,
    )
    image = models.ForeignKey(
        ImageModel,
        related_name="algums",
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )
    listeners = models.ManyToManyField(
        ProfileModel,
        related_name="albums_listeners",
    )
