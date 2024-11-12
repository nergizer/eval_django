from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.core.exceptions import BadRequest
from django.http import HttpResponseRedirect, HttpResponseBadRequest
from django.shortcuts import render
from django.urls import reverse

from competences.forms import CompetencesForm
from competences.models import UserProfile


# Create your views here.


def index(request):
    return render(request,"competences/index.html")


class LoginV(LoginView):
    template_name = "competences/login.html"
    next_page = "/competences/"


def profil(request):
    if not request.user.is_authenticated:
        raise PermissionError()

    return render(request,"competences/profil.html",{"competences" : UserProfile.get_for_user(request.user).competences.all(),"profil" : UserProfile.get_for_user(request.user)})


def competences(request):
    if not request.user.is_authenticated:
        raise PermissionError()
    if request.method == "POST":
        form = CompetencesForm(request.POST)


        if form.is_valid():
            UserProfile.get_for_user(request.user).competences.set(form.cleaned_data["comps"])
            return HttpResponseRedirect("/competences")

        raise BadRequest()

    else:
        form = CompetencesForm()
        return render(request,"competences/competences.html",{"form" : form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("competences:index"))
