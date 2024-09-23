from . import models
from django.db.models import Q, Count
from pprint import pprint
from datetime import datetime
from django.db.models.functions import Length
from django.db.models import Avg, Sum
import numpy as np
from statistics import mean
from operator import itemgetter
from django.utils import timezone

def get_dashboard_family():
    families = models.FamiliesModels.objects.all().count()

    if families > 0 :

        #r301
        r301 = models.FamiliesModels.r301.field.choices
        model_r301 = models.FamiliesModels.objects.values('r301').annotate(count=Count('r301')).order_by('-count').first()
        model_r301['name'] = next((d[1] for d in r301 if d[0] == model_r301['r301'])) if model_r301['count'] != 0 else '-'

        #r303
        r303 = models.FamiliesModels.r303.field.choices
        model_r303 = models.FamiliesModels.objects.values('r303').annotate(count=Count('r303')).order_by('-count').first()
        model_r303['name'] = next((d[1] for d in r303 if d[0] == model_r303['r303'])) if model_r303['count'] != 0 else '-'

        #r304
        r304 = models.FamiliesModels.r304.field.choices
        model_r304 = models.FamiliesModels.objects.values('r304').annotate(count=Count('r304')).order_by('-count').first()
        model_r304['name'] = next((d[1] for d in r304 if d[0] == model_r304['r304'])) if model_r304['count'] != 0 else '-'

        #r306
        r306 = models.FamiliesModels.r306.field.choices
        model_r306 = models.FamiliesModels.objects.values('r306').annotate(count=Count('r306')).order_by('-count').first()
        model_r306['name'] = next((d[1] for d in r306 if d[0] == model_r306['r306'])) if model_r306['count'] != 0 else '-'

        #r307
        r307 = models.FamiliesModels.r307.field.choices
        model_r307 = models.FamiliesModels.objects.values('r307').annotate(count=Count('r307')).order_by('-count').first()
        model_r307['name'] = next((d[1] for d in r307 if d[0] == model_r307['r307'])) if model_r307['count'] != 0 else '-'

        #r310
        r310 = models.FamiliesModels.r310.field.choices
        model_r310 = models.FamiliesModels.objects.values('r310').annotate(count=Count('r310')).order_by('-count').first()
        model_r310['name'] = next((d[1] for d in r310 if d[0] == model_r310['r310'])) if model_r310['count'] != 0 else '-'

        model_r401b = models.FamiliesModels.objects.aggregate(Avg('r401b'))

        model_r402 = [
            {'key' : 'Sapi', 'val' : models.FamiliesModels.objects.aggregate(Sum('r402a')).get('r402a__sum')},
            {'key' : 'Kerbau', 'val' : models.FamiliesModels.objects.aggregate(Sum('r402b')).get('r402b__sum')},
            {'key' : 'Kuda', 'val' : models.FamiliesModels.objects.aggregate(Sum('r402c')).get('r402c__sum')},
            {'key' : 'Babi', 'val' : models.FamiliesModels.objects.aggregate(Sum('r402d')).get('r402d__sum')},
            {'key' : 'Kambing/Domba', 'val' : models.FamiliesModels.objects.aggregate(Sum('r402e')).get('r402e__sum')},
            {'key' : 'Ayam Ras Pedaging', 'val' : models.FamiliesModels.objects.aggregate(Sum('r402h')).get('r402h__sum')},
            {'key' : 'Ayam Ras Petelur', 'val' : models.FamiliesModels.objects.aggregate(Sum('r402i')).get('r402i__sum')},
        ]
        newlist = sorted(model_r402, key=itemgetter('val'), reverse=True)[0]

        dashboard_data = [
            {
                'indicator' : 'Status penguasaan bangunan tempat tinggal terbanyak',
                'value' : f'{model_r301["name"]}',
                'count' : f'{model_r301["count"]} ({round(model_r301["count"] / families * 100) }%)'
            },
            {
                'indicator' : 'Jenis lantai bangunan terluas yang digunakan keluarga',
                'value' : f'{model_r303["name"]}',
                'count' : f'{model_r303["count"]} ({round(model_r303["count"] / families * 100) }%)'
            },
            {
                'indicator' : 'Jenis dinding terluas yang digunakan keluarga',
                'value' : f'{model_r304["name"]}',
                'count' : f'{model_r304["count"]} ({round(model_r304["count"] / families * 100) }%)'
            },
            {
                'indicator' : 'Jenis atap bangunan terluas yang digunakan keluarga',
                'value' : f'{model_r306["name"]}',
                'count' : f'{model_r306["count"]} ({round(model_r306["count"] / families * 100) }%)'
            },
            {
                'indicator' : 'Sumber penerangan utama yang dominan digunakan keluarga',
                'value' : f'{model_r307["name"]}',
                'count' : f'{model_r307["count"]} ({round(model_r307["count"] / families * 100) }%)'
            },
            {
                'indicator' : 'Sumber air minum utama yang dominan dikonsumsi keluarga',
                'value' : f'{model_r310["name"]}',
                'count' : f'{model_r310["count"]} ({round(model_r310["count"] / families * 100) }%)'
            },
            {
                'indicator' : 'Rata-rata luas lahan yang dimiliki keluarga',
                'value' : f'{model_r401b["r401b__avg"]} M&sup2',
                'count' : '-'
            },
            {
                'indicator' : 'Hewan ternak terbanyak yang dimiliki keluarga',
                'value' : f'{newlist["key"]} ({newlist["val"]} ekor)',
                'count' : '-'
            },
        ]
    else:
        dashboard_data = [
            {
                'indicator' : '-',
                'value' : '-',
                'count' : '-'
            }]

    return dashboard_data

