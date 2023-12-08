from accounts.models.profile_model import ProfileModel
from accounts.serializers.account_serializer import AccountSerializer
from accounts.serializers.image_serializer import ImageSerializerImage
from rest_framework import serializers


class ProfileSerializer(serializers.ModelSerializer):
    user = AccountSerializer(read_only=True)
    photo = ImageSerializerImage(read_only=True)

    class Meta:
        model = ProfileModel
        fields = [
            "id",
            "name",
            "description",
            "photo",
            "is_coordinator",
            "user",
        ]


class ProfileSerializerPatch(serializers.ModelSerializer):
    user = AccountSerializer(read_only=True)

    class Meta:
        model = ProfileModel
        fields = [
            "id",
            "name",
            "description",
            "photo",
            "is_coordinator",
            "user",
        ]


class ProfileSerializerList(serializers.ModelSerializer):
    user = AccountSerializer(read_only=True)
    photo = ImageSerializerImage(read_only=True)

    class Meta:
        model = ProfileModel
        fields = [
            "id",
            "name",
            "description",
            "photo",
            "is_coordinator",
            "user",
        ]
