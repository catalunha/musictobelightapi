from django.contrib import admin
from medias.models.audio_model import Audio
from medias.models.image_model import Image


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
