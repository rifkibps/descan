from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from . import models, helpers, forms
from django.http import JsonResponse
from pprint import pprint
from django.db.models import Q, Count, Sum, Avg
from django.db.models.functions import Length
import json
from django.shortcuts import get_object_or_404

# Create your views here.
class DashboardClassView(LoginRequiredMixin, View):
    
    def get(self, request):
        families = models.FamiliesModels.objects.all().count()
        populations = models.PopulationsModels.objects.all().count()
        welfare_recips = helpers.count_of_welfare_recips().count()
        labor_percentage = helpers.labor_participation()
        
        dashboard = models.FamiliesModels.objects.aggregate(
                    r501a =Count('r501a', filter=Q(r501a='1')),
                    r501b =Count('r501b', filter=Q(r501b='1')),
                    r501c =Count('r501c', filter=Q(r501c='1')),
                    r501d =Count('r501d', filter=Q(r501d='1')),
                    r501e =Count('r501e', filter=Q(r501e='1')),
                    r501f =Count('r501f', filter=Q(r501f='1')),
                    r501g =Count('r501g', filter=Q(r501g='1')),
                )
        
        for key, val in dashboard.items():
            dashboard[key] = round(val/families*100)


        #r415
        r415 = models.PopulationsModels.r415.field.choices
        model_r415 = models.PopulationsModels.objects.filter(r409 = '1').values('r415').annotate(count=Count('r415')).order_by('-count').first()
        model_r415['name'] = next((d[1] for d in r415 if d[0] == model_r415['r415'])) if model_r415['count'] != 0 else '-'


        #r301a
        r301a = models.FamiliesModels.r301a.field.choices
        model_r301a = models.FamiliesModels.objects.values('r301a').annotate(count=Count('r301a')).order_by('-count').first()
        model_r301a['name'] = next((d[1] for d in r301a if d[0] == model_r301a['r301a'])) if model_r301a['count'] != 0 else '-'

        #r302
        model_r302 = models.FamiliesModels.objects.aggregate(avg=Avg('r302'))

        #r303
        r303 = models.FamiliesModels.r303.field.choices
        model_r303 = models.FamiliesModels.objects.values('r303').annotate(count=Count('r303')).order_by('-count').first()
        model_r303['name'] = next((d[1] for d in r303 if d[0] == model_r303['r303'])) if model_r303['count'] != 0 else '-'

        

        #r304
        r304 = models.FamiliesModels.r304.field.choices
        model_r304 = models.FamiliesModels.objects.values('r304').annotate(count=Count('r304')).order_by('-count').first()
        model_r304['name'] = next((d[1] for d in r304 if d[0] == model_r304['r304'])) if model_r304['count'] != 0 else '-'

        

        #r305
        r305 = models.FamiliesModels.r305.field.choices
        model_r305 = models.FamiliesModels.objects.values('r305').annotate(count=Count('r305')).order_by('-count').first()
        model_r305['name'] = next((d[1] for d in r305 if d[0] == model_r305['r305'])) if model_r305['count'] != 0 else '-'
        
        #r306a
        r306a = models.FamiliesModels.r306a.field.choices
        model_r306a = models.FamiliesModels.objects.values('r306a').annotate(count=Count('r306a')).order_by('-count').first()
        model_r306a['name'] = next((d[1] for d in r306a if d[0] == model_r306a['r306a'])) if model_r306a['count'] != 0 else '-'

        #r307a
        r307a = models.FamiliesModels.r307a.field.choices
        model_r307a = models.FamiliesModels.objects.values('r307a').annotate(count=Count('r307a')).order_by('-count').first()
        model_r307a['name'] = next((d[1] for d in r307a if d[0] == model_r307a['r307a'])) if model_r307a['count'] != 0 else '-'

        #r307b
        r307b = models.FamiliesModels.r307b.field.choices
        model_r307b = models.FamiliesModels.objects.values('r307b').annotate(count=Count('r307b')).order_by('-count').first()
        model_r307b['name'] = next((d[1] for d in r307b if d[0] == model_r307b['r307b'])) if model_r307b['count'] != 0 else '-'

        #r308
        r308 = models.FamiliesModels.r308.field.choices
        model_r308 = models.FamiliesModels.objects.values('r308').annotate(count=Count('r308')).order_by('-count').first()
        model_r308['name'] = next((d[1] for d in r308 if d[0] == model_r308['r308'])) if model_r308['count'] != 0 else '-'

        dashboard_table = [
            {
                'indicator' : 'Sebagian besar Pendidikan Tertinggi KRT di Desa Banggai',
                'value' : f'{model_r301a["name"]}',
                'count' : f'{model_r301a["count"]}'
            },
            {
                'indicator' : 'Sebagian besar Status Kepemilikan Bangunan Tempat Tinggal di Desa Banggai',
                'value' : f'{model_r415["name"]}',
                'count' : f'{model_r415["count"]}'
            },
            {
                'indicator' : 'Rata-rata Luas Lantai Bangunan Tempat Tinggal di Desa Banggai',
                'value' : f'{model_r302["avg"]} M2',
                'count' : '-'
            },
            {
                'indicator' : 'Sebagian besar Jenis Lantai Bangunan Tempat Tinggal Terluas di Desa Banggai',
                'value' : f'{model_r303["name"]}',
                'count' : f'{model_r303["count"]}'
            },
            {
                'indicator' : 'Sebagian besar Jenis Dinding Tempat Tinggal Terluas Keluarga di Desa Banggai',
                'value' : f'{model_r304["name"]}',
                'count' : f'{model_r304["count"]}'
            },
            {
                'indicator' : 'Sebagian besar Jenis Atap Tempat Tinggal Terluas Keluarga di Desa Banggai',
                'value' : f'{model_r305["name"]}',
                'count' : f'{model_r305["count"]}'
            },
            {
                'indicator' : 'Sebagian besar Sumber Air Minum Utama Keluarga di Desa Banggai',
                'value' : f'{model_r306a["name"]}',
                'count' : f'{model_r306a["count"]}'
            },
            {
                'indicator' : 'Sebagian besar Sumber Penerangan Utama di Desa Banggai',
                'value' : f'{model_r307a["name"]}',
                'count' : f'{model_r307a["count"]}'
            },
            {
                'indicator' : 'Sebagian besar Daya Listrik yang Terpasang di Desa Banggai',
                'value' : f'{model_r307b["name"]}',
                'count' : f'{model_r307b["count"]}'
            },
            {
                'indicator' : 'Sebagian besar Bahan Bakar untuk Memasak di Desa Banggai',
                'value' : f'{model_r308["name"]}',
                'count' : f'{model_r308["count"]}'
            },
        ]
  

        context = {
            'title' : 'Halaman Dashboard',
            'families' : families,
            'populations' : populations,
            'welfare_recips' : welfare_recips,
            'labor_percentage' : labor_percentage,
            'dashboard' : dashboard,
            'dashboard_table' : dashboard_table
        }

        return render(request, 'app/dashboard/dashboard.html', context)


class TabulationsFamiliesClassView(LoginRequiredMixin, View):
    
    def get(self, request):

        families = models.FamiliesModels.objects.count()
        families_electricity = models.FamiliesModels.objects.filter(r307a__in =['1', '2']).count()
        welfare_recips = helpers.count_of_welfare_recips().count()
        sanition_family = models.FamiliesModels.objects.filter(r309a = '1').count()

        education_levels = models.PopulationsModels.r415.field.choices
        home_ownership_state = models.FamiliesModels.r301a.field.choices

        tabulations = helpers.get_tab_families()
        context = {
            'title' : 'Tabulasi Data Keluarga',
            'families' : families,
            'families_electricity' : families_electricity,
            'sanition_family' : sanition_family,
            'welfare_recips' : welfare_recips,
            'education_levels' : education_levels,
            'home_ownership_state' : home_ownership_state,
            'tabulations' : tabulations
        }
        return render(request, 'app/tabulasi/tabulasi-keluarga.html', context)

