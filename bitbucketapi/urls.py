from django.urls import path
from .views import RegistrationView, RequestsView, NoteView
from .decorators import save_request
from django.contrib.auth.views import LoginView, LogoutView

app_name = "bitbucketapi"
urlpatterns = [
    path("registration", save_request(RegistrationView.as_view()), name="registration"),
    path(
        "login",
        save_request(LoginView.as_view(template_name="bitbucketapi/login.html")),
        name="login",
    ),
    path("logout", save_request(LogoutView.as_view()), name="logout"),
    path("", save_request(RequestsView.as_view()), name="requests"),
    path("note", save_request(NoteView.as_view()), name="note"),
]
