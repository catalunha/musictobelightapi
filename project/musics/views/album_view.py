from django.db.models import Q
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from project.accounts.models.profile import Profile
from project.medias.models.image import Image
from project.musics.models.album import Album
from project.musics.serializers.album_serializer import (
    AlbumSerializerDetail,
    AlbumSerializerList,
    AlbumSerializerUpsert,
)


class AlbumViewList(APIView):
    permission_classes = [
        IsAuthenticated,
    ]

    def post(self, request):
        print("AlbumViewList.post")
        print("request.data", request.data)
        print("type request.data", type(request.data))
        if request.user.profile.is_coordinator is False:
            return Response(
                {"detail": "Você não tem permissão para criar albuns"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        albumSerializerUpsert = AlbumSerializerUpsert(
            data=request.data,
            partial=True,
        )
        albumSerializerUpsert.is_valid(
            raise_exception=True,
        )
        album = Album.objects.create(
            name=albumSerializerUpsert.validated_data.get("name"),
            description=albumSerializerUpsert.validated_data.get("description", None),
            coordinator=albumSerializerUpsert.validated_data.get(
                "coordinator", request.user.profile
            ),
        )
        image = request.data.get("image")
        if bool(image):
            print("image", image)
            imageNew = Image.objects.create(
                image=image,
                profile=request.user.profile,
            )
            album.image = imageNew
        listeners = request.POST.getlist("listeners", None)
        print("listeners", listeners)
        if bool(listeners):
            print("listeners", listeners)
            for listener in listeners:
                listenerNew = Profile.objects.get(id=listener)
                album.listeners.add(listenerNew)
        album.save()

        return Response({"id": album.id})

    def get(self, request):
        print("AlbumViewList.get")
        print("request.data", request.data)
        print("request.user", request.user)
        print("request.user.profile", request.user.profile)
        print("request.user.profile.id", request.user.profile.id)
        # albums = Album.objects.all()

        albums1 = Album.objects.filter(coordinator=request.user.profile.id)
        print("albums1: ", len(albums1))

        albums2 = Album.objects.filter(listeners=request.user.profile.id)
        print("albums2: ", len(albums2))

        albums3 = Album.objects.filter(
            coordinator=request.user.profile.id
        ) | Album.objects.filter(listeners=request.user.profile.id)
        print("albums3: ", len(albums3))

        albums = Album.objects.filter(
            Q(coordinator=request.user.profile.id)
            | Q(listeners=request.user.profile.id)
        ).distinct()
        print("albums: ", len(albums))

        albumSerializerList = AlbumSerializerList(
            albums,
            many=True,
        )
        return Response(albumSerializerList.data)


class AlbumViewDetail(APIView):
    permission_classes = [
        IsAuthenticated,
    ]

    def get(self, request, id):
        print("AlbumViewDetail.get")
        print("request.data", request.data)
        print("id", id)

        album = get_object_or_404(
            Album.objects.all(),
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
        if request.user.profile.is_coordinator is False:
            return Response(
                {"detail": "Você não tem permissão para editar albuns"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        album = get_object_or_404(
            Album.objects.all(),
            id=id,
        )
        print("album.coordinator", album.coordinator.id)
        print("request.user.profile", request.user.profile.id)
        if album.coordinator != request.user.profile:
            return Response(
                {"detail": "Você não tem permissão para editar este album"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        print("listeners: ", request.POST.getlist("listeners"))

        albumSerializerUpsert = AlbumSerializerUpsert(
            data=request.data,
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
            imageNew = Image.objects.create(
                image=image,
                profile=request.user.profile,
            )
            album.image = imageNew
        listeners = request.POST.getlist("listeners")
        if bool(listeners):
            print("listeners", listeners)
            album.listeners.clear()
            for listener in listeners:
                listenerNew = Profile.objects.get(id=listener)
                album.listeners.add(listenerNew)
        album.save()
        return Response()

    def delete(self, request, id):
        print("AlbumViewDetail.delete")
        print("request.data", request.data)
        print("id", id)
        print(
            "request.user.profile.is_coordinator", request.user.profile.is_coordinator
        )
        if request.user.profile.is_coordinator is False:
            return Response(
                {"detail": "Você não tem permissão para apagar albuns"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        album = get_object_or_404(
            Album.objects.all(),
            id=id,
        )
        if album.coordinator.id != request.user.profile.id:
            return Response(
                {"detail": "Você não tem permissão para apagar este album"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        album.delete()
        return Response()
