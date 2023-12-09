from django.contrib import admin
from medias.models.audio_model import AudioModel
from medias.models.image_model import ImageModel


@admin.register(ImageModel)
class ImageAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
    ]


@admin.register(AudioModel)
class AudioAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
    ]
