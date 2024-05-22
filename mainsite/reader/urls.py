from django.urls import path
from . import views


urlpatterns = [
    path('<str:book>/<int:chapter>', views.read_page),
]