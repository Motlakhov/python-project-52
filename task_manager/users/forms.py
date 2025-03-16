from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

class UserForm(UserCreationForm):
    """Users form class."""

    class Meta(object):
        """Meta class for user form."""

        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
        )
