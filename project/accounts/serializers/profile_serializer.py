from rest_framework import serializers

from project.accounts.models.profile import Profile
from project.accounts.serializers.account_serializer import AccountSerializer
from project.medias.serializers.image_serializer import ImageSerializerList


class ProfileSerializerDetail(serializers.ModelSerializer):
    user = AccountSerializer(read_only=True)
    photo = ImageSerializerList(read_only=True)

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
            "is_coordinator",
            "user",
        ]


class ProfileSerializerList(serializers.ModelSerializer):
    photo = ImageSerializerList(read_only=True)
    user = AccountSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = [
            "id",
            "name",
            "photo",
            "user",
        ]
