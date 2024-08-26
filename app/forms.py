from . import models
from django import forms

class FamiliesForm(forms.ModelForm):

    class Meta:
        model = models.FamiliesModels
        fields = "__all__"

class PopulationsForm(forms.ModelForm):
    class Meta:
        model = models.PopulationsModels
        fields = "__all__"
