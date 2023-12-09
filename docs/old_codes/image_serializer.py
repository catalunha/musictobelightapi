# from rest_framework import serializers

# from docs.old_codes.image import Image
# from project.accounts.serializers.profile_serializer import ProfileSerializerDetail


# class ImageSerializerAll(serializers.ModelSerializer):
#     profile = ProfileSerializerDetail(read_only=True)

#     class Meta:
#         model = Image
#         fields = [
#             "id",
#             "image",
#             "name",
#             "extension",
#             "size",
#             "deleted",
#             "profile",
#         ]


# class ImageSerializerImage(serializers.ModelSerializer):
#     class Meta:
#         model = Image
#         fields = [
#             "image",
#         ]