class TabulationsFamiliesFetchClassView(LoginRequiredMixin, View):

    def post(self, request):
        is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
        if is_ajax:
            if request.method == 'POST':
                
                tabs = helpers.get_tab_families()
                tab_request = int(request.POST.get('tab_request'))
                check_tab = next((d['text'] for (index, d) in enumerate(tabs) if d['val'] == tab_request), None)
                if check_tab is None:
                    return JsonResponse({"status": 'failed'}, status=400)
                
                data_tabs = {}
                if tab_request == 12:
                    model = models.FamiliesModels.objects.aggregate(
                        section1 =Count('r308', filter=Q(r308='1')),
                        section2 =Count('r308', filter=Q(r308='2')),
                        section3 =Count('r308', filter=Q(r308='3')),
                        section4 =Count('r308', filter=Q(r308='4')),
                        section5 =Count('r308', filter=Q(r308='5')),
                        section6 =Count('r308', filter=Q(r308='6')),
                        section7 =Count('r308', filter=Q(r308='7')),
                        section8 =Count('r308', filter=Q(r308='8')),
                        section9 =Count('r308', filter=Q(r308='9')),
                        section10 =Count('r308', filter=Q(r308='10')),
                        section11 =Count('r308', filter=Q(r308='11')),
                        section12 =Count('r308', filter=Q(r308='00'))
                    )
                    model = list(model.values())

                    r308 = models.FamiliesModels.r308.field.choices
                    data = [[(idx+1, 'text-center'), (dt[1], 'text-left'), (model[idx], 'text-center')] for idx, dt in enumerate(r308)]
                        
                    data_tabs['title'] = check_tab
                    data_tabs['content_table'] = helpers.generate_table(
                        [{'name':'No', 'class' : 'text-center'}, {'name':'Sumber Energi/Bahan Bakar', 'class' : ''}, {'name':'Jumlah Keluarga', 'class' : 'text-center'}],
                        data
                    )

                    return JsonResponse({"status": 'success', 'content' : data_tabs }, status=200)
                elif tab_request == 3:

                    r301b = models.FamiliesModels.r301b.field.choices
                    model = models.FamiliesModels.objects.aggregate(
                        section1 =Count('r301b', filter=Q(r301b='1')),
                        section2 =Count('r301b', filter=Q(r301b='2')),
                        section3 =Count('r301b', filter=Q(r301b='3')),
                        section4 =Count('r301b', filter=Q(r301b='4')),
                        section5 =Count('r301b', filter=Q(r301b='5')),
                        section6 =Count('r301b', filter=Q(r301b='6'))
                    )
                    model = list(model.values())
                    data = [[(idx+1, 'text-center'), (dt[1], 'text-left'), (model[idx], 'text-center')] for idx, dt in enumerate(r301b)]
                    
                    data_tabs['title'] = check_tab
                    data_tabs['content_table'] = helpers.generate_table(
                        [{'name':'No', 'class' : 'text-center'}, {'name':'Bukti Kepemilikan Tanah Bangunan', 'class' : ''}, {'name':'Jumlah Keluarga', 'class' : 'text-center'}],
                        data
                    )

                    return JsonResponse({"status": 'success', 'content' : data_tabs }, status=200)
                elif tab_request == 11:
                    r307b = models.FamiliesModels.r307b.field.choices
                    model = models.FamiliesModels.objects.aggregate(
                        section1 =Count('r307b', filter=Q(r307b='1')),
                        section2 =Count('r307b', filter=Q(r307b='2')),
                        section3 =Count('r307b', filter=Q(r307b='3')),
                        section4 =Count('r307b', filter=Q(r307b='4')),
                        section5 =Count('r307b', filter=Q(r307b='5'))
                    )
                    model = list(model.values())
                    data = [[(idx+1, 'text-center'), (dt[1], 'text-left'), (model[idx], 'text-center')] for idx, dt in enumerate(r307b)]
                    
                    data_tabs['title'] = check_tab
                    data_tabs['content_table'] = helpers.generate_table(
                        [{'name':'No', 'class' : 'text-center'}, {'name':'Daya Listrik Terpasang', 'class' : ''}, {'name':'Jumlah Keluarga', 'class' : 'text-center'}],
                        data
                    )

                    return JsonResponse({"status": 'success', 'content' : data_tabs }, status=200)
                elif tab_request == 9:

                    r306b = models.FamiliesModels.r306b.field.choices
                    model = models.FamiliesModels.objects.aggregate(
                        section1 =Count('r306b', filter=Q(r306b='1')),
                        section2 =Count('r306b', filter=Q(r306b='2')),
                        section3 =Count('r306b', filter=Q(r306b='8')),
                    )
                    model = list(model.values())
                    data = [[(idx+1, 'text-center'), (dt[1], 'text-left'), (model[idx], 'text-center')] for idx, dt in enumerate(r306b)]

                    data_tabs['title'] = check_tab
                    data_tabs['content_table'] = helpers.generate_table(
                        [{'name':'No', 'class' : 'text-center'}, {'name':'Jarak Sumber Minum dengan Penampungan Limbah', 'class' : ''}, {'name':'Jumlah Keluarga', 'class' : 'text-center'}],
                        data
                    )

                    return JsonResponse({"status": 'success', 'content' : data_tabs }, status=200)
                elif tab_request == 7:
                    r305 = models.FamiliesModels.r305.field.choices
                    model = models.FamiliesModels.objects.aggregate(
                        section1 =Count('r305', filter=Q(r305='1')),
                        section2 =Count('r305', filter=Q(r305='2')),
                        section3 =Count('r305', filter=Q(r305='3')),
                        section4 =Count('r305', filter=Q(r305='4')),
                        section5 =Count('r305', filter=Q(r305='5')),
                        section6 =Count('r305', filter=Q(r305='6')),
                        section7 =Count('r305', filter=Q(r305='7')),
                        section8 =Count('r305', filter=Q(r305='8')),
                    )
                    model = list(model.values())
                    data = [[(idx+1, 'text-center'), (dt[1], 'text-left'), (model[idx], 'text-center')] for idx, dt in enumerate(r305)]

                    data_tabs['title'] = check_tab
                    data_tabs['content_table'] = helpers.generate_table(
                        [{'name':'No', 'class' : 'text-center'}, {'name':'Jenis Atap Terluas', 'class' : ''}, {'name':'Jumlah Keluarga', 'class' : 'text-center'}],
                        data
                    )

                    return JsonResponse({"status": 'success', 'content' : data_tabs }, status=200)
                elif tab_request == 6:
                    r304 = models.FamiliesModels.r304.field.choices
                    model = models.FamiliesModels.objects.aggregate(
                        section1 =Count('r304', filter=Q(r304='1')),
                        section2 =Count('r304', filter=Q(r304='2')),
                        section3 =Count('r304', filter=Q(r304='3')),
                        section4 =Count('r304', filter=Q(r304='4')),
                        section5 =Count('r304', filter=Q(r304='5')),
                        section6 =Count('r304', filter=Q(r304='6')),
                        section7 =Count('r304', filter=Q(r304='7'))
                    )
                    model = list(model.values())
                    data = [[(idx+1, 'text-center'), (dt[1], 'text-left'), (model[idx], 'text-center')] for idx, dt in enumerate(r304)]

                    data_tabs['title'] = check_tab
                    data_tabs['content_table'] = helpers.generate_table(
                        [{'name':'No', 'class' : 'text-center'}, {'name':'Jenis Dinding Terluas', 'class' : ''}, {'name':'Jumlah Keluarga', 'class' : 'text-center'}],
                        data
                    )

                    return JsonResponse({"status": 'success', 'content' : data_tabs }, status=200)
                elif tab_request == 1:
                    r415 = models.PopulationsModels.r415.field.choices
                    model = models.FamiliesModels.objects.filter(families_members__r409 = '1').aggregate(
                        section1 =Count('families_members__r415', filter=Q(families_members__r415='1')),
                        section2 =Count('families_members__r415', filter=Q(families_members__r415='2')),
                        section3 =Count('families_members__r415', filter=Q(families_members__r415='3')),
                        section4 =Count('families_members__r415', filter=Q(families_members__r415='4')),
                        section5 =Count('families_members__r415', filter=Q(families_members__r415='5')),
                        section6 =Count('families_members__r415', filter=Q(families_members__r415='6')),
                        section7 =Count('families_members__r415', filter=Q(families_members__r415='7')),
                        section8 =Count('families_members__r415', filter=Q(families_members__r415='8')),
                        section9 =Count('families_members__r415', filter=Q(families_members__r415='9')),
                        section10 =Count('families_members__r415', filter=Q(families_members__r415='10')),
                        section11 =Count('families_members__r415', filter=Q(families_members__r415='11')),
                        section12 =Count('families_members__r415', filter=Q(families_members__r415='12')),
                        section13 =Count('families_members__r415', filter=Q(families_members__r415='13')),
                        section14 =Count('families_members__r415', filter=Q(families_members__r415='14')),
                        section15 =Count('families_members__r415', filter=Q(families_members__r415='15')),
                        section16 =Count('families_members__r415', filter=Q(families_members__r415='16')),
                        section17 =Count('families_members__r415', filter=Q(families_members__r415='17')),
                        section18 =Count('families_members__r415', filter=Q(families_members__r415='18')),
                        section19 =Count('families_members__r415', filter=Q(families_members__r415='19')),
                        section20 =Count('families_members__r415', filter=Q(families_members__r415='20')),
                        section21 =Count('families_members__r415', filter=Q(families_members__r415='21')),
                        section22 =Count('families_members__r415', filter=Q(families_members__r415='22')),
                        section23 =Count('families_members__r415', filter=Q(families_members__r415='23')),
                    )
                    model = list(model.values())

                    data = [[(idx+1, 'text-center'), (dt[1], 'text-left'), (model[idx], 'text-center')] for idx, dt in enumerate(r415)]

                    data_tabs['title'] = check_tab
                    data_tabs['content_table'] = helpers.generate_table(
                        [{'name':'No', 'class' : 'text-center'}, {'name':'Jenjang Pendidikan Tertinggi KRT', 'class' : ''}, {'name':'Jumlah Keluarga', 'class' : 'text-center'}],
                        data
                    )

                    return JsonResponse({"status": 'success', 'content' : data_tabs }, status=200)
                elif tab_request == 2:
                    r301a = models.FamiliesModels.r301a.field.choices
                    model = models.FamiliesModels.objects.aggregate(
                        section1 =Count('r301a', filter=Q(r301a='1')),
                        section2 =Count('r301a', filter=Q(r301a='2')),
                        section3 =Count('r301a', filter=Q(r301a='3')),
                        section4 =Count('r301a', filter=Q(r301a='4')),
                        section5 =Count('r301a', filter=Q(r301a='5')),
                    )
                    model = list(model.values())
                    data = [[(idx+1, 'text-center'), (dt[1], 'text-left'), (model[idx], 'text-center')] for idx, dt in enumerate(r301a)]

                    data_tabs['title'] = check_tab
                    data_tabs['content_table'] = helpers.generate_table(
                        [{'name':'No', 'class' : 'text-center'}, {'name':'Status Kepemilikan Bangunan Tempat Tinggal', 'class' : ''}, {'name':'Jumlah Keluarga', 'class' : 'text-center'}],
                        data
                    )

                    return JsonResponse({"status": 'success', 'content' : data_tabs }, status=200)
                elif tab_request == 5:
                    r303 = models.FamiliesModels.r303.field.choices
                    model = models.FamiliesModels.objects.aggregate(
                        section1 =Count('r303', filter=Q(r303='1')),
                        section2 =Count('r303', filter=Q(r303='2')),
                        section3 =Count('r303', filter=Q(r303='3')),
                        section4 =Count('r303', filter=Q(r303='4')),
                        section5 =Count('r303', filter=Q(r303='5')),
                        section6 =Count('r303', filter=Q(r303='6')),
                        section7 =Count('r303', filter=Q(r303='7')),
                        section8 =Count('r303', filter=Q(r303='8')),
                        section9 =Count('r303', filter=Q(r303='9')),
                    )
                    model = list(model.values())
                    data = [[(idx+1, 'text-center'), (dt[1], 'text-left'), (model[idx], 'text-center')] for idx, dt in enumerate(r303)]

                    data_tabs['title'] = check_tab
                    data_tabs['content_table'] = helpers.generate_table(
                        [{'name':'No', 'class' : 'text-center'}, {'name':'Jenis Lantai Terluas', 'class' : ''}, {'name':'Jumlah Keluarga', 'class' : 'text-center'}],
                        data
                    )
                    return JsonResponse({"status": 'success', 'content' : data_tabs }, status=200)
                elif tab_request == 8:
                    r306a = models.FamiliesModels.r306a.field.choices
                    model = models.FamiliesModels.objects.aggregate(
                        section1 =Count('r306a', filter=Q(r306a='1')),
                        section2 =Count('r306a', filter=Q(r306a='2')),
                        section3 =Count('r306a', filter=Q(r306a='3')),
                        section4 =Count('r306a', filter=Q(r306a='4')),
                        section5 =Count('r306a', filter=Q(r306a='5')),
                        section6 =Count('r306a', filter=Q(r306a='6')),
                        section7 =Count('r306a', filter=Q(r306a='7')),
                        section8 =Count('r306a', filter=Q(r306a='8')),
                        section9 =Count('r306a', filter=Q(r306a='9')),
                        section10 =Count('r306a', filter=Q(r306a='10')),
                        section11 =Count('r306a', filter=Q(r306a='11')),
                    )
                    model = list(model.values())
                    data = [[(idx+1, 'text-center'), (dt[1], 'text-left'), (model[idx], 'text-center')] for idx, dt in enumerate(r306a)]

                    data_tabs['title'] = check_tab
                    data_tabs['content_table'] = helpers.generate_table(
                        [{'name':'No', 'class' : 'text-center'}, {'name':'Sumber Air Minum Utama', 'class' : ''}, {'name':'Jumlah Keluarga', 'class' : 'text-center'}],
                        data
                    )
                    return JsonResponse({"status": 'success', 'content' : data_tabs }, status=200)
                elif tab_request == 10:
                    r307a = models.FamiliesModels.r307a.field.choices
                    model = models.FamiliesModels.objects.aggregate(
                        section1 =Count('r307a', filter=Q(r307a='1')),
                        section2 =Count('r307a', filter=Q(r307a='2')),
                        section3 =Count('r307a', filter=Q(r307a='3')),
                        section4 =Count('r307a', filter=Q(r307a='4')),
                    )
                    model = list(model.values())
                    data = [[(idx+1, 'text-center'), (dt[1], 'text-left'), (model[idx], 'text-center')] for idx, dt in enumerate(r307a)]

                    data_tabs['title'] = check_tab
                    data_tabs['content_table'] = helpers.generate_table(
                        [{'name':'No', 'class' : 'text-center'}, {'name':'Sumber Penerangan Utama', 'class' : ''}, {'name':'Jumlah Keluarga', 'class' : 'text-center'}],
                        data
                    )
                    return JsonResponse({"status": 'success', 'content' : data_tabs }, status=200)
                elif tab_request == 13:
                    r309a = models.FamiliesModels.r309a.field.choices
                    model = models.FamiliesModels.objects.aggregate(
                        section1 =Count('r309a', filter=Q(r309a='1')),
                        section2 =Count('r309a', filter=Q(r309a='2')),
                        section3 =Count('r309a', filter=Q(r309a='3')),
                        section4 =Count('r309a', filter=Q(r309a='4')),
                        section5 =Count('r309a', filter=Q(r309a='5')),
                        section6 =Count('r309a', filter=Q(r309a='6')),
                    )
                    model = list(model.values())
                    data = [[(idx+1, 'text-center'), (dt[1], 'text-left'), (model[idx], 'text-center')] for idx, dt in enumerate(r309a)]

                    data_tabs['title'] = check_tab
                    data_tabs['content_table'] = helpers.generate_table(
                        [{'name':'No', 'class' : 'text-center'}, {'name':'Kepemilikan Fasilitas Tempat Buang Air Besar', 'class' : ''}, {'name':'Jumlah Keluarga', 'class' : 'text-center'}],
                        data
                    )
                    return JsonResponse({"status": 'success', 'content' : data_tabs }, status=200)
                elif tab_request == 14:
                    r309b = models.FamiliesModels.r309b.field.choices
                    model = models.FamiliesModels.objects.aggregate(
                        section1 =Count('r309b', filter=Q(r309b='1')),
                        section2 =Count('r309b', filter=Q(r309b='2')),
                        section3 =Count('r309b', filter=Q(r309b='3')),
                        section4 =Count('r309b', filter=Q(r309b='4'))
                    )
                    model = list(model.values())
                    data = [[(idx+1, 'text-center'), (dt[1], 'text-left'), (model[idx], 'text-center')] for idx, dt in enumerate(r309b)]

                    data_tabs['title'] = check_tab
                    data_tabs['content_table'] = helpers.generate_table(
                        [{'name':'No', 'class' : 'text-center'}, {'name':'Jenis Kloset', 'class' : ''}, {'name':'Jumlah Keluarga', 'class' : 'text-center'}],
                        data
                    )
                    return JsonResponse({"status": 'success', 'content' : data_tabs }, status=200)
                elif tab_request == 15:
                    r310 = models.FamiliesModels.r310.field.choices
                    model = models.FamiliesModels.objects.aggregate(
                        section1 =Count('r310', filter=Q(r310='1')),
                        section2 =Count('r310', filter=Q(r310='2')),
                        section3 =Count('r310', filter=Q(r310='3')),
                        section4 =Count('r310', filter=Q(r310='4')),
                        section5 =Count('r310', filter=Q(r310='5')),
                        section6 =Count('r310', filter=Q(r310='6'))
                    )
                    model = list(model.values())
                    data = [[(idx+1, 'text-center'), (dt[1], 'text-left'), (model[idx], 'text-center')] for idx, dt in enumerate(r310)]

                    data_tabs['title'] = check_tab
                    data_tabs['content_table'] = helpers.generate_table(
                        [{'name':'No', 'class' : 'text-center'}, {'name':'Tempat Pembuangan Akhir Tinja', 'class' : ''}, {'name':'Jumlah Keluarga', 'class' : 'text-center'}],
                        data
                    )
                    return JsonResponse({"status": 'success', 'content' : data_tabs }, status=200)
                elif tab_request == 16:
                    r501a = models.FamiliesModels.r501a.field.choices
                    model = models.FamiliesModels.objects.aggregate(
                        section1 =Count('r501a', filter=Q(r501a='1')),
                        section2 =Count('r501a', filter=Q(r501a='2'))
                    )
                    model = list(model.values())
                    data = [[(idx+1, 'text-center'), (dt[1], 'text-left'), (model[idx], 'text-center')] for idx, dt in enumerate(r501a)]

                    data_tabs['title'] = check_tab
                    data_tabs['content_table'] = helpers.generate_table(
                        [{'name':'No', 'class' : 'text-center'}, {'name':'Status Penerimaan Bantuan Sosial Sembako/ BPNT', 'class' : ''}, {'name':'Jumlah Keluarga', 'class' : 'text-center'}],
                        data
                    )
                    return JsonResponse({"status": 'success', 'content' : data_tabs }, status=200)
                elif tab_request == 17:
                    r501b = models.FamiliesModels.r501b.field.choices
                    model = models.FamiliesModels.objects.aggregate(
                        section1 =Count('r501b', filter=Q(r501b='1')),
                        section2 =Count('r501b', filter=Q(r501b='2'))
                    )
                    model = list(model.values())
                    data = [[(idx+1, 'text-center'), (dt[1], 'text-left'), (model[idx], 'text-center')] for idx, dt in enumerate(r501b)]

                    data_tabs['title'] = check_tab
                    data_tabs['content_table'] = helpers.generate_table(
                        [{'name':'No', 'class' : 'text-center'}, {'name':'Status Penerimaan Keluarga Harapan (PKH)', 'class' : ''}, {'name':'Jumlah Keluarga', 'class' : 'text-center'}],
                        data
                    )
                    return JsonResponse({"status": 'success', 'content' : data_tabs }, status=200)
                elif tab_request == 18:
                    r501c = models.FamiliesModels.r501c.field.choices
                    model = models.FamiliesModels.objects.aggregate(
                        section1 =Count('r501c', filter=Q(r501c='1')),
                        section2 =Count('r501c', filter=Q(r501c='2'))
                    )
                    model = list(model.values())
                    data = [[(idx+1, 'text-center'), (dt[1], 'text-left'), (model[idx], 'text-center')] for idx, dt in enumerate(r501c)]

                    data_tabs['title'] = check_tab
                    data_tabs['content_table'] = helpers.generate_table(
                        [{'name':'No', 'class' : 'text-center'}, {'name':'Status Penerimaan Bantuan Langsung Tunai (BLT)', 'class' : ''}, {'name':'Jumlah Keluarga', 'class' : 'text-center'}],
                        data
                    )
                    return JsonResponse({"status": 'success', 'content' : data_tabs }, status=200)
                elif tab_request == 19:
                    r501d = models.FamiliesModels.r501d.field.choices
                    model = models.FamiliesModels.objects.aggregate(
                        section1 =Count('r501d', filter=Q(r501d='1')),
                        section2 =Count('r501d', filter=Q(r501d='2'))
                    )
                    model = list(model.values())
                    data = [[(idx+1, 'text-center'), (dt[1], 'text-left'), (model[idx], 'text-center')] for idx, dt in enumerate(r501d)]

                    data_tabs['title'] = check_tab
                    data_tabs['content_table'] = helpers.generate_table(
                        [{'name':'No', 'class' : 'text-center'}, {'name':'Status Penerimaan Subsidi Listrik', 'class' : ''}, {'name':'Jumlah Keluarga', 'class' : 'text-center'}],
                        data
                    )
                    return JsonResponse({"status": 'success', 'content' : data_tabs }, status=200)
                elif tab_request == 20:
                    r501e = models.FamiliesModels.r501e.field.choices
                    model = models.FamiliesModels.objects.aggregate(
                        section1 =Count('r501e', filter=Q(r501e='1')),
                        section2 =Count('r501e', filter=Q(r501e='2'))
                    )
                    model = list(model.values())
                    data = [[(idx+1, 'text-center'), (dt[1], 'text-left'), (model[idx], 'text-center')] for idx, dt in enumerate(r501e)]

                    data_tabs['title'] = check_tab
                    data_tabs['content_table'] = helpers.generate_table(
                        [{'name':'No', 'class' : 'text-center'}, {'name':'Status Penerimaan Bantuan Pemerintah Daerah', 'class' : ''}, {'name':'Jumlah Keluarga', 'class' : 'text-center'}],
                        data
                    )
                    return JsonResponse({"status": 'success', 'content' : data_tabs }, status=200)
                elif tab_request == 21:
                    r501f = models.FamiliesModels.r501f.field.choices
                    model = models.FamiliesModels.objects.aggregate(
                        section1 =Count('r501f', filter=Q(r501f='1')),
                        section2 =Count('r501f', filter=Q(r501f='2'))
                    )
                    model = list(model.values())
                    data = [[(idx+1, 'text-center'), (dt[1], 'text-left'), (model[idx], 'text-center')] for idx, dt in enumerate(r501f)]

                    data_tabs['title'] = check_tab
                    data_tabs['content_table'] = helpers.generate_table(
                        [{'name':'No', 'class' : 'text-center'}, {'name':'Status Penerimaan Subsidi Pupuk', 'class' : ''}, {'name':'Jumlah Keluarga', 'class' : 'text-center'}],
                        data
                    )
                    return JsonResponse({"status": 'success', 'content' : data_tabs }, status=200)
                elif tab_request == 22:
                    r501g = models.FamiliesModels.r501g.field.choices
                    model = models.FamiliesModels.objects.aggregate(
                        section1 =Count('r501g', filter=Q(r501g='1')),
                        section2 =Count('r501g', filter=Q(r501g='2'))
                    )
                    model = list(model.values())
                    data = [[(idx+1, 'text-center'), (dt[1], 'text-left'), (model[idx], 'text-center')] for idx, dt in enumerate(r501g)]

                    data_tabs['title'] = check_tab
                    data_tabs['content_table'] = helpers.generate_table(
                        [{'name':'No', 'class' : 'text-center'}, {'name':'Status Penerimaan Subsidi LPG', 'class' : ''}, {'name':'Jumlah Keluarga', 'class' : 'text-center'}],
                        data
                    )
                    return JsonResponse({"status": 'success', 'content' : data_tabs }, status=200)
                elif tab_request == 23:
                    r502a = models.FamiliesModels.r502a.field.choices
                    model = models.FamiliesModels.objects.aggregate(
                        section1 =Count('r502a', filter=Q(r502a='1')),
                        section2 =Count('r502a', filter=Q(r502a='2'))
                    )
                    model = list(model.values())
                    data = [[(idx+1, 'text-center'), (dt[1], 'text-left'), (model[idx], 'text-center')] for idx, dt in enumerate(r502a)]

                    data_tabs['title'] = check_tab
                    data_tabs['content_table'] = helpers.generate_table(
                        [{'name':'No', 'class' : 'text-center'}, {'name':'Status Kepemilikan Tabung gas >= 5,5 kg', 'class' : ''}, {'name':'Jumlah Keluarga', 'class' : 'text-center'}],
                        data
                    )
                    return JsonResponse({"status": 'success', 'content' : data_tabs }, status=200)
                elif tab_request == 24:
                    r502b = models.FamiliesModels.r502b.field.choices
                    model = models.FamiliesModels.objects.aggregate(
                        section1 =Count('r502b', filter=Q(r502b='1')),
                        section2 =Count('r502b', filter=Q(r502b='2'))
                    )
                    model = list(model.values())
                    data = [[(idx+1, 'text-center'), (dt[1], 'text-left'), (model[idx], 'text-center')] for idx, dt in enumerate(r502b)]

                    data_tabs['title'] = check_tab
                    data_tabs['content_table'] = helpers.generate_table(
                        [{'name':'No', 'class' : 'text-center'}, {'name':'Status Kepemilikan Lemari Es/Kulkas', 'class' : ''}, {'name':'Jumlah Keluarga', 'class' : 'text-center'}],
                        data
                    )
                    return JsonResponse({"status": 'success', 'content' : data_tabs }, status=200)
                elif tab_request == 25:
                    r502c = models.FamiliesModels.r502c.field.choices
                    model = models.FamiliesModels.objects.aggregate(
                        section1 =Count('r502c', filter=Q(r502c='1')),
                        section2 =Count('r502c', filter=Q(r502c='2'))
                    )
                    model = list(model.values())
                    data = [[(idx+1, 'text-center'), (dt[1], 'text-left'), (model[idx], 'text-center')] for idx, dt in enumerate(r502c)]

                    data_tabs['title'] = check_tab
                    data_tabs['content_table'] = helpers.generate_table(
                        [{'name':'No', 'class' : 'text-center'}, {'name':'Status Kepemilikan Air Conditioner (AC)', 'class' : ''}, {'name':'Jumlah Keluarga', 'class' : 'text-center'}],
                        data
                    )
                    return JsonResponse({"status": 'success', 'content' : data_tabs }, status=200)
                elif tab_request == 26:
                    r502d = models.FamiliesModels.r502d.field.choices
                    model = models.FamiliesModels.objects.aggregate(
                        section1 =Count('r502d', filter=Q(r502d='1')),
                        section2 =Count('r502d', filter=Q(r502d='2'))
                    )
                    model = list(model.values())
                    data = [[(idx+1, 'text-center'), (dt[1], 'text-left'), (model[idx], 'text-center')] for idx, dt in enumerate(r502d)]

                    data_tabs['title'] = check_tab
                    data_tabs['content_table'] = helpers.generate_table(
                        [{'name':'No', 'class' : 'text-center'}, {'name':'Status Kepemilikan Pemanas Air (Water Heater)', 'class' : ''}, {'name':'Jumlah Keluarga', 'class' : 'text-center'}],
                        data
                    )
                    return JsonResponse({"status": 'success', 'content' : data_tabs }, status=200)
                elif tab_request == 27:
                    r502e = models.FamiliesModels.r502e.field.choices
                    model = models.FamiliesModels.objects.aggregate(
                        section1 =Count('r502e', filter=Q(r502e='1')),
                        section2 =Count('r502e', filter=Q(r502e='2'))
                    )
                    model = list(model.values())
                    data = [[(idx+1, 'text-center'), (dt[1], 'text-left'), (model[idx], 'text-center')] for idx, dt in enumerate(r502e)]

                    data_tabs['title'] = check_tab
                    data_tabs['content_table'] = helpers.generate_table(
                        [{'name':'No', 'class' : 'text-center'}, {'name':'Status Kepemilikan Telepon Rumah', 'class' : ''}, {'name':'Jumlah Keluarga', 'class' : 'text-center'}],
                        data
                    )
                    return JsonResponse({"status": 'success', 'content' : data_tabs }, status=200)
                elif tab_request == 28:
                    r502f = models.FamiliesModels.r502f.field.choices
                    model = models.FamiliesModels.objects.aggregate(
                        section1 =Count('r502f', filter=Q(r502f='1')),
                        section2 =Count('r502f', filter=Q(r502f='2'))
                    )
                    model = list(model.values())
                    data = [[(idx+1, 'text-center'), (dt[1], 'text-left'), (model[idx], 'text-center')] for idx, dt in enumerate(r502f)]

                    data_tabs['title'] = check_tab
                    data_tabs['content_table'] = helpers.generate_table(
                        [{'name':'No', 'class' : 'text-center'}, {'name':'Status Kepemilikan Televisi Layar Datar (Min. 30 Inchi)', 'class' : ''}, {'name':'Jumlah Keluarga', 'class' : 'text-center'}],
                        data
                    )
                    return JsonResponse({"status": 'success', 'content' : data_tabs }, status=200)
                elif tab_request == 29:
                    r502g = models.FamiliesModels.r502g.field.choices
                    model = models.FamiliesModels.objects.aggregate(
                        section1 =Count('r502g', filter=Q(r502g='1')),
                        section2 =Count('r502g', filter=Q(r502g='2'))
                    )
                    model = list(model.values())
                    data = [[(idx+1, 'text-center'), (dt[1], 'text-left'), (model[idx], 'text-center')] for idx, dt in enumerate(r502g)]

                    data_tabs['title'] = check_tab
                    data_tabs['content_table'] = helpers.generate_table(
                        [{'name':'No', 'class' : 'text-center'}, {'name':'Status Kepemilikan Emas/Perhiasan (Min. 10 gram)', 'class' : ''}, {'name':'Jumlah Keluarga', 'class' : 'text-center'}],
                        data
                    )
                    return JsonResponse({"status": 'success', 'content' : data_tabs }, status=200)
                elif tab_request == 30:
                    r502h = models.FamiliesModels.r502h.field.choices
                    model = models.FamiliesModels.objects.aggregate(
                        section1 =Count('r502h', filter=Q(r502h='1')),
                        section2 =Count('r502h', filter=Q(r502h='2'))
                    )
                    model = list(model.values())
                    data = [[(idx+1, 'text-center'), (dt[1], 'text-left'), (model[idx], 'text-center')] for idx, dt in enumerate(r502h)]

                    data_tabs['title'] = check_tab
                    data_tabs['content_table'] = helpers.generate_table(
                        [{'name':'No', 'class' : 'text-center'}, {'name':'Status Kepemilikan Komputer/Laptop/Tablet', 'class' : ''}, {'name':'Jumlah Keluarga', 'class' : 'text-center'}],
                        data
                    )
                    return JsonResponse({"status": 'success', 'content' : data_tabs }, status=200)
                elif tab_request == 31:
                    r502i = models.FamiliesModels.r502i.field.choices
                    model = models.FamiliesModels.objects.aggregate(
                        section1 =Count('r502i', filter=Q(r502i='1')),
                        section2 =Count('r502i', filter=Q(r502i='2'))
                    )
                    model = list(model.values())
                    data = [[(idx+1, 'text-center'), (dt[1], 'text-left'), (model[idx], 'text-center')] for idx, dt in enumerate(r502i)]

                    data_tabs['title'] = check_tab
                    data_tabs['content_table'] = helpers.generate_table(
                        [{'name':'No', 'class' : 'text-center'}, {'name':'Status Kepemilikan Sepeda Motor', 'class' : ''}, {'name':'Jumlah Keluarga', 'class' : 'text-center'}],
                        data
                    )
                    return JsonResponse({"status": 'success', 'content' : data_tabs }, status=200)
                elif tab_request == 32:
                    r502k = models.FamiliesModels.r502k.field.choices
                    model = models.FamiliesModels.objects.aggregate(
                        section1 =Count('r502k', filter=Q(r502k='1')),
                        section2 =Count('r502k', filter=Q(r502k='2'))
                    )
                    model = list(model.values())
                    data = [[(idx+1, 'text-center'), (dt[1], 'text-left'), (model[idx], 'text-center')] for idx, dt in enumerate(r502k)]

                    data_tabs['title'] = check_tab
                    data_tabs['content_table'] = helpers.generate_table(
                        [{'name':'No', 'class' : 'text-center'}, {'name':'Status Kepemilikan Mobil', 'class' : ''}, {'name':'Jumlah Keluarga', 'class' : 'text-center'}],
                        data
                    )
                    return JsonResponse({"status": 'success', 'content' : data_tabs }, status=200)
                elif tab_request == 33:
                    r503a = models.FamiliesModels.r503a.field.choices
                    model = models.FamiliesModels.objects.aggregate(
                        section1 =Count('r503a', filter=Q(r503a='1')),
                        section2 =Count('r503a', filter=Q(r503a='2'))
                    )
                    model = list(model.values())
                    data = [[(idx+1, 'text-center'), (dt[1], 'text-left'), (model[idx], 'text-center')] for idx, dt in enumerate(r503a)]

                    data_tabs['title'] = check_tab
                    data_tabs['content_table'] = helpers.generate_table(
                        [{'name':'No', 'class' : 'text-center'}, {'name':'Status Kepemilikan Aset Lahan', 'class' : ''}, {'name':'Jumlah Keluarga', 'class' : 'text-center'}],
                        data
                    )
                    return JsonResponse({"status": 'success', 'content' : data_tabs }, status=200)
                elif tab_request == 34:
                    r503b = models.FamiliesModels.r503b.field.choices
                    model = models.FamiliesModels.objects.aggregate(
                        section1 =Count('r503b', filter=Q(r503b='1')),
                        section2 =Count('r503b', filter=Q(r503b='2'))
                    )
                    model = list(model.values())
                    data = [[(idx+1, 'text-center'), (dt[1], 'text-left'), (model[idx], 'text-center')] for idx, dt in enumerate(r503b)]

                    data_tabs['title'] = check_tab
                    data_tabs['content_table'] = helpers.generate_table(
                        [{'name':'No', 'class' : 'text-center'}, {'name':'Status Kepemilikan Aset Lahan', 'class' : ''}, {'name':'Jumlah Keluarga', 'class' : 'text-center'}],
                        data
                    )
                    return JsonResponse({"status": 'success', 'content' : data_tabs }, status=200)
                elif tab_request == 35:
                    model_count = models.FamiliesModels.objects.aggregate(
                        section1 = Count('r504a', filter=Q(r504a__gt =0)),
                        section2 = Count('r504b', filter=Q(r504b__gt =0)),
                        section3 = Count('r504c', filter=Q(r504c__gt =0)),
                        section4 = Count('r504d', filter=Q(r504d__gt =0)),
                        section5 = Count('r504e', filter=Q(r504e__gt =0))
                    )
                    model_count = list(model_count.values())

                    model_sum = models.FamiliesModels.objects.aggregate(
                        section1 = Sum('r504a', filter=Q(r504a__gt =0)),
                        section2 = Sum('r504b', filter=Q(r504b__gt =0)),
                        section3 = Sum('r504c', filter=Q(r504c__gt =0)),
                        section4 = Sum('r504d', filter=Q(r504d__gt =0)),
                        section5 = Sum('r504e', filter=Q(r504e__gt =0))
                    )
                    model_sum = list(model_sum.values())

                    data_header = [
                        {'name':'No', 'class' : 'text-center'}, 
                        {'name':'Kepemilikan Hewan Ternak', 'class' : 'text-left'}, 
                        {'name':'Banyaknya Keluarga', 'class' : 'text-center'},
                        {'name':'Jumlah Hewan (Ekor)', 'class' : 'text-center'}
                    ]

                    data_body = [
                        [(1, 'text-center'), ('Sapi', 'text-left'), (model_count[0], 'text-center'),  (model_sum[0] if model_sum[0] is not None else 0, 'text-center')],
                        [(2, 'text-center'), ('Kerbau', 'text-left'), (model_count[1], 'text-center'),  (model_sum[1] if model_sum[1] is not None else 0, 'text-center')],
                        [(3, 'text-center'), ('Kuda', 'text-left'), (model_count[2], 'text-center'),  (model_sum[2] if model_sum[2] is not None else 0, 'text-center')],
                        [(4, 'text-center'), ('Babi', 'text-left'), (model_count[3], 'text-center'),  (model_sum[3] if model_sum[3] is not None else 0, 'text-center')],
                        [(5, 'text-center'), ('Kambing/Domba', 'text-left'), (model_count[4], 'text-center'),  (model_sum[4] if model_sum[4] is not None else 0, 'text-center')],
                    ]

                    data_tabs['title'] = check_tab
                    data_tabs['content_table'] = helpers.generate_table(
                        data_header,
                        data_body
                    )
                    return JsonResponse({"status": 'success', 'content' : data_tabs }, status=200)
                elif tab_request == 36:
                    r506 = models.FamiliesModels.r506.field.choices
                    model = models.FamiliesModels.objects.aggregate(
                        section1 =Count('r506', filter=Q(r506='1')),
                        section2 =Count('r506', filter=Q(r506='2')),
                        section3 =Count('r506', filter=Q(r506='3')),
                        section4 =Count('r506', filter=Q(r506='4'))
                    )
                    model = list(model.values())
                    data = [[(idx+1, 'text-center'), (dt[1], 'text-left'), (model[idx], 'text-center')] for idx, dt in enumerate(r506)]

                    data_tabs['title'] = check_tab
                    data_tabs['content_table'] = helpers.generate_table(
                        [{'name':'No', 'class' : 'text-center'}, {'name':'Status Kepemilikan Rekening Aktif', 'class' : ''}, {'name':'Jumlah Keluarga', 'class' : 'text-center'}],
                        data
                    )
                    return JsonResponse({"status": 'success', 'content' : data_tabs }, status=200)
        return JsonResponse({'status': 'Invalid request'}, status=400)


