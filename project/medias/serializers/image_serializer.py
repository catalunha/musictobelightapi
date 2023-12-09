from medias.models.image_model import Image
from rest_framework.serializers import ModelSerializer


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
            "name",
        ]
