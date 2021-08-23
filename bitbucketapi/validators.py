import re
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _


class PasswordMaxValidator(object):
    def validate(self, password, user=None):
        if len(password) > 16:
            raise ValidationError(
                _("Your password must be no more than 16 characters."),
                code="password_no_max",
            )

    def get_help_text(self):
        return _("Your password must be no more than 16 characters.")


class SymbolValidator(object):
    def validate(self, password, user=None):
        if not re.findall("^[A-Z][a-zA-Z0-9]+$", password):
            raise ValidationError(
                _(
                    "The password must not contain prohibited characters and must begin with an uppercase letter."
                ),
                code="password_no_symbol",
            )

    def get_help_text(self):
        return _(
            "The password must not contain prohibited characters and must begin with an uppercase letter."
        )
