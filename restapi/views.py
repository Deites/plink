from rest_framework import viewsets, permissions
from .serializer import RequestsSerializer, NoteSerializer
from bitbucketapi.models import Note, RequestsList
from django.contrib.auth import get_user_model

User = get_user_model()


class NoteViewsets(viewsets.ModelViewSet):
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Note.objects.filter(user_note=self.request.user).order_by("-id")


class RequestsViewsets(viewsets.ModelViewSet):
    serializer_class = RequestsSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        x_forwarded_for = self.request.META.get("HTTP_X_FORWARDED_FOR")
        if x_forwarded_for:
            current_ip = x_forwarded_for.split(",")[-1].strip()
        else:
            current_ip = self.request.META.get("REMOTE_ADDR")

        return RequestsList.objects.filter(ip_user=current_ip).order_by("-id")
