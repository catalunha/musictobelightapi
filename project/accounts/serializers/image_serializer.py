from accounts.models.image_model import ImageModel
from accounts.serializers.profile_serializer import ProfileSerializer
from rest_framework import serializers


class ImageSerializerAll(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)

    class Meta:
        model = ImageModel
        fields = [
            "id",
            "image",
            "description",
            "extension",
            "size",
            "deleted",
            "profile",
        ]


class ImageSerializerImage(serializers.ModelSerializer):
    class Meta:
        model = ImageModel
        fields = [
            "image",
        ]
