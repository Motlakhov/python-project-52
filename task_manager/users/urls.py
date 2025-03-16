from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

# app_name='users'

urlpatterns = [
    path('', views.UsersList.as_view(), name='user-list'),

    # Маршрут для создания пользователя
    path('create/', views.CreateUser.as_view(), name='user-create'),
    
    # Маршрут для редактирования пользователя
    path('<int:pk>/update/', views.UserUpdate.as_view(), name='user-update'),
    
    # Маршрут для удаления пользователя
    path('<int:pk>/delete/', views.UserDelete.as_view(), name='user-delete'),

]