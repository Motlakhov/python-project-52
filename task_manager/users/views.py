from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic import (
    ListView, CreateView, UpdateView, DeleteView, TemplateView
)
from task_manager.mixins import (
    CustomLoginMixin,
    DeleteProtectionMixin,
    PermitModifyUserMixin,
)
from task_manager.views import (
    CustomCreateView,
    CustomDeleteView,
    CustomUpdateView,
)
from django.urls import reverse_lazy, reverse
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from .forms import RegisterUserForm, UpdateUserForm

LOGIN_URL = reverse_lazy('login')

class UsersList(ListView):
    model = User
    template_name = 'users/users.html'
    context_object_name = "users"

class UserCreateView(CustomCreateView):
    model = User
    form_class = RegisterUserForm
    success_url = reverse_lazy("login")
    success_message = _("User is successfully registered")
    extra_context = {
        "header": _("Registration"),
        "button_text": _("Sign up"),
    }


class UserUpdateView(
        CustomLoginMixin, PermitModifyUserMixin,
        CustomUpdateView):
    model = User
    form_class = UpdateUserForm
    success_url = reverse_lazy("users")
    success_message = _("User is successfully updated")
    extra_context = {
        "header": _("Update user"),
        "button_text": _("Update"),
    }

class UserDeleteView(
        CustomLoginMixin, PermitModifyUserMixin,
        DeleteProtectionMixin, CustomDeleteView):
    model = User
    success_url = reverse_lazy("users")
    success_message = _("User successfully deleted")
    protected_message = _("Cannot delete a user because it is in use")
    protected_url = reverse_lazy("users")
    extra_context = {
        "header": _("Delete user"),
        "button_text": _("Yes, delete"),
    }

