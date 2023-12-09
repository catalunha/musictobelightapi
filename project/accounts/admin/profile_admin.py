from accounts.models.profile_model import ProfileModel
from django.contrib import admin


@admin.register(ProfileModel)
class ProfileAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "description",
        "is_coordinator",
    ]
    search_fields = ("name",)
