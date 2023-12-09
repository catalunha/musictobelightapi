from django.contrib import admin

from project.accounts.models.image import Image


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "image",
        "name",
        "extension",
        "size",
        "deleted",
        "profile",
    ]
