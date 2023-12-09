from accounts.serializers.profile_serializer import ProfileSerializerList
from medias.serializers.image_serializer import ImageSerializerList
from musics.models.album_model import AlbumModel
from rest_framework.serializers import ModelSerializer


class AlbumSerializerList(ModelSerializer):
    image = ImageSerializerList(read_only=True)
    coordinator = ProfileSerializerList(read_only=True)

    class Meta:
        model = AlbumModel
        fields = [
            "id",
            "name",
            "image",
            "coordinator",
        ]


class AlbumSerializerDetail(ModelSerializer):
    coordinator = ProfileSerializerList(read_only=True)
    listeners = ProfileSerializerList(read_only=True, many=True)

    class Meta:
        model = AlbumModel
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
        model = AlbumModel
        fields = [
            "id",
            "name",
            "description",
            "listeners",
            "coordinator",
        ]