class TabulationsPopulationsClassView(LoginRequiredMixin, View):
    
    def get(self, request):

        populations = models.PopulationsModels.objects.all().count()
        # labor_force = models.PopulationsModels.objects.filter(
        #     Q(r407__gte = 15) & Q(r407__lte = 64) 
        # ).filter(
        #     (Q(r416a = 1) & ~Q(r416b = 0)) |
        #     (Q(r420a = 1) & ~Q(r422_23 = 0))
        # ).count()

        # jamkes = models.PopulationsModels.objects.filter(r431a__in = ['1', '2', '4', '8']).count()
        # penyakit_kronis = models.PopulationsModels.objects.filter(~Q(r430 = '01')).count()

        education_levels = models.PopulationsModels.r518.field.choices
        home_ownership_state = models.FamiliesModels.r301.field.choices

        # tabulations = helpers.get_tab_populations()
        context = {
            'title' : 'Tabulasi Data Penduduk',
            'populations' : populations,
            # 'labor_force' : labor_force,
            # 'jamkes' : jamkes,
            # 'penyakit_kronis': penyakit_kronis,
            'education_levels' : education_levels,
            'home_ownership_state' : home_ownership_state,
            # 'tabulations' : tabulations
        }
        return render(request, 'app/tabulasi/tabulasi-penduduk.html', context)


