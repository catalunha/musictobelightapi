from rest_framework.serializers import ModelSerializer

from project.accounts.serializers.profile_serializer import ProfileSerializerList
from project.medias.serializers.image_serializer import ImageSerializerList
from project.musics.models.album import Album


class AlbumSerializerList(ModelSerializer):
    image = ImageSerializerList(read_only=True)
    coordinator = ProfileSerializerList(read_only=True)

    class Meta:
        model = Album
        fields = [
            "id",
            "name",
            "image",
            "coordinator",
        ]


class AlbumSerializerDetail(ModelSerializer):
    coordinator = ProfileSerializerList(read_only=True)
    listeners = ProfileSerializerList(read_only=True, many=True)
    image = ImageSerializerList(read_only=True)

    class Meta:
        model = Album
        fields = [
            "id",
            "name",
            "description",
            "image",
            "listeners",
            "coordinator",
        ]


class AlbumSerializerUpsert(ModelSerializer):
    class Meta:
        model = Album
        fields = [
            "id",
            "name",
            "description",
            "listeners",
            "coordinator",
        ]
