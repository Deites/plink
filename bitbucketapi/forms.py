from django.contrib.auth.forms import UserCreationForm
from django import forms
import re
from django.utils.translation import ugettext as _
from django.contrib.auth import get_user_model

User = get_user_model()


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=100, required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    class Meta:
        model = User
        fields = (
            "email",
            "username",
            "password1",
            "password2",
            "first_name",
            "last_name",
        )

    def clean(self):
        cleaned_data = super().clean()

        email_valid = cleaned_data.get("email")
        first_name_valid = cleaned_data.get("first_name")
        last_name_valid = cleaned_data.get("last_name")

        if ("gmail.com" in email_valid) or ("icloud.com" in email_valid):
            msg = _("The email must not contain gmail.com or icloud.com.")
            self.add_error("email", msg)

        if not re.search(
            "^[a-zA-Z0-9_.-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email_valid
        ):
            msg = _("Email must not contain prohibited characters.")
            self.add_error("email", msg)

        if not re.search("^[a-zA-Z-]+$", first_name_valid):
            msg = _("First name must contain only letters and dashes.")
            self.add_error("first_name", msg)

        if not re.search("^[a-zA-Z-\s]+$", last_name_valid):
            msg = _("Last name must contain only letters, spaces and dashes.")
            self.add_error("last_name", msg)