class TabulationsPopulationsFetchClassView(LoginRequiredMixin, View):

    def post(self, request):
        is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
        if is_ajax:
            if request.method == 'POST':
                tabs = helpers.get_tab_populations()
                tab_request = int(request.POST.get('tab_request'))
                check_tab = next((d['text'] for (index, d) in enumerate(tabs) if d['val'] == tab_request), None)
                if check_tab is None:
                    return JsonResponse({"status": 'failed'}, status=400)
                
                data_tabs = {}
                if tab_request == 1:
                    pass
                elif tab_request == 2:
                    r408 = models.PopulationsModels.r408.field.choices
                    model = models.PopulationsModels.objects.aggregate(
                        section1 =Count('r408', filter=Q(r408='1')),
                        section2 =Count('r408', filter=Q(r408='2')),
                        section3 =Count('r408', filter=Q(r408='3')),
                        section4 =Count('r408', filter=Q(r408='4')),
                    )
                    model = list(model.values())
                    data = [[(idx+1, 'text-center'), (dt[1], 'text-left'), (model[idx], 'text-center')] for idx, dt in enumerate(r408)]
                    
                    data_tabs['title'] = check_tab
                    data_tabs['content_table'] = helpers.generate_table(
                        [{'name':'No', 'class' : 'text-center'}, {'name':'Status Perkawinan', 'class' : ''}, {'name':'Jumlah Keluarga', 'class' : 'text-center'}],
                        data
                    )

                    return JsonResponse({"status": 'success', 'content' : data_tabs }, status=200)
                elif tab_request == 3:
                    r416a = models.PopulationsModels.r416a.field.choices
                    model = models.PopulationsModels.objects.aggregate(
                        section1 =Count('r416a', filter=Q(r416a='1')),
                        section2 =Count('r416a', filter=Q(r416a='2'))
                    )
                    model = list(model.values())
                    data = [[(idx+1, 'text-center'), (dt[1], 'text-left'), (model[idx], 'text-center')] for idx, dt in enumerate(r416a)]
                    
                    data_tabs['title'] = check_tab
                    data_tabs['content_table'] = helpers.generate_table(
                        [{'name':'No', 'class' : 'text-center'}, {'name':'Status Bekerja', 'class' : ''}, {'name':'Jumlah Keluarga', 'class' : 'text-center'}],
                        data
                    )

                    return JsonResponse({"status": 'success', 'content' : data_tabs }, status=200)
                elif tab_request == 7:
                    r420a = models.PopulationsModels.r420a.field.choices
                    model = models.PopulationsModels.objects.aggregate(
                        section1 =Count('r420a', filter=Q(r420a='1')),
                        section2 =Count('r420a', filter=Q(r420a='2'))
                    )
                    model = list(model.values())
                    data = [[(idx+1, 'text-center'), (dt[1], 'text-left'), (model[idx], 'text-center')] for idx, dt in enumerate(r420a)]
                    
                    data_tabs['title'] = check_tab
                    data_tabs['content_table'] = helpers.generate_table(
                        [{'name':'No', 'class' : 'text-center'}, {'name':'Status Berusaha', 'class' : ''}, {'name':'Jumlah Keluarga', 'class' : 'text-center'}],
                        data
                    )
                    return JsonResponse({"status": 'success', 'content' : data_tabs }, status=200)
                elif tab_request == 4:
                    pass
                elif tab_request == 5:
                    pass
                elif tab_request == 6:
                   pass
                elif tab_request == 8:
                    pass
                elif tab_request == 9:
                    pass
                elif tab_request == 10:
                   pass
                elif tab_request == 11:
                    r430 = models.PopulationsModels.r430.field.choices
                    model = models.PopulationsModels.objects.aggregate(
                        section1 =Count('r430', filter=Q(r430='1')),
                        section2 =Count('r430', filter=Q(r430='2')),
                        section3 =Count('r430', filter=Q(r430='3')),
                        section4 =Count('r430', filter=Q(r430='4')),
                        section5 =Count('r430', filter=Q(r430='5')),
                        section6 =Count('r430', filter=Q(r430='6')),
                        section7 =Count('r430', filter=Q(r430='7')),
                        section8 =Count('r430', filter=Q(r430='8')),
                        section9 =Count('r430', filter=Q(r430='9')),
                        section10 =Count('r430', filter=Q(r430='10')),
                        section11 =Count('r430', filter=Q(r430='11')),
                        section12 =Count('r430', filter=Q(r430='12')),
                        section13 =Count('r430', filter=Q(r430='13')),
                        section14 =Count('r430', filter=Q(r430='14')),
                        section15 =Count('r430', filter=Q(r430='15')),
                        section16 =Count('r430', filter=Q(r430='16')),
                        section17 =Count('r430', filter=Q(r430='17')),
                        section18 =Count('r430', filter=Q(r430='18')),
                    )
                    model = list(model.values())
                    data = [[(idx+1, 'text-center'), (dt[1], 'text-left'), (model[idx], 'text-center')] for idx, dt in enumerate(r430)]

                    data_tabs['title'] = check_tab
                    data_tabs['content_table'] = helpers.generate_table(
                        [{'name':'No', 'class' : 'text-center'}, {'name':'Keluhan Kesehatan Kronis/Menahun', 'class' : ''}, {'name':'Jumlah Keluarga', 'class' : 'text-center'}],
                        data
                    )
                    return JsonResponse({"status": 'success', 'content' : data_tabs }, status=200)

        return JsonResponse({'status': 'Invalid request'}, status=400)


