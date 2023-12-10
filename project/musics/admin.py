from django.contrib import admin

from project.musics.models.album import Album
from project.musics.models.sound import Sound


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "coordinator",
    ]


@admin.register(Sound)
class Sound(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "author",
        "album",
    ]
