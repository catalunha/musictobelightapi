from django.contrib import admin

from project.accounts.models.profile import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "description",
        "is_coordinator",
    ]
    search_fields = ("name",)
