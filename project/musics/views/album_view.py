from accounts.models.profile_model import ProfileModel
from django.db.models import Q
from django.shortcuts import get_list_or_404, get_object_or_404
from medias.models.image_model import ImageModel
from musics.models.album_model import AlbumModel
from musics.serializers.album_serializer import (
    AlbumSerializerDetail,
    AlbumSerializerList,
    AlbumSerializerUpsert,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class AlbumViewList(APIView):
    permission_classes = [
        IsAuthenticated,
    ]

    def post(self, request):
        print("AlbumViewList.post")
        print("request.data", request.data)
        albumSerializerUpsert = AlbumSerializerUpsert(
            data=request,
            partial=True,
        )
        albumSerializerUpsert.is_valid(
            raise_exception=True,
        )
        albumModel = AlbumModel.objects.create(
            name=albumSerializerUpsert.validated_data.get("name"),
            description=albumSerializerUpsert.validated_data.get("description", None),
            coordinator=request.user.profile,
        )
        image = request.data.get("image")
        if bool(image):
            print("image", image)
            imageNew = ImageModel.objects.create(
                image=image,
                profile=request.user.profile,
            )
            albumModel.image = imageNew
        listeners = request.data.getlist("listeners")
        if bool(listeners):
            print("listeners", listeners)
            for listener in listeners:
                listenerNew = ProfileModel.objects.get(id=listener)
                albumModel.listeners.add(listenerNew)
        albumModel.save()

        Response({"id": albumModel.id})

    def get(self, request):
        print("AlbumViewList.get")
        print("request.data", request.data)
        albums = get_list_or_404(
            AlbumModel.objects.all(),
            Q(coordinator=request.user.profile) | Q(listeners=request.user.profile),
        )
        albumSerializerList = AlbumSerializerList(
            albums,
            many=True,
        )
        Response(albumSerializerList.data)


class AlbumViewDetail(APIView):
    permission_classes = [
        IsAuthenticated,
    ]

    def get(self, request, id):
        print("AlbumViewDetail.get")
        print("request.data", request.data)
        print("id", id)

        album = get_object_or_404(
            AlbumModel.objects.all(),
            id=id,
        )
        albumSerializerDetail = AlbumSerializerDetail(
            album,
        )
        return Response(albumSerializerDetail.data)

    def patch(self, request, id):
        print("AlbumViewDetail.post")
        print("request.data", request.data)
        print("id", id)

        album = get_object_or_404(
            AlbumModel.objects.all(),
            id=id,
        )
        albumSerializerUpsert = AlbumSerializerUpsert(
            data=request,
            partial=True,
        )
        albumSerializerUpsert.is_valid(
            raise_exception=True,
        )
        album.name = albumSerializerUpsert.validated_data.get(
            "name",
            album.name,
        )
        album.description = albumSerializerUpsert.validated_data.get(
            "description",
            album.description,
        )
        album.coordinator = albumSerializerUpsert.validated_data.get(
            "coordinator",
            album.coordinator,
        )
        image = request.data.get("image")
        if bool(image):
            print("image", image)
            if album.image is not None:
                imageOld = album.image
                imageOld.deleted = True
                imageOld.save()
            imageNew = ImageModel.objects.create(
                image=image,
                profile=request.user.profile,
            )
            album.image = imageNew
        listeners = request.data.getlist("listeners")
        if bool(listeners):
            print("listeners", listeners)
            album.listeners.clear()
            for listener in listeners:
                listenerNew = ProfileModel.objects.get(id=listener)
                album.listeners.add(listenerNew)
        album.save()
        return Response()

    def delete(self, request, id):
        print("AlbumViewDetail.delete")
        print("request.data", request.data)
        print("id", id)
        album = get_object_or_404(
            AlbumModel.objects.all(),
            id=id,
        )
        album.delete()
        return Response()