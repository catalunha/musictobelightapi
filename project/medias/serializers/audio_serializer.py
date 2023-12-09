from medias.models.audio_model import Audio
from rest_framework.serializers import ModelSerializer


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
