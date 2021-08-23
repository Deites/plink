from rest_framework import serializers
from bitbucketapi.models import RequestsList, Note
from djoser.serializers import UserSerializer, UserCreateSerializer
import re
from django.utils.translation import ugettext as _
from django.contrib.auth import get_user_model

User = get_user_model()


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = "__all__"


class RequestsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestsList
        fields = "__all__"


class GetUser(UserSerializer):
    class Meta:
        model = User
        fields = ("email", "username", "first_name", "last_name")


class PostUser(UserCreateSerializer):
    def validate(self, attrs):

        email_valid = attrs.get("email")
        first_name_valid = attrs.get("first_name")
        last_name_valid = attrs.get("last_name")

        if ("gmail.com" in email_valid) or ("icloud.com" in email_valid):
            msg = _("The email must not contain gmail.com or icloud.com.")
            raise serializers.ValidationError(msg)

        if not re.search(
            "^[a-zA-Z0-9_.-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email_valid
        ):
            msg = _("Email must not contain prohibited characters.")
            raise serializers.ValidationError(msg)

        if not re.search("^[a-zA-Z-]+$", first_name_valid):
            msg = _("First name must contain only letters and dashes.")
            raise serializers.ValidationError(msg)

        if not re.search("^[a-zA-Z-\s]+$", last_name_valid):
            msg = _("Last name must contain only letters, spaces and dashes.")
            raise serializers.ValidationError(msg)

        return super().validate(attrs)

    class Meta:
        model = User
        fields = ("email", "username", "password", "first_name", "last_name")
