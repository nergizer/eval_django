from django import forms
from django.db.models import QuerySet

from competences.models import Competence
from eval_django.utils import try_or


class CompetencesForm(forms.Form):
    #bar = forms.CharField()
    #foo = forms.TypedMultipleChoiceField(choices=[(0,"A"),(1,"B")])
    comps = forms.ModelMultipleChoiceField(label="Compétences (ctr click pour en sélectionner plusieurs)",queryset=try_or(lambda: Competence.objects.all(),Competence.objects.none()))
