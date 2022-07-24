from django.contrib import admin
from django.urls import path
from .views import index
from .views import signup, login


urlpatterns = [
    path('', index, name = 'homepage'),
    path('signup', signup),
    path('login', login)
]
