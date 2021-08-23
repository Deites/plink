from django.db import models
from jsonfield import JSONField
from django.contrib.auth import get_user_model

User = get_user_model()


class RequestsList(models.Model):
    ip_user = models.CharField(max_length=100, verbose_name="Ip")
    request_itself = models.CharField(max_length=100, verbose_name="Request")
    json = JSONField(default=None)

    def __str__(self):
        return str(self.ip_user)


class Note(models.Model):
    user_note = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    note = models.CharField(max_length=100, verbose_name="Note")

    def __str__(self):
        return str(self.note)
