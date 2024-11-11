from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


# Create your views here.


def index(request):
    return render(request,"competences/index.html")


class LoginV(LoginView):
    template_name = "competences/login.html"
    next_page = "/competences/"

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("competences:index"))
