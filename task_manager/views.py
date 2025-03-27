from django.contrib import messages
from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import (
    ListView, CreateView, UpdateView, DeleteView, TemplateView
)
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.utils.translation import gettext_lazy as _
from .mixins import ObjectContextMixin

def index(request):
    return render(request, 'index.html')


class CustomLoginView(LoginView):
    template_name = 'base_form.html'
    next_page = reverse_lazy("index")
    success_message = _('You are logged in')
    extra_context = {
        "header": _("Login"),
        "button_text": _("Log in"),
    }

class UserLogoutView(LogoutView):
    next_page = reverse_lazy("index")

    def dispatch(self, request, *args, **kwargs):
        messages.info(request, _("You have logged out"))
        return super().dispatch(request, *args, **kwargs)


class CustomCreateView(SuccessMessageMixin, CreateView):
    template_name = "base_form.html"

class CustomUpdateView(SuccessMessageMixin, UpdateView):
    template_name = "base_form.html"

class CustomDeleteView(
        ObjectContextMixin, SuccessMessageMixin, DeleteView):
    template_name = "delete_form.html"