class ManajemenFamiliesClassView(LoginRequiredMixin, View):
    
    def get(self, request):

        families = models.FamiliesModels.objects.all()
        education_levels = models.PopulationsModels.r518.field.choices
        home_ownership_state = models.FamiliesModels.r301.field.choices
        
        data_families = []
        for family in families:
            dt = {}
            dt['id'] = family.pk
            dt['r108'] = family.r108
            dt['r112'] = family.r112
            dt['r104'] = f"{family.r104.reg_name}, {family.r105.reg_sls_name}"

            members = models.PopulationsModels.objects.filter(family_id = family.pk, r409 = '2' )
            if members.exists():
                dt['r108'] = f"{dt['r108']} / { members.first().r402}"

            welf = '<select class="form-select" style="width:70%">'
            if family.r501a == '1':
                welf += '<option>BPNT</option>'
            if family.r501b == '1':
                welf += '<option>PKH</option>'
            if family.r501c == '1':
                welf += '<option>BLT</option>'
            if family.r501d == '1':
                welf += '<option>Subsidi Listrik</option>'
            if family.r501e == '1':
                welf += '<option>Bantuan Pemda</option>'
            if family.r501f == '1':
                welf += '<option>Subsidi Pupuk</option>'
            if family.r501g == '1':
                welf += '<option>Subsidi LPG</option>'
            welf += '</select>'

            if welf.find('<option>') != -1:
                dt['welf'] = welf
            else:
                dt['welf'] = 'Bukan penerima bantuan'


            assets = '<select class="form-select" style="width:100%">'
            if family.r502a == '1':
                assets += '<option>Tabung Gas >= 5,5 kg</option>'
            if family.r502n == '1':
                assets += '<option>Smartphone</option>'
            if family.r502b == '1':
                assets += '<option>Lemari Es/Kulkas</option>'
            if family.r502c == '1':
                assets += '<option>AC</option>'
            if family.r502d == '1':
                assets += '<option>Water Heater</option>'
            if family.r502e == '1':
                assets += '<option>Telepon Rumah</option>'
            if family.r502f == '1':
                assets += '<option>Televisi Layar Datar</option>'
            if family.r502g == '1':
                assets += '<option>Emas/Perhiasan</option>'
            if family.r502h == '1':
                assets += '<option>Komputer/Laptop/Tablet</option>'
            if family.r502i == '1':
                assets += '<option>Sepeda Motor</option>'
            if family.r502j == '1':
                assets += '<option>Sepeda</option>'
            if family.r502k == '1':
                assets += '<option>Mobil</option>'
            if family.r502l == '1':
                assets += '<option>Perahu</option>'
            if family.r502m == '1':
                assets += '<option>Perahu Motor</option>'

            assets += '</select>'
            if assets.find('<option>') != -1:
                dt['assets'] = assets
            else:
                dt['assets'] = 'Tidak memiliki aset'

            data_families.append(dt)

        context = {
            'title' : 'Manajemen Keluarga',
            'families' : data_families,
            'education_levels' : education_levels,
            'home_ownership_state' : home_ownership_state,
        }

        return render(request, 'app/master/master-keluarga.html', context)

