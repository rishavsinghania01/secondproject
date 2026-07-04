from django.urls import path  # type: ignore
from .views import *

urlpatterns = [
    path("getBooks/", getBooks),
    path("setBook/", setBook),
]
