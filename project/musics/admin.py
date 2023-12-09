from django.contrib import admin
from musics.models.album_model import AlbumModel
from musics.models.sound_model import SoundModel


@admin.register(AlbumModel)
class AlbumAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
    ]


@admin.register(SoundModel)
class SoundModel(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
    ]
