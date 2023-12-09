from rest_framework.serializers import ModelSerializer

from project.accounts.serializers.profile_serializer import ProfileSerializerList
from project.medias.serializers.audio_serializer import AudioSerializerList
from project.medias.serializers.image_serializer import ImageSerializerList
from project.musics.models.sound import Sound
from project.musics.serializers.album_serializer import AlbumSerializerList


class SoundSerializerList(ModelSerializer):
    image = ImageSerializerList(read_only=True)
    author = ProfileSerializerList(read_only=True)

    class Meta:
        model = Sound
        fields = [
            "id",
            "name",
            "image",
            "author",
        ]


class SoundSerializerDetail(ModelSerializer):
    audio = AudioSerializerList(read_only=True)
    image = ImageSerializerList(read_only=True)
    author = ProfileSerializerList(read_only=True)
    album = AlbumSerializerList(read_only=True)

    class Meta:
        model = Sound
        fields = [
            "id",
            "name",
            "description",
            "audio",
            "image",
            "author",
            "album",
        ]


class SoundSerializerUpsert(ModelSerializer):
    class Meta:
        model = Sound
        fields = [
            "id",
            "name",
            "description",
            "author",
            "album",
        ]
