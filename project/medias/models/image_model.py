from datetime import datetime

from bases.models import BaseModel
from django.db import models

from project.accounts.models.profile import Profile


class Image(BaseModel):
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
    extension = models.CharField(
        max_length=25,
        blank=True,
        null=True,
    )
    size = models.PositiveIntegerField(
        blank=True,
        null=True,
    )
    deleted = models.BooleanField(default=False)
    profile = models.ForeignKey(
        Profile,
        related_name="imagesmedia",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    def __str__(self) -> str:
        return f"Image: {self.id}"
