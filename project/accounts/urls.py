from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from project.accounts.views.account_view import (
    AccountViewCreateConfirmCode,
    AccountViewCreateSendCode,
    AccountViewMe,
    AccountViewPasswordConfirmCode,
    AccountViewPasswordSendCode,
)
from project.accounts.views.profile_view import (
    ProfileViewDetail,
    ProfileViewGetByEmail,
    ProfileViewList,
    ProfileViewMe,
)

urlpatterns = [
    path(
        "accounts/token/",
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
        "accounts/create/sendcode/",
        AccountViewCreateSendCode.as_view(),
        name="user_create_sendcode",
    ),
    path(
        "accounts/create/confirmcode/",
        AccountViewCreateConfirmCode.as_view(),
        name="user_create_confirmcode",
    ),
    path(
        "accounts/me/",
        AccountViewMe.as_view(),
        name="user_me",
    ),
    path(
        "accounts/password/sendcode/",
        AccountViewPasswordSendCode.as_view(),
        name="user_resetpassword_sendcode",
    ),
    path(
        "accounts/password/confirmcode/",
        AccountViewPasswordConfirmCode.as_view(),
        name="user_resetpassword_confirmcode",
    ),
]

urlpatterns += [
    path(
        "accounts/profile/me/",
        ProfileViewMe.as_view(),
        name="profile_me",
    ),
    path(
        "accounts/profile/getbyemail/<str:email>/",
        ProfileViewGetByEmail.as_view(),
        name="profile_getbyemail",
    ),
    path(
        "accounts/profile/<str:id>/",
        ProfileViewDetail.as_view(),
        name="profile_detail",
    ),
    path(
        "accounts/profile/",
        ProfileViewList.as_view(),
        name="profile_list",
    ),
]
