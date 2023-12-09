from medias.models.audio_model import AudioModel
from rest_framework.serializers import ModelSerializer


class AudioSerializerList(ModelSerializer):
    class Meta:
        model = AudioModel
        fields = [
            "audio",
        ]


class AudioSerializerDetail(ModelSerializer):
    class Meta:
        model = AudioModel
        fields = [
            "id",
            "audio",
            "name",
        ]
