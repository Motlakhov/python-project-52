"""
URL configuration for task_manager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    
    # Маршрут для списка пользователей
    path('users/', include('users.urls')),

    # # Маршрут для создания пользователя
    # path('users/create/', views.CreateUser.as_view(), name='user-create'),
    
    # # Маршрут для редактирования пользователя
    # path('users/<int:pk>/update/', views.UserUpdate.as_view(), name='user-update'),
    
    # # Маршрут для удаления пользователя
    # path('users/<int:pk>/delete/', views.UserDelete.as_view(), name='user-delete'),

    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
]
