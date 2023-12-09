from accounts.serializers.profile_serializer import ProfileSerializerList
from medias.serializers.audio_serializer import AudioSerializerList
from medias.serializers.image_serializer import ImageSerializerList
from musics.serializers.album_serializer import AlbumSerializerList
from rest_framework.serializers import ModelSerializer

from project.musics.models.sound import Sound


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
