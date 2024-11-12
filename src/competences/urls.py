from django.urls import path

from competences import views
from eval_django.utils import spath

app_name = "competences"

urlpatterns = [
    path('',views.index),
    spath('login', views.LoginV.as_view()),
    spath('logout', views.logout_view),
    spath('competences', views.competences),
    spath('profil', views.profil)

]