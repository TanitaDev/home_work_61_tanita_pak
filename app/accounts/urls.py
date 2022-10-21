from django.contrib import admin
from django.urls import path

from accounts.views import LoginView
from webapp.views import *

urlpatterns = [
    path('login/', LoginView.as_view(), name='login')
]
