from django import forms
from django.db.models import QuerySet

from competences.models import Competence, Requete
from eval_django.utils import try_or


# Pas de models forms car propriété owner requise (?)
class RequeteForm(forms.Form):
    description = forms.CharField()
    date = forms.DateField(widget=forms.SelectDateWidget())
    competence = forms.ModelChoiceField(label="Compétence :",
                                        queryset=try_or(lambda: Competence.objects.all(), Competence.objects.none()),
                                        widget=forms.Select(attrs={"class": "form"}))


class ConfirmForm(forms.Form):
    pass


class CompetencesForm(forms.Form):
    #bar = forms.CharField()
    #foo = forms.TypedMultipleChoiceField(choices=[(0,"A"),(1,"B")])
    comps = forms.ModelMultipleChoiceField(label="Compétences (ctr click pour en sélectionner plusieurs)",
                                           queryset=try_or(lambda: Competence.objects.all(), Competence.objects.none()),
                                           widget=forms.SelectMultiple(attrs={"class": ""}))
