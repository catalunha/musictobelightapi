from django.contrib import admin

from project.medias.models.audio import Audio
from project.medias.models.image import Image


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
    ]


@admin.register(Audio)
class AudioAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
    ]
