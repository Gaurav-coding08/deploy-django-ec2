from django.contrib import admin
from django.urls import path,include
from .views import hi_message,bye_message

urlpatterns = [
    path("hi/",hi_message),
    path("bye/",bye_message)
]