from typing import Any
from . import models
from django import forms
from pprint import pprint
from datetime import date
from . import helpers


class FamiliesForm(forms.ModelForm):

    class Meta:
        model = models.FamiliesModels
        fields = "__all__"

    def clean(self):

        form_data = self.cleaned_data 
        list_fields_val = [
            'r112',
            'r115',
            'r301a',
            'r301b',
            'r302',
            'r306a',
            'r306b',
            'r307a',
            'r307b',        
            'r309a',
            'r309b',
            'r310',
            'r501d',
            'r504a',
            'r504b',
            'r504c',
            'r504d',
            'r504e',
            'r502n',
            'r505'
        ]
        for field in list_fields_val:
            if field not in form_data.keys():
                return form_data
            
        form_data['r112'] = int(form_data['r112'])
        
        # Validasi NIK
        if form_data['r115'].isnumeric() == False or len(form_data['r115']) != 16:
            self._errors['r115'] = self.error_class(['Format Nomor kartu Keluarga harus berupa angka 16 digit.'])

        # Validasi r301a
        if form_data['r301a'] == '1':
            if(form_data.get('r301b') is None):
                self._errors['r301b'] = self.error_class(['Jika status kepemilikan bangunan adalah milik sendiri, maka bukti kepemilikan harus terisi.'])
        else:
            form_data['r301b'] = None
        
        if form_data['r302'] <= 0 :
            self._errors['r302'] = self.error_class(['Luas lantai bangunan harus lebih dari 0'])

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

        #Validasi Status Penerimaan Bantuan
        if form_data.get('r307b') == '1':
            if form_data.get('r501d') != '1':
                self._errors['r501d'] = self.error_class(['Jika daya listrik sebesar 450 Watt, maka status penerimaan Program Subsidi Listrik harus terisi "Ya"'])

        # Validasi Hewan Ternak

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

        if form_data['r502n'] == '1' and form_data['r505'] == '0':
            self._errors['r505'] = self.error_class(['Keluarga memiliki Smartphone, tetapi tidak menggunakan akses internet.'])

        if form_data['r505'] == '3' and form_data['r502n'] == '2' :
            self._errors['r505'] = self.error_class(['Keluarga tidak memiliki Smartphone, tetapi menggunakan akses internet handphone.'])

        self.cleaned_data = form_data
        return self.cleaned_data

