from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import AuthUser


class UserCreationForm(UserCreationForm):

    class Meta:
        model = AuthUser
        fields = ('email',)


class UserChangeForm(UserChangeForm):

    class Meta:
        model = AuthUser
        fields = ('email',)