class FamiliesAddClassView(LoginRequiredMixin, View):

    def get(self, request):
        context = {
            'title' : 'Tambah Data Keluarga',
            'form' : forms.FamiliesForm(),
            'form_penduduk' : forms.PopulationsForm(),
            'province_regions' : models.RegionAdministrativeModels.objects.annotate(text_len=Length('reg_code')).filter(text_len=2).order_by('reg_code')
        }
        
        return render(request, 'app/master/master-keluarga-add.html', context)
    
    def post(self, request):
        is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
        if is_ajax:
            if request.method == 'POST':

                data_families = json.loads(request.POST.get('form_families'))
                data_art = json.loads(request.POST.get('form_art'))
                data_art = helpers.transform_data(data_art)
                forms_errors = dict()

                # for fl in ['provinsi', 'kabkot', 'kecamatan']:
                #     if fl in data_families.keys():
                #         if len(data_families[fl]) == 0:
                #             forms_errors[fl] = ['This field is required.']
                #         del data_families[fl]

                # form_family = forms.FamiliesForm(data_families)
                # if form_family.is_valid() is False:
                #     for key, val in form_family.errors.items():
                #         forms_errors[key] = val
                
                # for idx, dt in enumerate(data_art):
                #     form_art = forms.PopulationsForm(dt)
                #     if form_art.is_valid() is False:
                #         for key, val in form_art.errors.items():
                #             if key != 'family_id':
                #                 forms_errors[f'form_art_{key}_{idx+1}'] = val
                
                # if len(forms_errors) > 0:
                #     return JsonResponse({"status": 'failed', "error": forms_errors}, status=400)

                # last_validations = helpers.combine_validations(data_families, data_art)
                
                # if len(last_validations) > 0:
                #     for key, val in last_validations.items():
                #         forms_errors[key] = val
                #     return JsonResponse({"status": 'failed', "error": forms_errors}, status=400)
                
                # form_family.save()
                # last_id = models.FamiliesModels.objects.latest('id').id
                # art_names = ''
                # for idx, dt in enumerate(data_art):
                #     data_art[idx]['family_id'] = last_id
                #     form_art = forms.PopulationsForm(dt)
                #     form_art.save()
                #     art_names += f'<li class="px-2">{idx+1}. {dt["r402"]}</li>'
                
                # msg = f'<ul class="px-0" style="list-style:none">\
                #             Data keluarga dengan ART berhasil ditambahkan: <br>\
                #            {art_names}\
                #         </ul>'
                # return JsonResponse({"status": msg}, status=200)
            
        return JsonResponse({'status': 'Invalid request'}, status=400)

