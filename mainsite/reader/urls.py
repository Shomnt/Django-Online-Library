from django.urls import path
from . import views

urlpatterns = [
    path('<str:book>/<int:page>', views.read_page),
]