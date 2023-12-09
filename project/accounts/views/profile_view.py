from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from project.accounts.models.profile import Profile
from project.accounts.serializers.profile_serializer import (
    ProfileSerializerDetail,
    ProfileSerializerList,
    ProfileSerializerUpsert,
)
from project.medias.models.image import Image


class ProfileViewList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        print("ProfileViewList.get")
        print("request.data", request.data)

        profileList = Profile.objects.all()
        profileSerializerList = ProfileSerializerList(
            profileList,
            many=True,
        )
        return Response(profileSerializerList.data)


class ProfileViewDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        print("ProfileViewDetail.get")
        print("request.data", request.data)
        print("id", id)

        profile = get_object_or_404(
            Profile.objects.all(),
            id=id,
        )

        profileSerializer = ProfileSerializerDetail(profile)

        return Response(profileSerializer.data)

    def patch(self, request, id):
        print("ProfileViewDetail.patch")
        print("request.data", request.data)
        print("id", id)

        profile = get_object_or_404(
            Profile.objects.all(),
            id=id,
        )
        profileSerializerPatch = ProfileSerializerUpsert(
            data=request.data,
            partial=True,
        )
        profileSerializerPatch.is_valid(raise_exception=True)

        profile.name = profileSerializerPatch.validated_data.get(
            "name",
            profile.name,
        )
        profile.description = profileSerializerPatch.validated_data.get(
            "description",
            profile.description,
        )
        profile.is_coordinator = profileSerializerPatch.validated_data.get(
            "is_coordinator",
            profile.is_coordinator,
        )
        photo = request.data.get("photo")
        if bool(photo):
            print("photo", photo)
            if profile.photo is not None:
                photoOld = profile.photo
                photoOld.deleted = True
                photoOld.save()
            photoNew = Image.objects.create(
                image=photo,
                profile=profile,
            )
            profile.photo = photoNew

        profile.save()

        profileSerializer = ProfileSerializerDetail(profile)

        return Response(profileSerializer.data)


class ProfileViewMe(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        print("ProfileViewMe.get")
        print("request.data", request.data)

        user = self.request.user
        profile = user.profiles
        profileSerializer = ProfileSerializerDetail(profile)
        return Response(profileSerializer.data)
