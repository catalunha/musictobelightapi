from accounts.models.image_model import ImageModel
from bases.models import BaseModel
from django.conf import settings
from django.db import models


class ProfileModel(BaseModel):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        related_name="profiles",
        on_delete=models.PROTECT,
    )
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1255)
    is_coordinator = models.BooleanField(default=False)
    photo = models.ForeignKey(
        ImageModel,
        related_name="profiles",
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )
