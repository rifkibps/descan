from typing import Any
from . import models
from django import forms
from pprint import pprint

class FamiliesForm(forms.ModelForm):

    class Meta:
        model = models.FamiliesModels
        fields = "__all__"

    def clean(self):

        form_data = self.cleaned_data
        
        # Validasi NIK
        if form_data['r115'].isnumeric() == False or len(form_data['r115']) != 16:
            self._errors['r115'] = self.error_class(['Format NIK harus berupa angka 16 digit.'])

        # Validasi r301a
        if form_data['r301a'] == '1':
            if(form_data.get('r301b') is None):
                self._errors['r301b'] = self.error_class(['Jika status kepemilikan bangunan adalah milik sendiri, maka bukti kepemilikan harus terisi.'])
        else:
            form_data['r301b'] = None
        
        # Validasi r306a
        if form_data['r306a'] in ['4', '5', '6', '7', '8']:
            if(form_data.get('r306b') is None):
                self._errors['r306b'] = self.error_class(['Jika sumber air minum utama adalah sumur bor/ sumur terlindung/ sumur tak terlindung/ mata air terlindung/ mata air tak terlindung, maka jarak sumber air minum utama ke tempat penampungan limbah harus terisi.'])
        else:
            form_data['r306b'] = None

        # Validasi r307a
        if form_data['r307a'] == '1':
            if(form_data.get('r307b') is None):
                self._errors['r307b'] = self.error_class(['Jika sumber penerangan utama adalah Listrik PLN dengan meteran, maka besaran daya harus terisi.'])
        else:
            form_data['r307b'] = None

        # Validasi r309a
        if form_data['r309a'] in ['1', '2', '3']:
            if(form_data.get('r309b') is None):
                self._errors['r309b'] = self.error_class(['Jika kepemilikan dan penggunaan fasilitas tempat buang air besar utama berkode 1, 2, atau 3, maka jenis kloset harus terisi.'])
        else:
            form_data['r309b'] = None
            form_data['r310'] = None

        if form_data['r504a'].isnumeric() and form_data['r504b'].isnumeric() and form_data['r504c'].isnumeric() and form_data['r504d'].isnumeric() and form_data['r504e'].isnumeric() :

            if form_data['r504a'] < 0 :
                self._errors['r504a'] = self.error_class(['Jumlah ternak sapi harus bernilai > 0'])
            
            if form_data['r504b'] < 0 :
                self._errors['r504b'] = self.error_class(['Jumlah ternak kerbau harus bernilai > 0'])

            if form_data['r504c'] < 0 :
                self._errors['r504c'] = self.error_class(['Jumlah ternak kuda harus bernilai > 0'])
            
            if form_data['r504d'] < 0 :
                self._errors['r504d'] = self.error_class(['Jumlah ternak babi harus bernilai > 0'])

            if form_data['r504e'] < 0 :
                self._errors['r504e'] = self.error_class(['Jumlah ternak kambing harus bernilai > 0'])

        return self.cleaned_data
    
    
        # self._errors['import_file'] = self.error_class(['Format template tidak sesuai. Silahkan gunakan template yang telah disediakan.'])
        # return self._errors['import_file']
        # return self.cleaned_data

class PopulationsForm(forms.ModelForm):
    class Meta:
        model = models.PopulationsModels
        fields = "__all__"
