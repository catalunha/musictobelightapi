from accounts.serializers.profile_serializer import ProfileSerializerDetail
from rest_framework import serializers

from project.accounts.models.image import Image


class ImageSerializerAll(serializers.ModelSerializer):
    profile = ProfileSerializerDetail(read_only=True)

    class Meta:
        model = Image
        fields = [
            "id",
            "image",
            "name",
            "extension",
            "size",
            "deleted",
            "profile",
        ]


class ImageSerializerImage(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = [
            "image",
        ]
