from . import models
from django.db.models import Q
from django.db.models import Q, Count, Sum
from pprint import pprint
from django.utils import timezone


def check_sorted(list_):
    for idx, dt in zip(range(len(list_)), list_):
        if idx != dt:
            return False


def year_calculator(date):

    today = timezone.now()
    age = today.year - date.year - ((today.month, today.day) < (date.month, date.day))

    return age


def combine_validations(data_families, data_art):
    form_errors = {}

    if len(data_art) > 0:
        if int(data_families['r112']) != len(data_art):
            form_errors['r112'] = 'Jumlah anggota keluarga tidak sesuai dengan jumlah art yang terisi'
    else:
        form_errors['r112'] = 'Jumlah anggota keluarga adalah minimal 1'
    
    r401 = [int(dt['r401']) for dt in data_art]
    r409 = [dt['r409'] for dt in data_art]
    
    # Pastikan urutan anggota keluarga
    if check_sorted(r401) is False:
        form_errors['form_art_r401_1'] = 'Nomor urut ART harus berurut'

    # Validasi KRT, Harus ada, dan harus 1
    for dt in data_art:
        if dt['r404'] in ['1', '5']:
            if '1' not in r409:
                form_errors['form_art_r409_1'] = 'Keluarga belum memiliki kepala keluarga'
            else:
                if r409.count('1') > 1:
                    form_errors['form_art_r409_1'] = 'Keluarga harus memiliki 1 kepala keluarga (tidak lebih)'


    if data_families['r506'] in ['1', '3']:
        error_r506 = False
        for dt in data_art:
            if dt['r420a'] != '2':
                error_r506 = True

        if error_r506 is False:
            form_errors[f'form_art_r420a_1'] = 'Keluarga memiliki rekening aktif untuk usaha, tetapi tidak ada ART yang memiliki usaha sendiri/bersama.'
    
    return form_errors

def transform_data(data):

    all_keys = list(set(key for d in data for key in d))
    results = []
    for i in range(len(list(data[0].values())[0])):
        new_dict = {}
        for key in all_keys:
            new_dict[key] = next((list(dt.values())[0][i] for dt in data if key in dt.keys()), None)
    
        results.append(new_dict)

    return results

def get_modus_family_chars():
    model = models.FamiliesModels.objects.values('r415').annotate(
            count=Count('r415')).order_by('-count').first()
    return model


def generate_table(header, body):
    
    thead = '<thead><tr>'
    for head in header:
        thead += f'<th class="{head["class"]}">{head["name"]}</th>'
    thead += '</tr></thead>'

    tbody = '<tbody>'
    for dt in body:
        row = '<tr>'
        for col_dt in dt:
            row += f'<td class="{col_dt[1]}">{col_dt[0]}</td>'
        row += '</tr>'
        tbody += row
    tbody += '</tbody>'

    return f'{thead} {tbody}'


