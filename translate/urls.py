#[18/09/2022 - Adithya Shetty]  routes file

from django.urls import path
from . import views

urlpatterns = [
    path("", views.translate_text_api , name='translate_text'),
]
    