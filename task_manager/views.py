from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import (
    ListView, CreateView, UpdateView, DeleteView, TemplateView
)
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView, LogoutView

def index(request):
    return render(request, 'index.html')

class UsersList(ListView):
    model = User
    template_name = 'users.html'

# Создание пользователя
class CreateUser(CreateView):
    form_class = UserCreationForm
    template_name = 'create_user.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        # Сначала создаем пользователя с использованием формы
        user = form.save()
        
        # Теперь сохраняем имя и фамилию
        user.first_name = self.request.POST.get('first_name')
        user.last_name = self.request.POST.get('last_name')
        user.save()
        
        return super().form_valid(form)

class UserUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = User
    fields = ['first_name', 'last_name']  # Только эти поля будут доступны для редактирования
    template_name = 'update_user.html'
    success_url = reverse_lazy('user-list')

    def test_func(self):
        """ Проверяем, что пользователь пытается изменить свою учетную запись """
        obj = self.get_object()
        return obj == self.request.user or self.request.user.is_superuser

class UserDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = User
    template_name = 'delete_user.html'
    success_url = reverse_lazy('user-list')

    def test_func(self):
        """ Проверяем, что пользователь пытается удалить свою учетную запись """
        obj = self.get_object()
        return obj == self.request.user or self.request.user.is_superuser


class CustomLoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True  # Перенаправление уже залогиненного пользователя на главную страницу

class CustomLogoutView(LogoutView):
    next_page = '/'  # После выхода перенаправляем на главную страницу