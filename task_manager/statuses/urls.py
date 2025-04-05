from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

# app_name='users'

urlpatterns = [
    path('', views.StatusesListView.as_view(), name='statuses'),
    path('create/', views.StatusCreateView.as_view(), name='status_create'),
    path('<int:pk>/update/', views.StatusUpdateView.as_view(), name='status_update'),
    path('<int:pk>/delete/', views.StatusDeleteView.as_view(), name='status_delete'),

    # # Маршрут для создания пользователя
    # path('create/', views.UserCreateView.as_view(), name='user-create'),
    
    # # Маршрут для редактирования пользователя
    # path('<int:pk>/update/', views.UserUpdateView.as_view(), name='user-update'),
    
    # # Маршрут для удаления пользователя
    # path('<int:pk>/delete/', views.UserDeleteView.as_view(), name='user-delete'),

]