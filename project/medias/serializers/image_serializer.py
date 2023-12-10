from rest_framework.serializers import ModelSerializer

from project.medias.models.image import Image


class ImageSerializerList(ModelSerializer):
    class Meta:
        model = Image
        fields = [
            "image",
        ]


class ImageSerializerDetail(ModelSerializer):
    class Meta:
        model = Image
        fields = [
            "id",
            "image",
        ]
