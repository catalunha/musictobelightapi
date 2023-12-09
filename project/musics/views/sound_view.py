from django.shortcuts import get_list_or_404, get_object_or_404
from medias.models.audio_model import AudioModel
from medias.models.image_model import ImageModel
from musics.models.sound_model import SoundModel
from musics.serializers.sound_serializer import (
    SoundSerializerDetail,
    SoundSerializerList,
    SoundSerializerUpsert,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class SoundViewList(APIView):
    permission_classes = [
        IsAuthenticated,
    ]

    def post(self, request):
        print("SoundViewList.post")
        print("request.data", request.data)
        soundSerializerUpsert = SoundSerializerUpsert(
            data=request,
            partial=True,
        )
        soundSerializerUpsert.is_valid(
            raise_exception=True,
        )
        soundModel = SoundModel.objects.create(
            name=soundSerializerUpsert.validated_data.get("name"),
            description=soundSerializerUpsert.validated_data.get("description", None),
            author=request.user.profile,
        )
        image = request.data.get("image")
        if bool(image):
            print("image", image)
            imageNew = ImageModel.objects.create(
                image=image,
                profile=request.user.profile,
            )
            soundModel.image = imageNew
        audio = request.data.get("audio")
        if bool(audio):
            print("audio", audio)
            audioNew = AudioModel.objects.create(
                audio=audio,
                profile=request.user.profile,
            )
            soundModel.audio = audioNew

        soundModel.save()

        Response({"id": soundModel.id})

    def get(self, request, id):
        print("SoundByAlbumViewList.get")
        print("request.data", request.data)
        albumId = request.GET.get("album", None)
        if albumId is None:
            sounds = SoundModel.objects.all()
        else:
            sounds = get_list_or_404(
                SoundModel.objects.all(),
                album=albumId,
            )
        soundSerializerList = SoundSerializerList(
            sounds,
            many=True,
        )
        Response(soundSerializerList.data)


class SoundViewDetail(APIView):
    permission_classes = [
        IsAuthenticated,
    ]

    def get(self, request, id):
        print("SoundViewDetail.get")
        print("request.data", request.data)
        print("id", id)

        sound = get_object_or_404(
            SoundModel.objects.all(),
            id=id,
        )
        soundSerializerDetail = SoundSerializerDetail(
            sound,
        )
        return Response(soundSerializerDetail.data)

    def patch(self, request, id):
        print("SoundViewDetail.post")
        print("request.data", request.data)
        print("id", id)

        sound = get_object_or_404(
            SoundModel.objects.all(),
            id=id,
        )
        soundSerializerUpsert = SoundSerializerUpsert(
            data=request,
            partial=True,
        )
        soundSerializerUpsert.is_valid(
            raise_exception=True,
        )
        sound.name = soundSerializerUpsert.validated_data.get(
            "name",
            sound.name,
        )
        sound.description = soundSerializerUpsert.validated_data.get(
            "description",
            sound.description,
        )
        sound.album = soundSerializerUpsert.validated_data.get(
            "album",
            sound.album,
        )
        sound.author = soundSerializerUpsert.validated_data.get(
            "author",
            sound.author,
        )
        image = request.data.get("image")
        if bool(image):
            print("image", image)
            if sound.image is not None:
                imageOld = sound.image
                imageOld.deleted = True
                imageOld.save()
            imageNew = ImageModel.objects.create(
                image=image,
                profile=request.user.profile,
            )
            sound.image = imageNew
        audio = request.data.get("audio")
        if bool(audio):
            print("audio", audio)
            if sound.audio is not None:
                audioOld = sound.audio
                audioOld.deleted = True
                audioOld.save()
            audioNew = AudioModel.objects.create(
                audio=audio,
                profile=request.user.profile,
            )
            sound.audio = audioNew

        sound.save()
        return Response()

    def delete(self, request, id):
        print("SoundViewDetail.delete")
        print("request.data", request.data)
        print("id", id)
        sound = get_object_or_404(
            SoundModel.objects.all(),
            id=id,
        )
        sound.delete()
        return Response()
