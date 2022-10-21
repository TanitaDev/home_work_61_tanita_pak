from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect

from accounts.forms import LoginForm


class LoginView(TemplateView):
    template_name = "login.html"

