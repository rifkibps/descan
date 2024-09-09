from typing import Any
from . import models
from django import forms
from pprint import pprint
from datetime import date
from . import helpers


# class PopulationsForm(forms.ModelForm):

#     class Meta:
#         model = models.PopulationsModels
#         fields = "__all__"

class FamiliesForm(forms.ModelForm):

    class Meta:
        model = models.FamiliesModels
        fields = "__all__"

    def clean(self):
        form_data = self.cleaned_data 
        data_not_cleaned = self.data

        if form_data.get('r202') is not None and form_data.get('r203') is not None and form_data.get('r205') is not None:
            if helpers.comparing_date(str(form_data['r202']), str(form_data['r203'])) is False:
                self._errors['r203'] = self.error_class(['Tgl kunjungan pertama tidak boleh lebih besar dari tgl kunjungan terakhir'])

            if helpers.comparing_date(str(form_data['r203']), str(form_data['r205'])) is False:
                self._errors['r205'] = self.error_class(['Tgl kunjungan akhir tidak boleh lebih besar dari tgl pemeriksaan'])

        if form_data.get('r108') is not None:
            # Validasi NIK
            if form_data['r108'].isnumeric() == False or len(form_data['r108']) != 16:
                self._errors['r108'] = self.error_class(['Format Nomor kartu Keluarga harus berupa angka 16 digit.'])
            else:
                check_kk = models.FamiliesModels.objects.filter(r108=form_data['r108'])
                if check_kk.exists():
                    if data_not_cleaned.get('id') is not None:
                        if check_kk.first().pk != int(data_not_cleaned.get('id')):
                            self._errors['r108'] = self.error_class(['No KK telah terdaftar pada database'])
                    else:
                        self._errors['r108'] = self.error_class(['No KK telah terdaftar pada database'])

        if form_data.get('r109') is not None:
            form_data['r109'] = int(form_data['r109'])
            if form_data['r109'] < 1:
                self._errors['r109'] = self.error_class(['Jumlah ART harus lebih dari 0.'])

        if form_data.get('r301') is not None :
            if form_data.get('r301') == '1':
                if form_data.get('r302') is None:
                    self._errors['r302'] = self.error_class(['Jika status penguasaan bangunan tempat tinggal adalah milik sendiri, maka status lahan yang ditempati harus terisi.'])
            else:
                form_data['r302'] = None

        if form_data.get('r401a') is not None and form_data.get('r401a') == '1':
            if form_data.get('r401b') is None or form_data.get('r401b') < 1:
                self._errors['r401b'] = self.error_class(['Jika memiliki tanah/lahan pertanian, maka luas lahan yang dimiliki harus terisi.'])
        else:
            form_data['r401b'] = None

        if form_data.get('r402a') is not None and form_data.get('r402a') < 0:
            self._errors['r402a'] = self.error_class(['Jumlah kepemilikan hewan ternak Sapi tidak boleh kurang dari 0.'])

        if form_data.get('r402b') is not None and form_data.get('r402b') < 0:
            self._errors['r402b'] = self.error_class(['Jumlah kepemilikan hewan ternak Kerbau tidak boleh kurang dari 0.'])

        if form_data.get('r402c') is not None and form_data.get('r402c') < 0:
            self._errors['r402c'] = self.error_class(['Jumlah kepemilikan hewan ternak Kuda tidak boleh kurang dari 0.'])

        if form_data.get('r402d') is not None and form_data.get('r402d') < 0:
            self._errors['r402d'] = self.error_class(['Jumlah kepemilikan hewan ternak Babi tidak boleh kurang dari 0.'])

        if form_data.get('r402e') is not None and form_data.get('r402e') < 0:
            self._errors['r402e'] = self.error_class(['Jumlah kepemilikan hewan ternak Kambing/Domba tidak boleh kurang dari 0.'])

        self.cleaned_data = form_data
        return self.cleaned_data

