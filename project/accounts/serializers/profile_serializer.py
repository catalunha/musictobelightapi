from accounts.serializers.account_serializer import AccountSerializer
from accounts.serializers.image_serializer import ImageSerializerImage
from rest_framework import serializers

from project.accounts.models.profile import Profile


class ProfileSerializerDetail(serializers.ModelSerializer):
    user = AccountSerializer(read_only=True)
    photo = ImageSerializerImage(read_only=True)

    class Meta:
        model = Profile
        fields = [
            "id",
            "name",
            "description",
            "photo",
            "is_coordinator",
            "user",
        ]


class ProfileSerializerUpsert(serializers.ModelSerializer):
    user = AccountSerializer(read_only=True)

    class Meta:
        model = Profile
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
        model = Profile
        fields = [
            "id",
            "name",
            "photo",
        ]
