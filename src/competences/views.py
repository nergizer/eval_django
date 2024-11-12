import datetime

from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.core.exceptions import BadRequest
from django.http import HttpResponseRedirect, HttpResponseBadRequest
from django.shortcuts import render
from django.urls import reverse

from competences.forms import CompetencesForm, ConfirmForm, RequeteForm
from competences.models import UserProfile, Requete


# Create your views here.


def index(request):
    if not request.user.is_authenticated:
        return render(request,"competences/index.html")
    usr = UserProfile.get_for_user(request.user)

    return render(request, "competences/index.html",
                  {
                      "requetes_self" : Requete.objects.filter(owner=usr),
                      "requetes_available": Requete.objects.exclude(owner=usr)
                  .filter(competence__in=usr.competences.all(),date__gt=datetime.datetime.now())

                  })


class LoginV(LoginView):
    template_name = "competences/login.html"
    next_page = "/competences/"


def profil(request):
    if not request.user.is_authenticated:
        raise PermissionError()

    return render(request,"competences/profil.html",{"competences" : UserProfile.get_for_user(request.user).competences.all(),"profil" : UserProfile.get_for_user(request.user)})


def accepter(request,req_id : int):
    if not request.user.is_authenticated:
        raise PermissionError()
    if request.method == "POST":
        form = ConfirmForm(request.POST)

        if form.is_valid():
            prof = UserProfile.get_for_user(request.user)
            req = Requete.objects.get(pk=req_id)
            if req.date >= datetime.datetime.now() and req.assigned is None and prof.competences.contains(req.competence):
                req.assigned = request.user
                return HttpResponseRedirect("/competences")

        raise BadRequest()
    else:
        form = ConfirmForm()
        return render(request,"competences/accepter.html", {"form" : form})

def requete(request):
    if not request.user.is_authenticated:
        raise PermissionError()
    if request.method == "POST":
        form = RequeteForm(request.POST)

        if form.is_valid():
            prof = UserProfile.get_for_user(request.user)
            Requete.objects.create(description=form.cleaned_data["description"],competence=form.cleaned_data["competence"],date=form.cleaned_data["date"],owner=prof)
            return HttpResponseRedirect("/competences")

        raise BadRequest()
    else:
        form = RequeteForm()
        return render(request,"competences/requete.html", {"form" : form})


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