def get_dashboard_population():
    populations = models.PopulationsModels.objects.all().count()
    
    if populations > 0:

        #r505
        r505 = models.PopulationsModels.r505.field.choices
        model_r505 = models.PopulationsModels.objects.values('r505').annotate(count=Count('r505')).order_by('-count').first()
        model_r505['name'] = next((d[1] for d in r505 if d[0] == model_r505['r505'])) if model_r505['count'] != 0 else '-'

        #r301a
        r506 = models.PopulationsModels.r506.field.choices
        model_r506 = models.PopulationsModels.objects.values('r506').annotate(count=Count('r506')).order_by('-count').first()
        model_r506['name'] = next((d[1] for d in r506 if d[0] == model_r506['r506'])) if model_r506['count'] != 0 else '-'

        model_r508 = round(mean([dt.age for dt in models.PopulationsModels.objects.all()]))

        #r510
        r510 = models.PopulationsModels.r510.field.choices
        model_r510 = models.PopulationsModels.objects.values('r510').annotate(count=Count('r510')).order_by('-count').first()
        model_r510['name'] = next((d[1] for d in r510 if d[0] == model_r510['r510'])) if model_r510['count'] != 0 else '-'


        #r511
        r511 = models.PopulationsModels.r511.field.choices
        model_r511 = models.PopulationsModels.objects.values('r511').annotate(count=Count('r511')).order_by('-count').first()
        model_r511['name'] = next((d[1] for d in r511 if d[0] == model_r511['r511'])) if model_r511['count'] != 0 else '-'

        #r512
        r512 = models.PopulationsModels.r512.field.choices
        model_r512 = models.PopulationsModels.objects.values('r512').annotate(count=Count('r512')).order_by('-count').first()
        model_r512['name'] = next((d[1] for d in r512 if d[0] == model_r512['r512'])) if model_r512['count'] != 0 else '-'


        #r513
        r513 = models.PopulationsModels.r513.field.choices
        model_r513 = models.PopulationsModels.objects.values('r513').annotate(count=Count('r513')).order_by('-count').first()
        model_r513['name'] = next((d[1] for d in r513 if d[0] == model_r513['r513'])) if model_r513['count'] != 0 else '-'
        
        #r518
        r518 = models.PopulationsModels.r518.field.choices
        model_r518 = models.PopulationsModels.objects.values('r518').annotate(count=Count('r518')).order_by('-count').first()
        model_r518['name'] = next((d[1] for d in r518 if d[0] == model_r518['r518'])) if model_r518['count'] != 0 else '-'


        #r519
        r519 = models.PopulationsModels.r519.field.choices
        model_r519 = models.PopulationsModels.objects.values('r519').annotate(count=Count('r519')).order_by('-count').first()
        model_r519['name'] = next((d[1] for d in r519 if d[0] == model_r519['r519'])) if model_r519['count'] != 0 else '-'

        dashboard_data = [
            {
                'indicator' : 'Sebagian besar keberadaan penduduk',
                'value' : f'{model_r505["name"]}',
                'count' : f'{model_r505["count"]} ({round(model_r505["count"] / populations * 100) }%)'
            },
            {
                'indicator' : 'Sebagian besar jenis kelamin penduduk',
                'value' : f'{model_r506["name"]}',
                'count' : f'{model_r506["count"]} ({round(model_r506["count"] / populations * 100) }%)'
            },
            {
                'indicator' : 'Rata-rata umur penduduk',
                'value' : model_r508,
                'count' : '-'
            },
            {
                'indicator' : 'Sebagian besar status perkawinan/pernikahan',
                'value' : f'{model_r510["name"]}',
                'count' : f'{model_r510["count"]} ({round(model_r510["count"] / populations * 100) }%)'
            },
            {
                'indicator' : 'Sebagian besar agama yang dianut penduduk',
                'value' : f'{model_r511["name"]}',
                'count' : f'{model_r511["count"]} ({round(model_r511["count"] / populations * 100) }%)'
            },
                {
                'indicator' : 'Suku bangsa yang paling dominan',
                'value' : f'{model_r512["name"]}',
                'count' : f'{model_r512["count"]} ({round(model_r512["count"] / populations * 100) }%)'
            },
            {
                'indicator' : 'Kegiatan utama penduduk yang paling dominan',
                'value' : f'{model_r513["name"]}',
                'count' : f'{model_r513["count"]} ({round(model_r513["count"] / populations * 100) }%)'
            },
            {
                'indicator' : 'Jenjang pendidikan terakhir yang paling banyak ditamatkan',
                'value' : f'{model_r518["name"]}',
                'count' : f'{model_r518["count"]} ({round(model_r518["count"] / populations * 100) }%)'
            },
            {
                'indicator' : 'Sebagian besar jaminan kesehatan yang dimiliki penduduk',
                'value' : f'{model_r519["name"]}',
                'count' : f'{model_r519["count"]} ({round(model_r519["count"] / populations * 100) }%)'
            },
        ]
    else:
        dashboard_data = [
            {
                'indicator' : '-',
                'value' : '-',
                'count' : '-'
            }]

    return dashboard_data

