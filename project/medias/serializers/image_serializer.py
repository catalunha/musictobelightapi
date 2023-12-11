from rest_framework.serializers import ModelSerializer

# from project.accounts.serializers.profile_serializer import ProfileSerializerList
from project.medias.models.image import Image


class ImageSerializerList(ModelSerializer):
    class Meta:
        model = Image
        fields = [
            "image",
        ]


class ImageSerializerDetail(ModelSerializer):
    # profile = ProfileSerializerList(read_only=True)

    class Meta:
        model = Image
        fields = [
            "id",
            "image",
            "name",
            "extension",
            "size",
            "deleted",
            # "profile",
        ]
