from django import forms

from competences.models import Competence


class CompetencesForm(forms.Form):
    comps = forms.TypedMultipleChoiceField(choices=Competence.objects.all())