def splitting_list(dt_list, n_component):

    if len(dt_list) < n_component:
        n_component = 2

    # Tentukan batas-batas interval
    bins_group = []
    bins = list(np.linspace(min(dt_list), max(dt_list), n_component+1, dtype=int))
    for idx in range(len(bins)):
        if idx < len(bins)-1 :
            bins_group.append((idx+1, int(bins[idx]), int(bins[idx+1])))

    groups = {}
    for num in dt_list:
        for ord, batas_bawah, batas_atas in bins_group:
            if batas_bawah <= num <= batas_atas:
                rentang_str = f"{ord}_{batas_bawah} - {batas_atas}"
                groups.setdefault(rentang_str, []).append(num)

    list_tuples = list(groups.items())
    groups = dict(sorted(list_tuples))

    groups_sorted = []
    for key, val in groups.items():
        groups_sorted.append((key.split('_')[1], len(val)))

    return groups_sorted


def check_sorted(list_):
    
    for idx, dt in zip(range(len(list_)), list_):
        if idx+1 != dt:
            return False

def comparing_date(date_first, date_last, format ='%Y-%m-%d'):
    # Konversi string ke objek datetime
    date_first = datetime.strptime(date_first, format)
    date_last = datetime.strptime(date_last, format)
    dev = date_last - date_first
    return dev.days >= 0 

