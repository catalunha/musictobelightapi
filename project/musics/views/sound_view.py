from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from project.medias.models.audio import Audio
from project.medias.models.image import Image
from project.musics.models.sound import Sound
from project.musics.serializers.sound_serializer import (
    SoundSerializerDetail,
    SoundSerializerList,
    SoundSerializerUpsert,
)


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
        sound = Sound.objects.create(
            name=soundSerializerUpsert.validated_data.get("name"),
            description=soundSerializerUpsert.validated_data.get("description", None),
            author=request.user.profile,
        )
        image = request.data.get("image")
        if bool(image):
            print("image", image)
            imageNew = Image.objects.create(
                image=image,
                profile=request.user.profile,
            )
            sound.image = imageNew
        audio = request.data.get("audio")
        if bool(audio):
            print("audio", audio)
            audioNew = Audio.objects.create(
                audio=audio,
                profile=request.user.profile,
            )
            sound.audio = audioNew

        sound.save()

        Response({"id": sound.id})

    def get(self, request, id):
        print("SoundByAlbumViewList.get")
        print("request.data", request.data)
        albumId = request.GET.get("album", None)
        if albumId is None:
            sounds = Sound.objects.all()
        else:
            sounds = get_list_or_404(
                Sound.objects.all(),
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
            Sound.objects.all(),
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
            Sound.objects.all(),
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
            imageNew = Image.objects.create(
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
            audioNew = Audio.objects.create(
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
            Sound.objects.all(),
            id=id,
        )
        sound.delete()
        return Response()
