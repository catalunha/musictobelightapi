from django.urls import path

from project.musics.views.album_view import AlbumViewDetail, AlbumViewList
from project.musics.views.sound_view import SoundViewDetail, SoundViewList

urlpatterns = [
    path(
        "musics/album/",
        AlbumViewList.as_view(),
        name="music_album_list",
    ),
    path(
        "musics/album/<str:id>/",
        AlbumViewDetail.as_view(),
        name="musics_album_detail",
    ),
]

urlpatterns += [
    path(
        "musics/sound/",
        SoundViewList.as_view(),
        name="music_sound_list",
    ),
    path(
        "musics/sound/<str:id>/",
        SoundViewDetail.as_view(),
        name="musics_sound_detail",
    ),
]