class ManajemenFamiliesDeleteClassView(LoginRequiredMixin, View):

    def post(self, request):
        is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'

        if is_ajax:
            if request.method == 'POST':
                try:
                    data = get_object_or_404(models.FamiliesModels, pk=request.POST.get('pk'))
                    old_dt = data.r108 
                    data.delete()
                    return JsonResponse({'status' : 'success', 'message': f'Keluarga atas nama "{old_dt}" berhasil dihapus.'})
                except:
                    return JsonResponse({'status': 'failed', 'message': 'Data tidak tersedia'})
                
        return JsonResponse({'status': 'Invalid request'}, status=400)
        
class RegionFetchDataClassView(LoginRequiredMixin, View):
        
        def post(self, request):
            is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
            if is_ajax:
                if request.method == 'POST':
                    regency_regs = models.RegionAdministrativeModels.objects.annotate(text_len=Length('reg_code'))
                    if request.POST.get('province_id'):
                        regency_regs = regency_regs.filter(text_len=4).filter(reg_code__icontains=request.POST.get('province_id')).order_by('reg_code').values()
                    elif request.POST.get('regency_id'):
                        regency_regs = regency_regs.filter(text_len=7).filter(reg_code__icontains=request.POST.get('regency_id')).order_by('reg_code').values()
                    elif request.POST.get('district_id'):
                        regency_regs = regency_regs.filter(text_len=10).filter(reg_code__icontains=request.POST.get('district_id')).order_by('reg_code').values()
                    elif request.POST.get('subdistrict_id'):
                        regency_regs = models.RegionSLSModels.objects.filter(reg_code__reg_code = request.POST.get('subdistrict_id')).values()
                    
                    return JsonResponse({"data": list(regency_regs)}, status=200)
            return JsonResponse({'status': 'Invalid request'}, status=400)

class ManajemenPopulationsClassView(LoginRequiredMixin, View): 
        
    def get(self, request):
        education_levels = models.PopulationsModels.r415.field.choices
        home_ownership_state = models.FamiliesModels.r301a.field.choices
        
        data_populations = []
        populations = models.PopulationsModels.objects.all()
        for population in populations:
            dt = {}
            dt['nama'] = population.r402
            dt['hubungan'] = f'{population.get_r409_display()} (Keluarga {population.family_id.r108})'
            dt['keberadaan'] = population.get_r404_display()
            dt['tgl_lahir'] = population.r406
            dt['umur'] = population.r407
            dt['pendidikan'] = population.get_r415_display() if population.r415 is not None else '-'
            data_populations.append(dt)

        context = {
            'title' : 'Manajemen Penduduk',
            'populations' : data_populations,
            'education_levels' : education_levels,
            'home_ownership_state' : home_ownership_state,
        }
        return render(request, 'app/master/master-penduduk.html', context)
