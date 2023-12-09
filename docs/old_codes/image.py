# from datetime import datetime

# from django.db import models

# from project.bases.models import BaseModel


# class Image(BaseModel):
#     def uploadTo(instance, fileName):
#         fileNameExtension = fileName.split(".")[-1]
#         now = datetime.now().strftime("%Y$m%d%H%M%S%f")
#         return "accounts/image/{0}/{1}.{2}".format(
#             instance.id,
#             now,
#             fileNameExtension,
#         )

#     def save(self, *args, **kwargs):
#         self.size = self.image.size
#         name = self.image.name
#         self.extension = name.split(".")[-1]
#         super().save(*args, **kwargs)

#     image = models.ImageField(
#         upload_to=uploadTo,
#     )
#     name = models.CharField(
#         max_length=255,
#         blank=True,
#         null=True,
#     )
#     extension = models.CharField(
#         max_length=25,
#         blank=True,
#         null=True,
#     )
#     size = models.PositiveIntegerField(
#         blank=True,
#         null=True,
#     )
#     deleted = models.BooleanField(
#         blank=True,
#         null=True,
#     )
#     profile = models.ForeignKey(
#         "accounts.Profile",
#         related_name="images",
#         on_delete=models.SET_NULL,
#         null=True,
#     )

#     def __str__(self) -> str:
#         return f"{self.id}"
