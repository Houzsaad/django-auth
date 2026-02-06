#from turtle import update
from django.urls import path

from .views import user_list, memmber, profile, login_view, logout_view, register_view, ceo, add, delete, update

from django.contrib.auth import views as auth_views


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('register/', auth_views.LoginView.as_view(template_name='accounts/register.html'), name='register'),
    path('profile/', profile, name='profile'),
    path('user_list/', user_list, name='user_list'),
    path('memmber/', memmber, name='memmber'),
    path('ceo/', ceo, name='ceo'),
    path('add/', add, name='add'),
    path('delete/<int:pk>/', delete, name='delete'),
    path('update/<int:pk>/', update, name='update'),
]