class PopulationsForm(forms.ModelForm):
    class Meta:
        model = models.PopulationsModels
        fields = "__all__"

    def clean(self):
        form_data = self.cleaned_data
   
        list_fields_val = [
            'r401',
            'r403',
            'r404',
        ]
        
        for field in list_fields_val:
            if field not in form_data.keys():
                return form_data
            
        form_data['r401'] = int(form_data['r401'])
        # Validasi NIK

        if form_data['r403'].isnumeric() == False or len(form_data['r403']) != 16:
            self._errors['r403'] = self.error_class(['Format NIK harus berupa angka 16 digit.'])

        if form_data['r404'] not in ['1', '5']:
            form_data['r405'] = None
            form_data['r406'] = None
            form_data['r407'] = None
            form_data['r408'] = None
            form_data['r409'] = None
            form_data['r411'] = None
            form_data['r412'] = None
            form_data['r415'] = None
            form_data['r416a'] = None
            form_data['r416b'] = None
            form_data['r417'] = None
            form_data['r418'] = None
            form_data['r420a'] = None
            form_data['r421'] = None
            form_data['r422_23'] = None
            form_data['r425'] = None
            form_data['r427'] = None
            form_data['r430'] = None
            form_data['r431a'] = None
            form_data['r431f'] = None

        else:
            if form_data.get('r405') is None:
                self._errors['r405'] = self.error_class(['Jika ART ditemukan/keluarga baru, maka isian jenis kelamin harus terisi'])
            
            if form_data.get('r406') is None:
                self._errors['r406'] = self.error_class(['Jika ART berstatus ditemukan/keluarga baru, maka tanggal lahir harus terisi'])

            if form_data.get('r407') is None :
                self._errors['r407'] = self.error_class(['Jika ART berstatus ditemukan/keluarga baru, maka umur harus terisi'])
            else:
                form_data['r407'] = int(form_data['r407'])
                if form_data.get('r406') is not None:
                    age = helpers.year_calculator(form_data.get('r406'))
                    if form_data['r407'] != age:
                        self._errors['r407'] = self.error_class(['Umur tidak sesuai dengan tanggal lahir'])

            if form_data.get('r408') is None:
                self._errors['r408'] = self.error_class(['Jika ART berstatus ditemukan/keluarga baru, maka status perkawinan harus terisi'])

            if form_data.get('r409') is None:
                self._errors['r409'] = self.error_class(['Jika ART berstatus ditemukan/keluarga baru, maka status hubungan dengan kepala keluarga harus terisi'])
            else:
                if form_data.get('r408') == '1':
                    if form_data.get('r409') in ['2', '4' ,'6']:
                        self._errors['r409'] = self.error_class(['Jika status hubungan dengan kepala keluarga adalah istri/suami/menantu/orangtua/mertua, maka status perkawinan tidak boleh "Belum Kawin"'])

            if form_data.get('r411') is None:
                self._errors['r411'] = self.error_class(['Jika ART berstatus ditemukan/keluarga baru, maka kepemilikan kartu identitas harus terisi'])

            if form_data.get('r412') is None:
                self._errors['r412'] = self.error_class(['Jika ART berstatus ditemukan/keluarga baru, maka partisipasi sekolah harus terisi'])
            else:
                if form_data.get('r415') is None:
                    self._errors['r415'] = self.error_class(['Jika ART masih bersekolah/pernah bersekolah, maka ijazah/STTB tertinggi harus terisi'])
                else:
                    pendidikan = form_data.get('r415')
                    age = form_data.get('r407')
                    if age is not None:
                        if pendidikan in ['1', '2', '3', '4', '5'] and int(age) < 11:
                            self._errors['r415'] = self.error_class(['Jika ART berpendidikan SD/Setara, maka umur ART harus berusia minimal 11 tahun'])
                        elif pendidikan in ['6', '7', '8', '9', '10'] and int(age) < 13 :
                            self._errors['r415'] = self.error_class(['Jika ART berpendidikan SMP/Setara, maka umur ART harus berusia minimal 13 tahun'])
                        elif pendidikan in ['11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22'] and int(age) < 17:
                            self._errors['r415'] = self.error_class(['Jika ART berpendidikan SMA - S3, maka umur ART harus berusia minimal 17 tahun'])

            if form_data.get('r416a') is None:
                self._errors['r416a'] = self.error_class(['Jika ART berstatus ditemukan/keluarga baru, maka status bekerja harus terisi'])
            else:
                if form_data.get('r416a') == '1':
                    if form_data.get('r416b') is None:
                        self._errors['r416b'] = self.error_class(['Jika ART bekerja selama seminggu yang lalu, maka jam kerja harus terisi'])
                    else:
                        if int(form_data.get('r416b')) < 1:
                            self._errors['r416b'] = self.error_class(['Jika ART bekerja selama seminggu yang lalu, maka jam kerja harus lebih dari 0 jam'])

                    if form_data.get('r417') is None:
                        self._errors['r417'] = self.error_class(['Jika ART bekerja selama seminggu yang lalu, maka lapangan usaha harus terisi'])
                    
                    if form_data.get('r418') is None:
                        self._errors['r418'] = self.error_class(['Jika ART bekerja selama seminggu yang lalu, maka status dalam bekerja harus terisi'])
                
                else:
                    form_data['r416b'] = None
                    form_data['r417'] = None
                    form_data['r418'] = None
                
            if form_data.get('r420a') is None:
                self._errors['r420a'] = self.error_class(['Jika ART berstatus ditemukan/keluarga baru, maka kepemilikan usaha harus terisi'])
            else:
                if form_data.get('r420a') == '1':
                    if form_data.get('r421') is None:
                        self._errors['r421'] = self.error_class(['Jika ART memiliki usaha, maka lapangan usaha dari usaha utama harus terisi'])
                    if form_data.get('r422_23') is None:
                        self._errors['r422_23'] = self.error_class(['Jika ART memiliki usaha, maka jumlah pekerja harus terisi'])
                    else:
                        if form_data.get('r422_23') < 1:
                            print('Jumalah tenaga kerja error')
                            self._errors['r422_23'] = self.error_class(['Jika ART memiliki usaha, maka jumlah pekerja harus lebih dari 0 jam'])

                    if form_data.get('r425') is None:
                        self._errors['r425'] = self.error_class(['Jika ART memiliki usaha, maka omset usaha utama perbulan harus terisi'])

                else:
                    form_data['r421'] = None
                    form_data['r422_23'] = None
                    form_data['r425'] = None
                    
            if form_data.get('r430') is None:
                self._errors['r430'] = self.error_class(['Jika ART berstatus ditemukan/keluarga baru, maka keluhan kesehatan harus terisi'])

            if form_data.get('r431a') is None:
                self._errors['r431a'] = self.error_class(['Jika ART berstatus ditemukan/keluarga baru, maka kepemilikan jaminan kesehatan harus terisi'])
            else:
                if form_data.get('r418') is not None and form_data.get('r418') == '5' and form_data.get('r431a') in ['0', '1', '4', '8', '99']:
                    self._errors['r431a'] = self.error_class(['Jika ART adalah PNS/TNI/Polri/ BUMN/BUMD/pejabat negara, maka kepemilikan jaminan kesehatan harus terisi JKN Mandiri'])

            if form_data.get('r431f') is None:
                self._errors['r431f'] = self.error_class(['Jika ART berstatus ditemukan/keluarga baru, maka kepemilikan jaminan ketenagakerjaan harus terisi'])

            self.cleaned_data = form_data
            return self.cleaned_data
