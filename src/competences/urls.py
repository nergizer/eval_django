from django.urls import path

from competences import views

urlpatterns = [
    path('',views.index),
    path('login', views.LoginV.as_view()),
    path('logout', views.logout_view)
]