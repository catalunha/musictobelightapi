from bases.models import BaseModel
from django.db import models

from project.accounts.models.profile import Profile
from project.medias.models.image import Image


class Album(BaseModel):
    name = models.CharField(
        max_length=255,
    )
    description = models.CharField(
        max_length=255,
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
        related_name="algums",
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )
    listeners = models.ManyToManyField(
        Profile,
        related_name="albums_listeners",
    )
