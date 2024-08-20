from . import models
from django.db.models import Q
from datetime import date

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

     