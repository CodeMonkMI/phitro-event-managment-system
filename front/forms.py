from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm
from users.mixin import StyledFormMixin


class CustomPasswordResetForm(StyledFormMixin, PasswordResetForm):
    pass


class CustomSetPasswordForm(StyledFormMixin, SetPasswordForm):
    pass