class PopulationsForm(forms.ModelForm):
    class Meta:
        model = models.PopulationsModels
        fields = "__all__"

    def clean(self):

        form_data = self.cleaned_data
        data_not_cleaned = self.data
        
        if form_data.get('r501') is not None:
            if int(form_data['r501']) < 1:
                self._errors['r501'] = self.error_class(['Nomor urut harus lebih dari 1'])

        if form_data.get('r502') is not None:
            if form_data['r502'].isnumeric() == False or len(form_data['r502']) != 16:
                self._errors['r502'] = self.error_class(['Format Nomor kartu Keluarga harus berupa angka 16 digit.'])
            else:
                check_nik = models.PopulationsModels.objects.filter(r502=form_data['r502'])
                if check_nik.exists():
                    if data_not_cleaned.get('art_id') is not None:
                        if check_nik.first().pk != int(data_not_cleaned.get('art_id')):
                            self._errors['r502'] = self.error_class(['NIK telah terdaftar pada database'])
                    else:
                        self._errors['r502'] = self.error_class(['NIK telah terdaftar pada database'])

        if form_data.get('r504') is not None and form_data.get('r510') is not None:
            if form_data.get('r504') in ['2', '4', '6'] and form_data.get('r510') == '1':
                self._errors['r510'] = self.error_class(['Jika ART bersatus Istri/Suami/Menantu/Mertua/Orang Tua, maka status pernikahan tidak boleh "Belum Kawin'])

        if form_data.get('r505') is not None:
            if form_data['r505'] not in ['1', '4']:
                form_data['r513'] = None
                form_data['r517'] = None
                form_data['r519'] = None
                form_data['r520a'] = None
                form_data['r520b'] = None
                form_data['r520c'] = None
                form_data['r520d'] = None
                form_data['r520e'] = None
                form_data['r520f'] = None
                form_data['r520g'] = None
                form_data['r520h'] = None
                form_data['r520i'] = None
            else:
                if form_data.get('r513') is None:
                    self._errors['r513'] = self.error_class(['Jika ART tinggal bersama/keluarga baru, maka kegiatan pekerjaan utama harus terisi'])
                else:
                    if form_data.get('r513') == '5':
                        if form_data.get('r514') is None:
                            self._errors['r514'] = self.error_class(['Jika ART bekerja, maka pekerjaan utama harus terisi'])

                        if form_data.get('r515') is None:
                            self._errors['r515'] = self.error_class(['Jika ART bekerja, maka lapangan usaha utama harus terisi'])

                        if form_data.get('r516') is None:
                            self._errors['r516'] = self.error_class(['Jika ART bekerja, maka komoditas utama harus terisi'])
                    else:
                        form_data['r514'] = None
                        form_data['r515'] = None
                        form_data['r516'] = None

                if form_data.get('r517') is None:
                    self._errors['r517'] = self.error_class(['Jika ART tinggal bersama/keluarga baru, maka partisipasi sekolah harus terisi'])
                else:
                    if form_data.get('r513') is not None and form_data.get('r513') == '1':
                        if form_data.get('r517') != '2':
                            self._errors['r517'] = self.error_class(['Jika kegiatan utama ART adalah bersekolah, maka partisipasi sekolah harus terisi "Masih Sekolah"'])

                    if form_data.get('r517') in ['2', '3']:
                        if form_data.get('r518') is None:
                            self._errors['r518'] = self.error_class(['Jika ART masih bersekolah/tidak bersekolah lagi, maka jenjang pendidikan tertinggi harus terisi'])
                    else:
                        form_data['r518'] = None
                
                if form_data.get('r519') is None:
                    self._errors['r519'] = self.error_class(['Jika ART tinggal bersama/keluarga baru, maka isian jaminan kesehatan harus terisi'])

                if form_data.get('r520a') is None:
                    self._errors['r520a'] = self.error_class(['Jika ART tinggal bersama/keluarga baru, maka isian disabilitas tunanetra/buta harus terisi'])
                if form_data.get('r520b') is None:
                    self._errors['r520b'] = self.error_class(['Jika ART tinggal bersama/keluarga baru, maka isian disabilitas tunarungu/tuli harus terisi'])
                if form_data.get('r520c') is None:
                    self._errors['r520c'] = self.error_class(['Jika ART tinggal bersama/keluarga baru, maka isian disabilitas tunawicara/bisu harus terisi'])
                if form_data.get('r520d') is None:
                    self._errors['r520d'] = self.error_class(['Jika ART tinggal bersama/keluarga baru, maka isian disabilitas tunarungu–wicara/tuli–bisu harus terisi'])
                if form_data.get('r520e') is None:
                    self._errors['r520e'] = self.error_class(['Jika ART tinggal bersama/keluarga baru, maka isian disabilitas tunadaksa/ cacat tubuh harus terisi'])
                if form_data.get('r520f') is None:
                    self._errors['r520f'] = self.error_class(['Jika ART tinggal bersama/keluarga baru, maka isian disabilitas tunagrahita harus terisi'])
                if form_data.get('r520g') is None:
                    self._errors['r520g'] = self.error_class(['Jika ART tinggal bersama/keluarga baru, maka isian disabilitas tunalaras harus terisi'])
                if form_data.get('r520h') is None:
                    self._errors['r520h'] = self.error_class(['Jika ART tinggal bersama/keluarga baru, maka isian disabilitas cacat ganda harus terisi'])

        self.cleaned_data = form_data
        return self.cleaned_data