def combine_validations(data_families, data_art):
    form_errors = {}
    
    if len(data_art) > 0:
        if int(data_families['r109']) != len(data_art):
            form_errors['r109'] = ['Jumlah ART tidak sesuai dengan jumlah art yang terisi']
    else:
        form_errors['r109'] = ['Jumlah ART adalah minimal 1']

    r501 = [int(dt['r501']) for dt in data_art]
    r504 = [dt['r504'] for dt in data_art]
    
    # Pastikan urutan anggota keluarga
    if check_sorted(r501) is False:
        form_errors['form_art_r501_1'] = ['Nomor urut ART harus berurut']

    # Validasi KRT, Harus ada, dan harus 1
    nama_kk = data_families['r107'].lower()
    for idx, dt in enumerate(data_art):
        if dt['r505'] in ['1', '4']:
            if '1' not in r504:
                form_errors[f'form_art_r504_{idx+1}'] = ['Keluarga belum memiliki kepala keluarga']
            else:
                if r504.count('1') != 1:
                    form_errors[f'form_art_r504_{idx+1}'] = ['Keluarga harus memiliki 1 kepala keluarga (tidak lebih)']
                else:
                    if dt['r504'] == '1' and dt['r503'].lower() != nama_kk:
                        form_errors[f'form_art_r503_{idx+1}'] = ['Nama kepala keluarga pada Blok V tidak sesuai dengan Blok I Rincian Nama KK']

    if len(form_errors) > 0 :
        return form_errors

    if len(data_art) > 1 :
        kk_gender = next((dt['r506'] for dt in data_art if dt['r504'] == '1'), None)
        for idx, dt in enumerate(data_art):
            if dt['r504'] == '2':
                if kk_gender == dt['r506']:
                    form_errors[f'form_art_r506_{idx+1}'] = [f'Pasangan istri/suami kepala keluarga tidak boleh berjenis kelamin sama']

    return form_errors


def age(date):

    today = timezone.now()
    age = today.year - date.year - ((today.month, today.day) < (date.month, date.day))

    return age

