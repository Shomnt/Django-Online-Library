from django.contrib import admin
from django.urls import include, path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.catalog, name='catalog'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('user_page', views.user_page, name='user_page'),
    path('user-logout', views.user_logout, name="user-logout"),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
]
