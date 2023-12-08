from accounts.models.image_model import ImageModel
from accounts.models.profile_model import ProfileModel
from accounts.serializers.profile_serializer import (
    ProfileSerializer,
    ProfileSerializerList,
    ProfileSerializerPatch,
)
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class ProfileViewList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        print("ProfileViewList.get")
        print("request.data", request.data)

        profileModelList = ProfileModel.objects.all()
        profileSerializerList = ProfileSerializerList(
            profileModelList,
            many=True,
        )
        return Response(profileSerializerList.data)


class ProfileViewDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        print("ProfileViewDetail.get")
        print("request.data", request.data)
        print("id", id)

        profileModel = get_object_or_404(
            ProfileModel.objects.all(),
            id=id,
        )

        profileSerializer = ProfileSerializer(profileModel)

        return Response(profileSerializer.data)

    def patch(self, request, id):
        print("ProfileViewDetail.patch")
        print("request.data", request.data)
        print("id", id)

        profileModel = get_object_or_404(
            ProfileModel.objects.all(),
            id=id,
        )
        profileSerializerPatch = ProfileSerializerPatch(
            data=request.data,
            partial=True,
        )
        profileSerializerPatch.is_valid(raise_exception=True)

        profileModel.name = profileSerializerPatch.validated_data.get(
            "name",
            profileModel.name,
        )
        profileModel.description = profileSerializerPatch.validated_data.get(
            "description",
            profileModel.description,
        )
        photo = request.data.get("photo")
        if bool(photo):
            print("photo", photo)
            if profileModel.photo is not None:
                photoOld = profileModel.photo
                photoOld.deleted = True
                photoOld.save()
            photoNew = ImageModel.objects.create(
                image=photo,
                profile=profileModel,
            )
            profileModel.photo = photoNew

        profileModel.save()

        profileSerializer = ProfileSerializer(profileModel)

        return Response(profileSerializer.data)


class ProfileViewMe(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        print("ProfileViewMe.get")
        print("request.data", request.data)

        user = self.request.user
        profile = user.profiles
        profileSerializer = ProfileSerializer(profile)
        return Response(profileSerializer.data)
