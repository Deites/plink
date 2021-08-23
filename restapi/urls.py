from .views import RequestsViewsets, NoteViewsets
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from bitbucketapi.decorators import save_request
from django.contrib.auth import get_user_model

User = get_user_model()

urlpatterns = [
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.jwt")),
    path(
        "notes/creation/",
        save_request(NoteViewsets.as_view({"post": "create"})),
        name="notecreate",
    ),
    path(
        "notes/",
        save_request(
            NoteViewsets.as_view(
                {
                    "get": "list",
                }
            )
        ),
        name="note",
    ),
    path(
        "requests/",
        save_request(
            RequestsViewsets.as_view(
                {
                    "get": "list",
                }
            )
        ),
        name="requests",
    ),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
