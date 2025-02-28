from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth.models import User
from django.views.generic import (
    ListView, CreateView, UpdateView, DeleteView, TemplateView
)
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView, LogoutView

class UsersList(ListView):
    model = User
    template_name = 'users/users.html'

class CreateUser(CreateView):
    form_class = CustomUserCreationForm  # Используем кастомную форму
    template_name = 'users/create_user.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        # Форма уже сохраняет first_name и last_name благодаря методу save в CustomUserCreationForm
        return super().form_valid(form)

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

