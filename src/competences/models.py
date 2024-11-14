from __future__ import annotations

from django.contrib.auth.models import User
from django.db import models
from django.db.models import Model, QuerySet


# Create your models here.

class Competence(Model):
    nom = models.CharField(max_length=256)

    def __str__(self):
        return self.nom

    class Meta:
        pass


class UserProfile(Model):
    user = models.ForeignKey(to=User, primary_key=True, on_delete=models.CASCADE)
    competences = models.ManyToManyField(to=Competence, default=[])

    def get_requetes(self, competences: set[Competence]) -> QuerySet[Requete]:
        return Requete.objects.filter(owner=self, competence__in=competences)

    @classmethod
    def get_for_user(cls, user: User) -> UserProfile:
        try:
            return cls.objects.get(pk=user.id)
        except UserProfile.DoesNotExist:
            return cls.objects.create(user=user)


class Requete(Model):
    description = models.CharField(max_length=256)
    date = models.DateField()
    competence = models.ForeignKey(to=Competence, on_delete=models.CASCADE)
    owner = models.ForeignKey(to=UserProfile, on_delete=models.CASCADE)
    assigned = models.ForeignKey(to=UserProfile, on_delete=models.CASCADE, related_name="assigned", blank=True,
                                 null=True)

    def __str__(self):
        return self.description + ": " + str(self.competence) + ", le " + str(self.date)
