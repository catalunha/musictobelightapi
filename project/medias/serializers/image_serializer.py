from medias.models.image_model import ImageModel
from rest_framework.serializers import ModelSerializer


class ImageSerializerList(ModelSerializer):
    class Meta:
        model = ImageModel
        fields = [
            "image",
        ]


class ImageSerializerDetail(ModelSerializer):
    class Meta:
        model = ImageModel
        fields = [
            "id",
            "image",
            "name",
        ]
