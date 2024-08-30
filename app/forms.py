from typing import Any
from . import models
from django import forms

class FamiliesForm(forms.ModelForm):

    class Meta:
        model = models.FamiliesModels
        fields = "__all__"

    def clean(self):
        pass
        # self._errors['import_file'] = self.error_class(['Format template tidak sesuai. Silahkan gunakan template yang telah disediakan.'])
        # return self._errors['import_file']
        # return self.cleaned_data

class PopulationsForm(forms.ModelForm):
    class Meta:
        model = models.PopulationsModels
        fields = "__all__"
