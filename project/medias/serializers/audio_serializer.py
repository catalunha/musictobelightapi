from rest_framework.serializers import ModelSerializer

from project.medias.models.audio import Audio


class AudioSerializerList(ModelSerializer):
    class Meta:
        model = Audio
        fields = [
            "audio",
        ]


class AudioSerializerDetail(ModelSerializer):
    class Meta:
        model = Audio
        fields = [
            "id",
            "audio",
            "name",
        ]