def get_region_code(r104, r105):

    data_region = dict()
    region = models.RegionAdministrativeModels.objects

    prov = r104[:2]
    provs = region.annotate(text_len=Length('reg_code')).filter(text_len=2).order_by('reg_code').values()
    opt_prov = [f'<option value="{dt["reg_code"]}" {"selected" if dt["reg_code"]==prov else ""}>[{dt["reg_code"]}]&ensp;{dt["reg_name"]}</option>' for dt in provs]

    data_region['prov'] = {
        'value' : prov,
        'opt' : ''.join(opt_prov)
    }

    kabkot = r104[:4]
    kabkots = region.annotate(text_len=Length('reg_code')).filter(text_len=4).filter(reg_code__icontains=prov).order_by('reg_code').values()
    opt_kabkots = [f'<option value="{dt["reg_code"]}" {"selected" if dt["reg_code"]==kabkot else ""}>[{dt["reg_code"]}]&ensp;{dt["reg_name"]}</option>' for dt in kabkots]
    data_region['kabkot'] = {
        'value' : kabkot,
        'opt' : ''.join(opt_kabkots)
    }

    kec = r104[:7]
    kecs = region.annotate(text_len=Length('reg_code')).filter(text_len=7).filter(reg_code__icontains=kabkot).order_by('reg_code').values()
    opt_kabkots = [f'<option value="{dt["reg_code"]}" {"selected" if dt["reg_code"]==kec else ""}>[{dt["reg_code"]}]&ensp;{dt["reg_name"]}</option>' for dt in kecs]
    data_region['kec'] = {
        'value' : kec,
        'opt' : ''.join(opt_kabkots)
    }

    r104_model = region.filter(reg_code = r104).first()
    r104_lists = region.annotate(text_len=Length('reg_code')).filter(text_len=10).filter(reg_code__icontains=kec).order_by('reg_code').values()
    opt_r104 = [f'<option value="{dt["id"]}" {"selected" if dt["reg_code"]==r104 else ""}>[{dt["reg_code"]}]&ensp;{dt["reg_name"]}</option>' for dt in r104_lists]
    data_region['r104'] = {
        'value' : r104_model.pk,
        'opt' : ''.join(opt_r104)
    }

    r105_lists = models.RegionSLSModels.objects.filter(reg_code = r104_model.pk ).values()
    opt_r105 = [f'<option value="{dt["id"]}" {"selected" if dt["id"]==r105 else ""}>[{dt["reg_sls_code"]}]&ensp;{dt["reg_sls_name"]}</option>' for dt in r105_lists]
    data_region['r105'] = {
        'value' : r105,
        'opt' : ''.join(opt_r105)
    }

    return data_region

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
        {'val' : '', 'text' : '---------'},
        {'val' : 1, 'text' : 'Jumlah Keluarga Berdasarkan Status Penguasaan Bangunan Tempat Tinggal'},
        {'val' : 2, 'text' : 'Jumlah Keluarga Berdasarkan Status Kepemilikan Lahan Tempat Tinggal'},
        {'val' : 3, 'text' : 'Jumlah Keluarga Berdasarkan Jenis Lantai Bangunan Terluas'},
        {'val' : 4, 'text' : 'Jumlah Keluarga Berdasarkan Jenis Dinding Bangunan Terluas'},
        {'val' : 5, 'text' : 'Jumlah Keluarga Berdasarkan Jenis Atap Bangunan Terluas'},
        {'val' : 6, 'text' : 'Jumlah Keluarga Berdasarkan Ketersedian ventilasi udara (jendela)'},
        {'val' : 7, 'text' : 'Jumlah Keluarga Berdasarkan Sumber Penerangan Utama'},
        {'val' : 8, 'text' : 'Jumlah Keluarga Berdasarkan Ketersedian Tempat Pembuangan Sampah'},
        {'val' : 9, 'text' : 'Jumlah Keluarga Berdasarkan Sumber Air Minum Utama'},
        {'val' : 10, 'text' : 'Jumlah Keluarga Berdasarkan Kepemilikan Tanah/Lahan Pertanian'},
        {'val' : 11, 'text' : 'Jumlah Keluarga Berdasarkan Luas Lahan Pertanian'},
        {'val' : 12, 'text' : 'Jumlah Keluarga Berdasarkan Kepemilikan Hewan Ternak'}
    ]

    return opts


def get_tab_populations():
    opts = [
        {'val' : '', 'text' : '---------'},
        {'val' : 1, 'text' : 'Jumlah Penduduk Menurut Hubungan dengan KK' },
        {'val' : 2, 'text' : 'Jumlah Penduduk Menurut Keberadan Anggota Rumah Tangga' },
        {'val' : 3, 'text' : 'Jumlah Penduduk Menurut Jenis Kelamin' },
        {'val' : 4, 'text' : 'Jumlah Penduduk Menurut Status Perkawinan' },
        {'val' : 5, 'text' : 'Jumlah Penduduk Menurut Agama' },
        {'val' : 6, 'text' : 'Jumlah Penduduk Menurut Suku' },
        {'val' : 7, 'text' : 'Jumlah Penduduk Menurut Kegiatan Utama' },
        {'val' : 8, 'text' : 'Jumlah Penduduk Menurut Lapangan Usaha' },
        {'val' : 9, 'text' : 'Jumlah Penduduk Menurut Partisipasi Sekolah' },
        {'val' : 10, 'text' : 'Jumlah Penduduk Menurut Pendidikan Tinggi yang Ditamatkan' },
        {'val' : 11, 'text' : 'Jumlah Penduduk Menurut Jaminan Kesehatan' },
        {'val' : 12, 'text' : 'Jumlah Penduduk Menurut Keterangan Disabilitas' }
    ]

    return opts


def labor_participation(model):
    labors = []   
    labors_work = []
    for dt in model:
        if dt.age > 15 :
            labors.append(dt)

        if dt.r513 in ['4', '5']:
            labors_work.append(dt)

    labor_participation = round(len(labors_work) / len(labors) * 100) if len(labors) != 0 else 0
    return labor_participation
