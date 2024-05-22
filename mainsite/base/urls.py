from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.catalog, name='catalog'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('user-logout', views.user_logout, name="user-logout"),
]
