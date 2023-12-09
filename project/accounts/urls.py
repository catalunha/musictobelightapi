from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from project.accounts.views.account_view import (
    AccountViewCreate,
    AccountViewMe,
    AccountViewNewPassword,
    AccountViewResetPassword,
)
from project.accounts.views.profile_view import (
    ProfileViewDetail,
    ProfileViewList,
    ProfileViewMe,
)

urlpatterns = [
    path(
        "accounts/token",
        TokenObtainPairView.as_view(),
        name="token_obtain_pair",
    ),
    path(
        "accounts/token/refresh/",
        TokenRefreshView.as_view(),
        name="token_refresh",
    ),
    path(
        "accounts/token/verify/",
        TokenVerifyView.as_view(),
        name="token_verify",
    ),
]

urlpatterns += [
    path(
        "accounts/create/",
        AccountViewCreate.as_view(),
        name="user_create",
    ),
    path(
        "accounts/me",
        AccountViewMe.as_view(),
        name="user_me",
    ),
    path(
        "accounts/password/reset/",
        AccountViewResetPassword.as_view(),
        name="user_resetpassword",
    ),
    path(
        "accounts/password/new/",
        AccountViewNewPassword.as_view(),
        name="user_newpassword",
    ),
]

urlpatterns += [
    path(
        "accounts/profile/",
        ProfileViewList.as_view(),
        name="profile_list",
    ),
    path(
        "accounts/profile/me/",
        ProfileViewMe.as_view(),
        name="profile_me",
    ),
    path(
        "accounts/profile/<str:id>/",
        ProfileViewDetail.as_view(),
        name="profile_detail",
    ),
]
