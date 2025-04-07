from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


# Create your models here.
class User(AbstractUser):
    def __str__(self):
        return self.get_full_name()

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

# from django.contrib.auth import get_user_model

# def get_full_name(self):
#     return f'{self.first_name} {self.last_name}'

# get_user_model().add_to_class('str', get_full_name)