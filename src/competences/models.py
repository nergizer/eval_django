from __future__ import annotations

from django.contrib.auth.models import User
from django.db import models
from django.db.models import Model, QuerySet


# Create your models here.

class Competence(Model):
    nom = models.CharField(max_length=256)


class UserProfile(Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    competences = models.ManyToManyField(to=Competence)

    def get_requetes(self,competences : set[Competence]) -> QuerySet[Requete]:
        return Requete.objects.filter(owner=self,competence__in=competences)


class Requete(Model):
    description = models.CharField(max_length=256)
    date = models.DateField()
    competence = models.ForeignKey(to=Competence,on_delete=models.CASCADE)
    owner = models.ForeignKey(to=UserProfile,on_delete=models.CASCADE)
    assigned = models.ForeignKey(to=UserProfile, on_delete=models.CASCADE,related_name="assigned", null=True)