def get_tab_families():

    opts = [
        {'val' : None, 'text' : '----'},
        {'val' : 1, 'text' : 'Jumlah Keluarga Menurut Pendidikan Tertinggi KRT'},
        {'val' : 2, 'text' : 'Jumlah Keluarga Menurut Status Kepemilikan Bangunan Tempat Tinggal'},
        {'val' : 3, 'text' : 'Jumlah Keluarga Menurut Bukti kepemilikan Tanah Bangunan Tempat Tinggal'},
        {'val' : 4, 'text' : 'Jumlah Keluarga Menurut Luas Lantai Bangunan Tempat Tinggal'},
        {'val' : 5, 'text' : 'Jumlah Keluarga Menurut Jenis Lantai Terluas'},
        {'val' : 6, 'text' : 'Jumlah Keluarga Menurut Jenis Dinding Terluas'},
        {'val' : 7, 'text' : 'Jumlah Keluarga Menurut Jenis Atap Terluas'},
        {'val' : 8, 'text' : 'Jumlah Keluarga Menurut Sumber Air Minum Utama'},
        {'val' : 9, 'text' : 'Jumlah Keluarga Menurut Jarak Sumber Air Minum Utama ke Tempat Penampungan Limbah'},
        {'val' : 10, 'text' : 'Jumlah Keluarga Menurut Sumber Penerangan Utama'},
        {'val' : 11, 'text' : 'Jumlah Keluarga Menurut Daya yang Terpasang'},
        {'val' : 12, 'text' : 'Jumlah Keluarga Menurut Bahan Bakar/Energi Utama untuk Memasak'},
        {'val' : 13, 'text' : 'Jumlah Keluarga Menurut Kepemilikan dan Penggunaan Fasilitas Tempat Buang Air Besar'},
        {'val' : 14, 'text' : 'Jumlah Keluarga Menurut Jenis Kloset'},
        {'val' : 15, 'text' : 'Jumlah Keluarga Menurut Tempat Pembuangan Akhir Tinja'},
        {'val' : 16, 'text' : 'Jumlah Keluarga Menurut Penerima Program Bantuan Sosial Sembako/ BPNT'},
        {'val' : 17, 'text' : 'Jumlah Keluarga Menurut Penerima Program Keluarga Harapan (PKH)'},
        {'val' : 18, 'text' : 'Jumlah Keluarga Menurut Penerima Program Bantuan Langsung Tunai (BLT) Desa'},
        {'val' : 19, 'text' : 'Jumlah Keluarga Menurut Penerima Program Subsidi Listrik (Gratis/Pemotongan Biaya)'},
        {'val' : 20, 'text' : 'Jumlah Keluarga Menurut Penerima Program Bantuan Pemerintah Daerah'},
        {'val' : 21, 'text' : 'Jumlah Keluarga Menurut Penerima Program Bantuan Subsidi Pupuk'},
        {'val' : 22, 'text' : 'Jumlah Keluarga Menurut Penerima Program Subsidi LPG'},

        {'val' : 23, 'text' : 'Jumlah Keluarga Menurut Kepemilikan Tabung gas 5,5 kg atau lebih'},
        {'val' : 24, 'text' : 'Jumlah Keluarga Menurut Kepemilikan Lemari Es/Kulkas'},
        {'val' : 25, 'text' : 'Jumlah Keluarga Menurut Kepemilikan Air Conditioner (AC)'},
        {'val' : 26, 'text' : 'Jumlah Keluarga Menurut Kepemilikan Pemanas Air (Water Heater)'},
        {'val' : 27, 'text' : 'Jumlah Keluarga Menurut Kepemilikan Telepon Rumah (PSTN)'},
        {'val' : 28, 'text' : 'Jumlah Keluarga Menurut Kepemilikan Televisi Layar Datar (Min. 30 Inci)'},
        {'val' : 29, 'text' : 'Jumlah Keluarga Menurut Kepemilikan Emas/Perhiasan (Min. 10 gram)'},
        {'val' : 30, 'text' : 'Jumlah Keluarga Menurut Kepemilikan Komputer/Laptop/Tablet'},
        {'val' : 31, 'text' : 'Jumlah Keluarga Menurut Kepemilikan Sepeda Motor'},
        {'val' : 32, 'text' : 'Jumlah Keluarga Menurut Kepemilikan Mobil'},

        {'val' : 33, 'text' : 'Jumlah Keluarga Menurut Kepemilikan Aset Lahan (selain yang ditempati)'},
        {'val' : 34, 'text' : 'Jumlah Keluarga Menurut Kepemilikan Aset Rumah/Bangunan di Tempat Lain'},
        {'val' : 35, 'text' : 'Jumlah Keluarga Menurut Kepemilikan Hewan Ternak'},
        {'val' : 36, 'text' : 'Jumlah Keluarga Menurut Kepemilikan Rekening Aktif'}
    ]

    return opts
def get_tab_populations():
    opts = [
        {'val' : None, 'text' : '----'},
        {'val' : 1, 'text' : 'Jumlah Penduduk Menurut Jenis Kelamin dan Kelompok Umur' },
        {'val' : 2, 'text' : 'Jumlah Penduduk Menurut Status Perkawinan' },
        {'val' : 3, 'text' : 'Jumlah Penduduk Menurut Status Bekerja' },
        {'val' : 4, 'text' : 'Rata-rata Jam Kerja Menurut Kelompok Umur' },
        {'val' : 5, 'text' : 'Rata-rata Jam Kerja Menurut Jenis Kelamin' },
        {'val' : 6, 'text' : 'Jumlah Penduduk >15 Tahun yang Bekerja Selama Seminggu yang lalu Menurut Status Pekerjaan Utama' },
        {'val' : 7, 'text' : 'Jumlah penduduk menurut kepemilikan usaha sendiri/bersama' },
        {'val' : 8, 'text' : 'Rata-rata Jumlah Pekerja yang Dibayar pada Usaha Utama' },
        {'val' : 9, 'text' : 'Rata-rata Jumlah Pekerja yang Tidak Dibayar pada Usaha Utama' },
        {'val' : 10, 'text' : 'Pengelompokan Omzet Usaha Utama Perbulan' },
        {'val' : 11, 'text' : 'Jumlah Penduduk Menurut Keluhan Kesehatan Kronis/Menahun' },
    ]

    return opts

def count_of_welfare_recips():
    model = models.PopulationsModels.objects.filter(
        Q(family_id__r501a = '1') |
        Q(family_id__r501b = '1') |
        Q(family_id__r501c = '1') |
        Q(family_id__r501d = '1') |
        Q(family_id__r501e = '1') |
        Q(family_id__r501f = '1') |
        Q(family_id__r501g = '1') | 
        Q(r431a = '1')
    ).values('family_id', 'family_id__r108').distinct()

    return model

def labor_participation():
    
    labor_force = models.PopulationsModels.objects.filter(
        Q(r407__gte = 15) & Q(r407__lte = 64) 
    )

    laber_force_work = labor_force.filter(
        (Q(r416a = 1) & ~Q(r416b = 0)) |
        (Q(r420a = 1) & ~Q(r422_23 = 0))
    )

    labor_participation = round(laber_force_work.count() / labor_force.count() * 100, 2)

    return labor_participation

     