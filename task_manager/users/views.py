from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth.models import User
from django.views.generic import (
    ListView, CreateView, UpdateView, DeleteView, TemplateView
)
from django.urls import reverse_lazy, reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

class UsersList(ListView):
    model = User
    template_name = 'users/users.html'

class CreateUser(SuccessMessageMixin, CreateView):
    form_class = CustomUserCreationForm
    template_name = 'users/create_user.html'
    success_url = reverse_lazy('login')
    success_message = "Пользователь успешно зарегистрирован."

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save()
        return response

class UserUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = User
    fields = ['first_name', 'last_name']  # Только эти поля будут доступны для редактирования
    template_name = 'users/update_user.html'
    success_url = reverse_lazy('user-list')

    def test_func(self):
        """ Проверяем, что пользователь пытается изменить свою учетную запись """
        obj = self.get_object()
        return obj == self.request.user or self.request.user.is_superuser

class UserDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = User
    template_name = 'users/delete_user.html'
    success_url = reverse_lazy('user-list')

    def test_func(self):
        """ Проверяем, что пользователь пытается удалить свою учетную запись """
        obj = self.get_object()
        return obj == self.request.user or self.request.user.is_superuser

