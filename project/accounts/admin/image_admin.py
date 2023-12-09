from accounts.models.image_model import ImageModel
from django.contrib import admin


@admin.register(ImageModel)
class ImageAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "image",
        "name",
        "extension",
        "size",
        "deleted",
        "profile",
    ]
