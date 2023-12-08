from datetime import datetime

from bases.models import BaseModel
from django.db import models


class ImageModel(BaseModel):
    def uploadTo(instance, fileName):
        fileNameExtension = fileName.split(".")[-1]
        now = datetime.now().strftime("%Y%m%d%M%S%f")
        return "medias/image/{0}/{1}/{2}".format(
            instance.id,
            now,
            fileNameExtension,
        )

    def save(self, *arg, **kwargs):
        self.size = self.image.size
        self.extension = self.image.name.split(".")[-1]
        super().save(*arg, **kwargs)

    image = models.ImageField(upload_to=uploadTo)

    name = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )
