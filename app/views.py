from django.urls import reverse_lazy
from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.serializers.json import DjangoJSONEncoder
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from . import models, helpers, forms
from django.http import JsonResponse, HttpResponse
from pprint import pprint
from django.db.models import Q, Count, Sum, Avg
from django.db.models.functions import Length
import json
from django.shortcuts import get_object_or_404, redirect



# Create your views here.
class DashboardClassView(LoginRequiredMixin, View):
    def get(self, request):

        
        dashboard_population = helpers.get_dashboard_population()
        dashboard_family = helpers.get_dashboard_family()

        context = {
            'title' : 'Halaman Dashboard',
            # 'families' : families,
            # 'populations' : pop_counter,
            # 'disability' : disability,
            # 'labor_percentage' : labor_percentage,
            # 'welfare_recips' : welfare_recips,
            # 'dashboard' : dashboard,
            'dashboard_population' : dashboard_population,
            'dashboard_family' : dashboard_family
        }


        return render(request, 'app/dashboard/dashboard.html', context)

class TabulationsFamiliesClassView(LoginRequiredMixin, View):
    
    def get(self, request):

        tabulations = helpers.get_tab_families()
        context = {
            'title' : 'Tabulasi Data Keluarga',
            'tabulations' : tabulations,
            'province_regions' : models.RegionAdministrativeModels.objects.annotate(text_len=Length('reg_code')).filter(text_len=2).order_by('reg_code')
        }

        return render(request, 'app/tabulasi/tabulasi-keluarga.html', context)

class TabulationsFamiliesFetchClassView(LoginRequiredMixin, View):

    def post(self, request):
        is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
        if is_ajax:
            if request.method == 'POST':
                
                tab_request = request.POST.get('tab_request')
                if tab_request is None:
                    return JsonResponse({"status": 'failed'}, status=400)
                
                tab_request = int(tab_request)
                adm_code = request.POST.get('adm_code')
                sls_code = request.POST.get('sls_code')

                tabs = helpers.get_tab_families()
                check_tab = next((d['text'] for (index, d) in enumerate(tabs) if d['val'] == int(tab_request)), None)
                if check_tab is None:
                    return JsonResponse({"status": 'failed'}, status=400)
                
                model = models.FamiliesModels.objects
                if adm_code:
                    model = model.filter(r104__reg_code__icontains = adm_code)
                if sls_code:
                    model = model.filter(r105__reg_sls_code__icontains = sls_code)

                data_tabs = {}
                if tab_request == 1:
                    model = model.aggregate(
                        section1 = Count('r301', filter=Q(r301='1')),
                        section2 = Count('r301', filter=Q(r301='2')),
                        section3 = Count('r301', filter=Q(r301='3')),
                        section4 = Count('r301', filter=Q(r301='4')),
                        section5 = Count('r301', filter=Q(r301='5')),
                        section6 = Count('r301', filter=Q(r301='6'))
                    )
                    model = list(model.values())

                    r301 = models.FamiliesModels.r301.field.choices
                    data = [[(idx+1, 'text-center'), (dt[1], 'text-left'), (model[idx], 'text-center')] for idx, dt in enumerate(r301)]
                        
                    data_tabs['title'] = check_tab
                    data_tabs['content_table'] = helpers.generate_table(
                        [{'name':'No', 'class' : 'text-center'}, {'name':'Status penguasaan bangunan tempat tinggal', 'class' : ''}, {'name':'Jumlah Keluarga', 'class' : 'text-center'}],
                        data
                    )
                    return JsonResponse({"status": 'success', 'content' : data_tabs }, status=200)
                
                elif tab_request == 2:
                    model = model.aggregate(
                        section1 = Count('r302', filter=Q(r302='1')),
                        section2 = Count('r302', filter=Q(r302='2')),
                        section3 = Count('r302', filter=Q(r302='3')),
                        section4 = Count('r302', filter=Q(r302='4'))
                    )
                    model = list(model.values())

                    r302 = models.FamiliesModels.r302.field.choices
                    data = [[(idx+1, 'text-center'), (dt[1], 'text-left'), (model[idx], 'text-center')] for idx, dt in enumerate(r302)]
                        
                    data_tabs['title'] = check_tab
                    data_tabs['content_table'] = helpers.generate_table(
                        [{'name':'No', 'class' : 'text-center'}, {'name':'Status Kepemilikan Lahan Tempat Tinggal', 'class' : ''}, {'name':'Jumlah Keluarga', 'class' : 'text-center'}],
                        data
                    )
                    return JsonResponse({"status": 'success', 'content' : data_tabs }, status=200)
          
                elif tab_request == 3:
                    model = model.aggregate(
                        section1 = Count('r303', filter=Q(r303='1')),
                        section2 = Count('r303', filter=Q(r303='2')),
                        section3 = Count('r303', filter=Q(r303='3')),
                        section4 = Count('r303', filter=Q(r303='4')),
                        section5 = Count('r303', filter=Q(r303='5')),
                        section6 = Count('r303', filter=Q(r303='6')),
                        section7 = Count('r303', filter=Q(r303='7')),
                        section8 = Count('r303', filter=Q(r303='8')),
                        section9 = Count('r303', filter=Q(r303='9')),
                        section10 = Count('r303', filter=Q(r303='10'))
                    )
                    model = list(model.values())

                    r303 = models.FamiliesModels.r303.field.choices
                    data = [[(idx+1, 'text-center'), (dt[1], 'text-left'), (model[idx], 'text-center')] for idx, dt in enumerate(r303)]
                        
                    data_tabs['title'] = check_tab
                    data_tabs['content_table'] = helpers.generate_table(
                        [{'name':'No', 'class' : 'text-center'}, {'name':'Jenis Lantai Bangunan Terluas', 'class' : ''}, {'name':'Jumlah Keluarga', 'class' : 'text-center'}],
                        data
                    )
                    return JsonResponse({"status": 'success', 'content' : data_tabs }, status=200)

                elif tab_request == 4:
                    model = model.aggregate(
                        section1 = Count('r304', filter=Q(r304='1')),
                        section2 = Count('r304', filter=Q(r304='2')),
                        section3 = Count('r304', filter=Q(r304='3')),
                        section4 = Count('r304', filter=Q(r304='4')),
                        section5 = Count('r304', filter=Q(r304='5')),
                        section6 = Count('r304', filter=Q(r304='6')),
                        section7 = Count('r304', filter=Q(r304='7'))
                    )
                    model = list(model.values())

                    r304 = models.FamiliesModels.r304.field.choices
                    data = [[(idx+1, 'text-center'), (dt[1], 'text-left'), (model[idx], 'text-center')] for idx, dt in enumerate(r304)]
                        
                    data_tabs['title'] = check_tab
                    data_tabs['content_table'] = helpers.generate_table(
                        [{'name':'No', 'class' : 'text-center'}, {'name':'Jenis Dinding Bangunan Terluas', 'class' : ''}, {'name':'Jumlah Keluarga', 'class' : 'text-center'}],
                        data
                    )
                    return JsonResponse({"status": 'success', 'content' : data_tabs }, status=200)

                elif tab_request == 5:
                    model = model.aggregate(
                        section1 = Count('r306', filter=Q(r306='1')),
                        section2 = Count('r306', filter=Q(r306='2')),
                        section3 = Count('r306', filter=Q(r306='3')),
                        section4 = Count('r306', filter=Q(r306='4')),
                        section5 = Count('r306', filter=Q(r306='5')),
                        section6 = Count('r306', filter=Q(r306='6')),
                        section7 = Count('r306', filter=Q(r306='7')),
                        section8 = Count('r306', filter=Q(r306='8')),
                        section9 = Count('r306', filter=Q(r306='9')),
                        section10 = Count('r306', filter=Q(r306='10'))
                    )
                    model = list(model.values())

                    r306 = models.FamiliesModels.r306.field.choices
                    data = [[(idx+1, 'text-center'), (dt[1], 'text-left'), (model[idx], 'text-center')] for idx, dt in enumerate(r306)]
                        
                    data_tabs['title'] = check_tab
                    data_tabs['content_table'] = helpers.generate_table(
                        [{'name':'No', 'class' : 'text-center'}, {'name':'Jenis Atap Bangunan Terluas', 'class' : ''}, {'name':'Jumlah Keluarga', 'class' : 'text-center'}],
                        data
                    )
                    return JsonResponse({"status": 'success', 'content' : data_tabs }, status=200)
             
                elif tab_request == 6:
                    model = model.aggregate(
                        section1 = Count('r305', filter=Q(r305='1')),
                        section2 = Count('r305', filter=Q(r305='2')),
                        section3 = Count('r305', filter=Q(r305='3'))
                    )
                    model = list(model.values())

                    r305 = models.FamiliesModels.r305.field.choices
                    data = [[(idx+1, 'text-center'), (dt[1], 'text-left'), (model[idx], 'text-center')] for idx, dt in enumerate(r305)]
                        
                    data_tabs['title'] = check_tab
                    data_tabs['content_table'] = helpers.generate_table(
                        [{'name':'No', 'class' : 'text-center'}, {'name':'Ketersediaan Ventilasi Udara', 'class' : ''}, {'name':'Jumlah Keluarga', 'class' : 'text-center'}],
                        data
                    )
                    return JsonResponse({"status": 'success', 'content' : data_tabs }, status=200)

                elif tab_request == 7:
                    model = model.aggregate(
                        section1 = Count('r307', filter=Q(r307='1')),
                        section2 = Count('r307', filter=Q(r307='2')),
                        section3 = Count('r307', filter=Q(r307='3')),
                        section4 = Count('r307', filter=Q(r307='4'))
                    )
                    model = list(model.values())

                    r307 = models.FamiliesModels.r307.field.choices
                    data = [[(idx+1, 'text-center'), (dt[1], 'text-left'), (model[idx], 'text-center')] for idx, dt in enumerate(r307)]
                        
                    data_tabs['title'] = check_tab
                    data_tabs['content_table'] = helpers.generate_table(
                        [{'name':'No', 'class' : 'text-center'}, {'name':'Sumber Penerangan Utama Bangunan', 'class' : ''}, {'name':'Jumlah Keluarga', 'class' : 'text-center'}],
                        data
                    )
                    return JsonResponse({"status": 'success', 'content' : data_tabs }, status=200)

                elif tab_request == 8:
                    model = model.aggregate(
                        section1 = Count('r308', filter=Q(r308='1')),
                        section2 = Count('r308', filter=Q(r308='2')),
                        section3 = Count('r308', filter=Q(r308='3')),
                        section4 = Count('r308', filter=Q(r308='4')),
                        section5 = Count('r308', filter=Q(r308='5'))
                    )
                    model = list(model.values())

                    r308 = models.FamiliesModels.r308.field.choices
                    data = [[(idx+1, 'text-center'), (dt[1], 'text-left'), (model[idx], 'text-center')] for idx, dt in enumerate(r308)]
                        
                    data_tabs['title'] = check_tab
                    data_tabs['content_table'] = helpers.generate_table(
                        [{'name':'No', 'class' : 'text-center'}, {'name':'Ketersediaan Tempat Pembuangan Sampah', 'class' : ''}, {'name':'Jumlah Keluarga', 'class' : 'text-center'}],
                        data
                    )
                    return JsonResponse({"status": 'success', 'content' : data_tabs }, status=200)

                elif tab_request == 9:
                    model = model.aggregate(
                        section1 = Count('r310', filter=Q(r310='1')),
                        section2 = Count('r310', filter=Q(r310='2')),
                        section3 = Count('r310', filter=Q(r310='3')),
                        section4 = Count('r310', filter=Q(r310='4')),
                        section5 = Count('r310', filter=Q(r310='5')),
                        section6 = Count('r310', filter=Q(r310='6')),
                        section7 = Count('r310', filter=Q(r310='7')),
                        section8 = Count('r310', filter=Q(r310='8')),
                        section9 = Count('r310', filter=Q(r310='9')),
                        section10 = Count('r310', filter=Q(r310='10'))
                    )
                    model = list(model.values())

                    r310 = models.FamiliesModels.r310.field.choices
                    data = [[(idx+1, 'text-center'), (dt[1], 'text-left'), (model[idx], 'text-center')] for idx, dt in enumerate(r310)]
                        
                    data_tabs['title'] = check_tab
                    data_tabs['content_table'] = helpers.generate_table(
                        [{'name':'No', 'class' : 'text-center'}, {'name':'Sumber Air Minum Utama', 'class' : ''}, {'name':'Jumlah Keluarga', 'class' : 'text-center'}],
                        data
                    )
                    return JsonResponse({"status": 'success', 'content' : data_tabs }, status=200)

                elif tab_request == 10:
                    model = model.aggregate(
                        section1 = Count('r401a', filter=Q(r401a='1')),
                        section2 = Count('r401a', filter=Q(r401a='2')),
                    )
                    model = list(model.values())

                    r401a = models.FamiliesModels.r401a.field.choices
                    data = [[(idx+1, 'text-center'), (dt[1], 'text-left'), (model[idx], 'text-center')] for idx, dt in enumerate(r401a)]
                        
                    data_tabs['title'] = check_tab
                    data_tabs['content_table'] = helpers.generate_table(
                        [{'name':'No', 'class' : 'text-center'}, {'name':'Kepemilikan Tanah/Lahan Pertanian', 'class' : ''}, {'name':'Jumlah Keluarga', 'class' : 'text-center'}],
                        data
                    )
                    return JsonResponse({"status": 'success', 'content' : data_tabs }, status=200)

                elif tab_request == 11:
                   
                    model = model.filter(r401a = '1').values_list('r401b', flat=True)
                    model = list(model)
                    data = [[(1, 'text-center'), ('Data tidak tersedia', 'text-left'), (0, 'text-center')]]
                    if len(model) != 0:
                        groups = helpers.splitting_list(model, 5)
                        data = [[(idx+1, 'text-center'), (dt[0], 'text-left'), (dt[1], 'text-center')] for idx, dt in enumerate(groups)]

                    data_tabs['title'] = check_tab
                    data_tabs['content_table'] = helpers.generate_table(
                        [{'name':'No', 'class' : 'text-center'}, {'name':'Luas Lahan Pertanian (Ha)', 'class' : ''}, {'name':'Jumlah Keluarga', 'class' : 'text-center'}],
                        data
                    )

                    return JsonResponse({"status": 'success', 'content' : data_tabs }, status=200)
                
                elif tab_request == 12:
                    model = model.aggregate(
                        section1 = Count('r402a', filter=Q(r402a='1')),
                        section2 = Count('r402b', filter=Q(r402b='1')),
                        section3 = Count('r402c', filter=Q(r402c='1')),
                        section4 = Count('r402d', filter=Q(r402d='1')),
                        section5 = Count('r402e', filter=Q(r402e='1')),
                        section6 = Count('r402g', filter=Q(r402g='1')),
                        section7 = Count('r402h', filter=Q(r402h='1')),
                        section8 = Count('r402i', filter=Q(r402i='1'))
                    )
                    model = list(model.values())
                    data = [
                        [(1, 'text-center'), ('Sapi', 'text-left'), (model[0], 'text-center')],
                        [(2, 'text-center'), ('Kerbau', 'text-left'), (model[1], 'text-center')],
                        [(3, 'text-center'), ('Kuda', 'text-left'), (model[2], 'text-center')],
                        [(4, 'text-center'), ('Babi', 'text-left'), (model[3], 'text-center')],
                        [(5, 'text-center'), ('Kambing/Domba', 'text-left'), (model[4], 'text-center')],
                        [(6, 'text-center'), ('Ayam Buras', 'text-left'), (model[5], 'text-center')],
                        [(7, 'text-center'), ('Ayam Ras Pedaging', 'text-left'), (model[6], 'text-center')],
                        [(8, 'text-center'), ('Ayam Ras Petelur', 'text-left'), (model[7], 'text-center')],
                    ]

                    data_tabs['title'] = check_tab
                    data_tabs['content_table'] = helpers.generate_table(
                        [{'name':'No', 'class' : 'text-center'}, {'name':'Jumlah Kepemilikan Hewan Ternak (Ekor)', 'class' : ''}, {'name':'Jumlah Keluarga', 'class' : 'text-center'}],
                        data
                    )
                    return JsonResponse({"status": 'success', 'content' : data_tabs }, status=200)

        return JsonResponse({'status': 'Invalid request'}, status=400)

class TabulationsPopulationsClassView(LoginRequiredMixin, View):
    
    def get(self, request):
        populations = models.PopulationsModels.objects.all().count()
        tabulations = helpers.get_tab_populations()
        context = {
            'title' : 'Tabulasi Data Penduduk',
            'populations' : populations,
            'tabulations' : tabulations,
            'province_regions' : models.RegionAdministrativeModels.objects.annotate(text_len=Length('reg_code')).filter(text_len=2).order_by('reg_code')
        }
        return render(request, 'app/tabulasi/tabulasi-penduduk.html', context)

class TabulationsPopulationsFetchClassView(LoginRequiredMixin, View):

    def post(self, request):
        is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
        if is_ajax:
            if request.method == 'POST':

                tab_request = request.POST.get('tab_request')
                if tab_request is None:
                    return JsonResponse({"status": 'failed'}, status=400)
                
                tab_request = int(tab_request)
                adm_code = request.POST.get('adm_code')
                sls_code = request.POST.get('sls_code')

                tabs = helpers.get_tab_populations()
                check_tab = next((d['text'] for (index, d) in enumerate(tabs) if d['val'] == int(tab_request)), None)
                if check_tab is None:
                    return JsonResponse({"status": 'failed'}, status=400)
                
                model = models.PopulationsModels.objects
                if adm_code:
                    model = model.filter(family_id__r104__reg_code__icontains = adm_code)
                if sls_code:
                    model = model.filter(family_id__r105__reg_sls_code__icontains = sls_code)

                data_tabs = {}
                if tab_request == 1:
                    model = model.aggregate(
                        section1 = Count('r504', filter=Q(r504='1')),
                        section2 = Count('r504', filter=Q(r504='2')),
                        section3 = Count('r504', filter=Q(r504='3')),
                        section4 = Count('r504', filter=Q(r504='4')),
                        section5 = Count('r504', filter=Q(r504='5')),
                        section6 = Count('r504', filter=Q(r504='6')),
                        section7 = Count('r504', filter=Q(r504='7'))
                    )
                    model = list(model.values())

                    r504 = models.PopulationsModels.r504.field.choices
                    data = [[(idx+1, 'text-center'), (dt[1], 'text-left'), (model[idx], 'text-center')] for idx, dt in enumerate(r504)]
                        
                    data_tabs['title'] = check_tab
                    data_tabs['content_table'] = helpers.generate_table(
                        [{'name':'No', 'class' : 'text-center'}, {'name':'Hubungan dengan Kepala Keluarga', 'class' : ''}, {'name':'Jumlah Penduduk', 'class' : 'text-center'}],
                        data
                    )
                    return JsonResponse({"status": 'success', 'content' : data_tabs }, status=200)
                
                elif tab_request == 2:
                    model = model.aggregate(
                        section1 = Count('r505', filter=Q(r505='1')),
                        section2 = Count('r505', filter=Q(r505='2')),
                        section3 = Count('r505', filter=Q(r505='3')),
                        section4 = Count('r505', filter=Q(r505='4')),
                        section5 = Count('r505', filter=Q(r505='5'))
                    )
                    model = list(model.values())

                    r505 = models.PopulationsModels.r505.field.choices
                    data = [[(idx+1, 'text-center'), (dt[1], 'text-left'), (model[idx], 'text-center')] for idx, dt in enumerate(r505)]
                        
                    data_tabs['title'] = check_tab
                    data_tabs['content_table'] = helpers.generate_table(
                        [{'name':'No', 'class' : 'text-center'}, {'name':'Keberadaan Anggota Rumah Tangga', 'class' : ''}, {'name':'Jumlah Penduduk', 'class' : 'text-center'}],
                        data
                    )
                    return JsonResponse({"status": 'success', 'content' : data_tabs }, status=200)
                
                elif tab_request == 3:
                    model = model.aggregate(
                        section1 = Count('r506', filter=Q(r506='1')),
                        section2 = Count('r506', filter=Q(r506='2'))
                    )
                    model = list(model.values())

                    r506 = models.PopulationsModels.r506.field.choices
                    data = [[(idx+1, 'text-center'), (dt[1], 'text-left'), (model[idx], 'text-center')] for idx, dt in enumerate(r506)]
                        
                    data_tabs['title'] = check_tab
                    data_tabs['content_table'] = helpers.generate_table(
                        [{'name':'No', 'class' : 'text-center'}, {'name':'Jenis Kelamin ART', 'class' : ''}, {'name':'Jumlah Penduduk', 'class' : 'text-center'}],
                        data
                    )
                    return JsonResponse({"status": 'success', 'content' : data_tabs }, status=200)
                
                elif tab_request == 4:
                    model = model.aggregate(
                        section1 = Count('r510', filter=Q(r510='1')),
                        section2 = Count('r510', filter=Q(r510='2')),
                        section3 = Count('r510', filter=Q(r510='3')),
                        section4 = Count('r510', filter=Q(r510='4'))
                    )
                    model = list(model.values())

                    r510 = models.PopulationsModels.r510.field.choices
                    data = [[(idx+1, 'text-center'), (dt[1], 'text-left'), (model[idx], 'text-center')] for idx, dt in enumerate(r510)]
                        
                    data_tabs['title'] = check_tab
                    data_tabs['content_table'] = helpers.generate_table(
                        [{'name':'No', 'class' : 'text-center'}, {'name':'Status Perkawinan ART', 'class' : ''}, {'name':'Jumlah Penduduk', 'class' : 'text-center'}],
                        data
                    )
                    return JsonResponse({"status": 'success', 'content' : data_tabs }, status=200)
                
                elif tab_request == 5:
                    model = model.aggregate(
                        section1 = Count('r511', filter=Q(r511='1')),
                        section2 = Count('r511', filter=Q(r511='2')),
                        section3 = Count('r511', filter=Q(r511='3')),
                        section4 = Count('r511', filter=Q(r511='4')),
                        section5 = Count('r511', filter=Q(r511='5')),
                        section6 = Count('r511', filter=Q(r511='6'))
                    )
                    model = list(model.values())

                    r511 = models.PopulationsModels.r511.field.choices
                    data = [[(idx+1, 'text-center'), (dt[1], 'text-left'), (model[idx], 'text-center')] for idx, dt in enumerate(r511)]
                        
                    data_tabs['title'] = check_tab
                    data_tabs['content_table'] = helpers.generate_table(
                        [{'name':'No', 'class' : 'text-center'}, {'name':'Agama', 'class' : ''}, {'name':'Jumlah Penduduk', 'class' : 'text-center'}],
                        data
                    )
                    return JsonResponse({"status": 'success', 'content' : data_tabs }, status=200)
                
                elif tab_request == 6:
                    model = model.aggregate(
                        section1 = Count('r512', filter=Q(r512='1')),
                        section2 = Count('r512', filter=Q(r512='2')),
                    )
                    model = list(model.values())

                    r512 = models.PopulationsModels.r512.field.choices
                    data = [[(idx+1, 'text-center'), (dt[1], 'text-left'), (model[idx], 'text-center')] for idx, dt in enumerate(r512)]
                        
                    data_tabs['title'] = check_tab
                    data_tabs['content_table'] = helpers.generate_table(
                        [{'name':'No', 'class' : 'text-center'}, {'name':'Suku', 'class' : ''}, {'name':'Jumlah Penduduk', 'class' : 'text-center'}],
                        data
                    )
                    return JsonResponse({"status": 'success', 'content' : data_tabs }, status=200)
                
                elif tab_request == 7:
                    model = model.aggregate(
                        section1 = Count('r513', filter=Q(r513='1')),
                        section2 = Count('r513', filter=Q(r513='2')),
                        section3 = Count('r513', filter=Q(r513='3')),
                        section4 = Count('r513', filter=Q(r513='4')),
                        section5 = Count('r513', filter=Q(r513='5'))
                    )
                    model = list(model.values())

                    r513 = models.PopulationsModels.r513.field.choices
                    data = [[(idx+1, 'text-center'), (dt[1], 'text-left'), (model[idx], 'text-center')] for idx, dt in enumerate(r513)]
                        
                    data_tabs['title'] = check_tab
                    data_tabs['content_table'] = helpers.generate_table(
                        [{'name':'No', 'class' : 'text-center'}, {'name':'Kegiatan Utama ART', 'class' : ''}, {'name':'Jumlah Penduduk', 'class' : 'text-center'}],
                        data
                    )
                    return JsonResponse({"status": 'success', 'content' : data_tabs }, status=200)
                
                elif tab_request == 8:
                    model = model.aggregate(
                        section1 = Count('r515', filter=Q(r515='01')),
                        section2 = Count('r515', filter=Q(r515='02')),
                        section3 = Count('r515', filter=Q(r515='03')),
                        section4 = Count('r515', filter=Q(r515='04')),
                        section5 = Count('r515', filter=Q(r515='05')),
                        section6 = Count('r515', filter=Q(r515='06')),
                        section7 = Count('r515', filter=Q(r515='07')),
                        section8 = Count('r515', filter=Q(r515='08')),
                        section9 = Count('r515', filter=Q(r515='09')),
                        section10 = Count('r515', filter=Q(r515='10')),

                        section11 = Count('r515', filter=Q(r515='11')),
                        section12 = Count('r515', filter=Q(r515='12')),
                        section13 = Count('r515', filter=Q(r515='13')),
                        section14 = Count('r515', filter=Q(r515='14')),
                        section15 = Count('r515', filter=Q(r515='15')),
                        section16 = Count('r515', filter=Q(r515='16')),
                        section17 = Count('r515', filter=Q(r515='17')),
                        section18 = Count('r515', filter=Q(r515='18')),
                        section19 = Count('r515', filter=Q(r515='19')),
                        section20 = Count('r515', filter=Q(r515='20')),

                        section21 = Count('r515', filter=Q(r515='21')),
                        section22 = Count('r515', filter=Q(r515='22')),
                        section23 = Count('r515', filter=Q(r515='23')),
                        section24 = Count('r515', filter=Q(r515='24')),
                        section25 = Count('r515', filter=Q(r515='25')),
                        section26 = Count('r515', filter=Q(r515='26')),
                    )
                    model = list(model.values())

                    r515 = models.PopulationsModels.r515.field.choices
                    data = [[(idx+1, 'text-center'), (dt[1], 'text-left'), (model[idx], 'text-center')] for idx, dt in enumerate(r515)]
                        
                    data_tabs['title'] = check_tab
                    data_tabs['content_table'] = helpers.generate_table(
                        [{'name':'No', 'class' : 'text-center'}, {'name':'Lapangan Usaha', 'class' : ''}, {'name':'Jumlah Penduduk', 'class' : 'text-center'}],
                        data
                    )
                    return JsonResponse({"status": 'success', 'content' : data_tabs }, status=200)
                
                elif tab_request == 9:
                    model = model.aggregate(
                        section1 = Count('r517', filter=Q(r517='1')),
                        section2 = Count('r517', filter=Q(r517='2')),
                        section3 = Count('r517', filter=Q(r517='3'))
                    )
                    model = list(model.values())

                    r517 = models.PopulationsModels.r517.field.choices
                    data = [[(idx+1, 'text-center'), (dt[1], 'text-left'), (model[idx], 'text-center')] for idx, dt in enumerate(r517)]
                        
                    data_tabs['title'] = check_tab
                    data_tabs['content_table'] = helpers.generate_table(
                        [{'name':'No', 'class' : 'text-center'}, {'name':'Status Partisipasi Sekolah', 'class' : ''}, {'name':'Jumlah Penduduk', 'class' : 'text-center'}],
                        data
                    )
                    return JsonResponse({"status": 'success', 'content' : data_tabs }, status=200)
                
                elif tab_request == 10:
                    model = model.aggregate(
                        section1 = Count('r518', filter=Q(r518='1')),
                        section2 = Count('r518', filter=Q(r518='2')),
                        section3 = Count('r518', filter=Q(r518='3')),
                        section4 = Count('r518', filter=Q(r518='4')),
                        section5 = Count('r518', filter=Q(r518='5')),
                        section6 = Count('r518', filter=Q(r518='6'))
                    )
                    model = list(model.values())

                    r518 = models.PopulationsModels.r518.field.choices
                    data = [[(idx+1, 'text-center'), (dt[1], 'text-left'), (model[idx], 'text-center')] for idx, dt in enumerate(r518)]
                        
                    data_tabs['title'] = check_tab
                    data_tabs['content_table'] = helpers.generate_table(
                        [{'name':'No', 'class' : 'text-center'}, {'name':'Jenjang Pendidikan yang Ditamatkan', 'class' : ''}, {'name':'Jumlah Penduduk', 'class' : 'text-center'}],
                        data
                    )
                    return JsonResponse({"status": 'success', 'content' : data_tabs }, status=200)

                elif tab_request == 11:
                    model = model.aggregate(
                        section1 = Count('r519', filter=Q(r519='0')),
                        section2 = Count('r519', filter=Q(r519='1')),
                        section3 = Count('r519', filter=Q(r519='2')),
                        section4 = Count('r519', filter=Q(r519='3')),
                    )
                    model = list(model.values())

                    r519 = models.PopulationsModels.r519.field.choices
                    data = [[(idx+1, 'text-center'), (dt[1], 'text-left'), (model[idx], 'text-center')] for idx, dt in enumerate(r519)]
                        
                    data_tabs['title'] = check_tab
                    data_tabs['content_table'] = helpers.generate_table(
                        [{'name':'No', 'class' : 'text-center'}, {'name':'Jaminan Kesehatan', 'class' : ''}, {'name':'Jumlah Penduduk', 'class' : 'text-center'}],
                        data
                    )
                    return JsonResponse({"status": 'success', 'content' : data_tabs }, status=200)
                
                elif tab_request == 12:
                    model = model.aggregate(
                        section1 = Count('r520a', filter=Q(r520a='1')),
                        section2 = Count('r520b', filter=Q(r520b='1')),
                        section3 = Count('r520c', filter=Q(r520c='1')),
                        section4 = Count('r520d', filter=Q(r520d='1')),
                        section5 = Count('r520e', filter=Q(r520e='1')),
                        section6 = Count('r520f', filter=Q(r520f='1')),
                        section7 = Count('r520g', filter=Q(r520g='1')),
                        section8 = Count('r520h', filter=Q(r520h='1'))
                    )
                    model = list(model.values())
                    data = [
                        [(1, 'text-center'), ('Tunanetra/Buta', 'text-left'), (model[0], 'text-center')],
                        [(2, 'text-center'), ('Tunarungu/Tuli', 'text-left'), (model[1], 'text-center')],
                        [(3, 'text-center'), ('Tunawicara/Bisu', 'text-left'), (model[2], 'text-center')],
                        [(4, 'text-center'), ('Tunarungu-Wicara/Tuli-Bisu', 'text-left'), (model[3], 'text-center')],
                        [(5, 'text-center'), ('Tunadaksa/Cacat Tubuh', 'text-left'), (model[4], 'text-center')],
                        [(6, 'text-center'), ('Tunagrahita', 'text-left'), (model[5], 'text-center')],
                        [(7, 'text-center'), ('Tunalaras', 'text-left'), (model[6], 'text-center')],
                        [(8, 'text-center'), ('Cacat Ganda', 'text-left'), (model[7], 'text-center')],
                    ]

                    data_tabs['title'] = check_tab
                    data_tabs['content_table'] = helpers.generate_table(
                        [{'name':'No', 'class' : 'text-center'}, {'name':'Keterangan Disabilitas', 'class' : ''}, {'name':'Jumlah Penduduk', 'class' : 'text-center'}],
                        data
                    )
                    return JsonResponse({"status": 'success', 'content' : data_tabs }, status=200)
                
        return JsonResponse({'status': 'Invalid request'}, status=400)

class ManajemenFamiliesClassView(LoginRequiredMixin, View):
    
    def get(self, request):

        pencacah = models.OfficerModels.objects.filter(role = '1').all()
        pemeriksa = models.OfficerModels.objects.filter(role = '2').all()
        hasil = models.FamiliesModels.r206.field.choices

        filters = [
            [1, 'Pendidikan Kepala Rumah Tangga'],
            [2, 'Status Penguasaan Bangunan Tempat Tinggal'],
            [3, 'Status Lahan Tempat Tinggal'],
            [4, 'Jenis Lantai Terluas'],
            [5, 'Jenis Dinding Terluas'],
            [6, 'Keberadaan Jendela'],
            [7, 'Jenis Atap Terluas'],
            [8, 'Sumber Penerangan Utama'],
            [9, 'Tempat Pembuangan Sampah'],
            [10, 'Sumber Air Minum Utama']
        ]
        
        context = {
            'title' : 'Manajemen Keluarga',
            'pencacah' : pencacah,
            'pemeriksa' : pemeriksa,
            'hasil' : hasil,
            'filters' : filters,
            'province_regions' : models.RegionAdministrativeModels.objects.annotate(text_len=Length('reg_code')).filter(text_len=2).order_by('reg_code')
   
        }

        return render(request, 'app/master/master-keluarga.html', context)

class ManajemenFamiliesFetchTableClassView(LoginRequiredMixin, View):

    def post(self, request):
        
        data = self._datatables(request)
        return HttpResponse(json.dumps(data, cls=DjangoJSONEncoder), content_type='application/json')
		
    def _datatables(self, request):

        # Define default column for ordering first request
        def_col = 'r107' 

        datatables = request.POST

        # Get Draw
        draw = int(datatables.get('draw'))
        start = int(datatables.get('start'))
        search = datatables.get('search[value]')

        order_idx = int(datatables.get('order[0][column]')) # Default 1st index for
        order_dir = datatables.get('order[0][dir]') # Descending or Ascending
        order_col = 'columns[' + str(order_idx) + '][data]'
        order_col_name = datatables.get(order_col)

        if 'no' in order_col_name:
            order_col_name = def_col

        if (order_dir == "desc"):
            order_col_name =  str('-' + order_col_name)

        model = models.FamiliesModels.objects

        id_def_data = list(model.order_by(def_col).values_list('id'))
        id_def_data = [list((idx+1, ) + id_def_data[idx]) for idx in range(len(id_def_data))]
        
        records_total = model.count()
        records_filtered = records_total
        
        if datatables.get('region'):
            model = model.filter(r104__reg_code__icontains = datatables.get('region'))

        if datatables.get('region_sls'):
            model = model.filter(r105__reg_sls_code__icontains = datatables.get('region_sls'))
        
        if datatables.get('r201'):
            model = model.filter(r201 = datatables.get('r201'))

        if datatables.get('r204'):
            model = model.filter(r204 = datatables.get('r204'))

        if datatables.get('r206'):
            model = model.filter(r206 = datatables.get('r206'))

        if datatables.get('filter'):
            req, val = datatables.get('filter').split('_')
            if req == '1':
                model = models.FamiliesModels.objects.filter(families_members__r504 = '1', families_members__r518 = val)
            elif req == '2':
                model = model.filter(r301 = val)
            elif req == '3':
                model = model.filter(r302 = val)
            elif req == '4':
                model = model.filter(r303 = val)
            elif req == '5':
                model = model.filter(r304 = val)
            elif req == '6':
                model = model.filter(r305 = val)
            elif req == '7':
                model = model.filter(r306 = val)
            elif req == '8':
                model = model.filter(r307 = val)
            elif req == '9':
                model = model.filter(r308 = val)
            else:
                model = model.filter(r310 = val)

        if search:
            model = model.filter(
                Q(r104__reg_name__icontains=search) |
                Q(r105__reg_sls_code__icontains=search) |
                Q(r105__reg_sls_name__icontains=search) |
                Q(r107__icontains=search)|
                Q(r109__icontains=search)
            ).exclude(
                Q(r104=None) |
                Q(r105=None) |
                Q(r107=None) |
                Q(r109=None)
            )

            records_total = model.count()
            records_filtered = records_total
        
        model = model.order_by(order_col_name)
            
        # Conf Paginator
        length = int(datatables.get('length')) if int(datatables.get('length')) > 0 else len(model)
        page_number = int(start / length + 1)
        paginator = Paginator(model, length)

        try:
            object_list = paginator.page(page_number).object_list
        except PageNotAnInteger:
            object_list = paginator.page(1).object_list
        except EmptyPage:
            object_list = paginator.page(1).object_list

        data = []

        for obj in object_list:
            data.append(
            {
                'no': [x for x in id_def_data if obj.id == x[1]][0][0],
                'r104__reg_name' : f'{obj.r104.reg_name} / ({obj.r105.reg_sls_code}) {obj.r105.reg_sls_name}',
                'r107': obj.r107,
                'r109': obj.r109,
                'r203' : obj.r203.strftime('%d-%m-%Y'),
                'created_at' : obj.created_at.strftime('%d-%m-%Y'),
                'actions': f'<a href="{reverse_lazy("app:mnj_families_edit")}?id={obj.id}" target="_blank" class="btn btn-sm icon btn-edit p-0" data-id="{obj.id}"><i class="mdi mdi-account-edit"></i></a>\
                <button class="btn btn-sm icon btn-delete p-0" data-id="{obj.id}"><i class="mdi mdi-trash-can-outline"></i></button>'
            })

        return {    
            'draw': draw,
            'recordsTotal': records_total,
            'recordsFiltered': records_filtered,
            'data': data,
        }

class ManajemenFamiliesEditClassView(LoginRequiredMixin, View):
    
    def get(self, request):

        if request.GET.get('id') is not None:
            model = models.FamiliesModels.objects.prefetch_related('families_members').filter(pk = int(request.GET.get('id')))
            if model.exists():
                model = model.first()
                regions = helpers.get_region_code(model.r104.reg_code, model.r105.pk)
                forms_art = []
                id = []
                for dt in model.families_members.all():
                    form = forms.PopulationsForm(instance=dt)
                    forms_art.append(form)
                    id.append(dt.id)

                pencacah = models.OfficerModels.objects.filter(role = '1').all()
                pemeriksa = models.OfficerModels.objects.filter(role = '2').all()
                context = {
                    'title' : 'Edit Data Keluarga',
                    'regions' : regions,
                    'pencacah' : pencacah,
                    'pemeriksa' : pemeriksa,
                    'pk' : request.GET.get('id'),
                    'form' : forms.FamiliesForm(instance=model),
                    'forms_art' : zip(id, forms_art),
                    'form_penduduk' : forms.PopulationsForm(),
                }
                return render(request, 'app/master/master-keluarga-edit.html', context)
        return redirect('app:mnj_families')
    
    def post(self, request):

        is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
        if is_ajax:
            if request.method == 'POST':
                data_families = json.loads(request.POST.get('form_families'))
                instance = get_object_or_404(models.FamiliesModels, pk=data_families.get('id'))
                art_colls = list(instance.families_members.values_list('id', flat=True))

                data_art = json.loads(request.POST.get('form_art'))
                art_form_colls = [int(dt) for dt in data_art[0]['art_id'] if len(dt) > 0]

                art_remove = list(set(art_colls) - set(art_form_colls))

                data_art = helpers.transform_data(data_art)
                forms_errors = dict()

                for fl in ['provinsi', 'kabkot', 'kecamatan']:
                    if fl in data_families.keys():
                        if len(data_families[fl]) == 0:
                            forms_errors[fl] = ['This field is required.']
                        del data_families[fl]

                form_family = forms.FamiliesForm(data_families, instance=instance)
                if form_family.is_valid() is False:
                    for key, val in form_family.errors.items():
                        forms_errors[key] = val
                
                forms_validated = []
                for idx, dt in enumerate(data_art):
                    data_art[idx]['family_id'] = instance.id
                    if len(dt['art_id']) != 0:
                        instance_art = get_object_or_404(models.PopulationsModels, pk=dt.get('art_id'))
                        form_art = forms.PopulationsForm(dt, instance=instance_art)
                    else:
                        form_art = forms.PopulationsForm(dt)

                    if form_art.is_valid() is False:
                        for key, val in form_art.errors.items():
                            forms_errors[f'form_art_{key}_{idx+1}'] = val
                    else:
                        forms_validated.append(form_art)

                if len(forms_errors) > 0:
                    return JsonResponse({"status": 'failed', "error": forms_errors}, status=400)

                last_validations = helpers.combine_validations(data_families, data_art)
                if len(last_validations) > 0:
                    for key, val in last_validations.items():
                        forms_errors[key] = val
                    return JsonResponse({"status": 'failed', "error": forms_errors}, status=400)

                form_family.save() 
                for form in forms_validated:
                    form.save()

                for id in art_remove:
                    data = get_object_or_404(models.PopulationsModels, pk=id)
                    data.delete()

                msg = f'<ul class="px-0" style="list-style:none">\
                            Data Keluarga <b>{data_families["r107"]}</b> telah berhasil diupdate.<br>\
                        </ul>'
                return JsonResponse({"status": msg}, status=200)

        return JsonResponse({'status': 'Invalid request'}, status=400)
    
class ManajemenFamiliesAddClassView(LoginRequiredMixin, View):

    def get(self, request):
        pencacah = models.OfficerModels.objects.filter(role = '1').all()
        pemeriksa = models.OfficerModels.objects.filter(role = '2').all()
        context = {
            'title' : 'Tambah Data Keluarga',
            'form' : forms.FamiliesForm(),
            'pencacah' : pencacah,
            'pemeriksa' : pemeriksa,
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

                for fl in ['provinsi', 'kabkot', 'kecamatan']:
                    if fl in data_families.keys():
                        if len(data_families[fl]) == 0:
                            forms_errors[fl] = ['This field is required.']
                        del data_families[fl]

                form_family = forms.FamiliesForm(data_families)
                if form_family.is_valid() is False:
                    for key, val in form_family.errors.items():
                        forms_errors[key] = val
                
                for idx, dt in enumerate(data_art):
                    form_art = forms.PopulationsForm(dt)
                    if form_art.is_valid() is False:
                        for key, val in form_art.errors.items():
                            if key != 'family_id':
                                forms_errors[f'form_art_{key}_{idx+1}'] = val

                if len(forms_errors) > 0:
                    return JsonResponse({"status": 'failed', "error": forms_errors}, status=400)

                last_validations = helpers.combine_validations(data_families, data_art)
                if len(last_validations) > 0:
                    for key, val in last_validations.items():
                        forms_errors[key] = val
                    return JsonResponse({"status": 'failed', "error": forms_errors}, status=400)

                form_family.save()
                last_id = models.FamiliesModels.objects.latest('id').id
                for idx, dt in enumerate(data_art):
                    data_art[idx]['family_id'] = last_id
                    form_art = forms.PopulationsForm(dt)
                    form_art.save()
                
                msg = f'<ul class="px-0" style="list-style:none">\
                            Data Keluarga <b>{data_families["r107"]}</b> telah berhasil ditambahkan.<br>\
                        </ul>'
                return JsonResponse({"status": msg}, status=200)
            
        return JsonResponse({'status': 'Invalid request'}, status=400)

class ManajemenFamiliesDeleteClassView(LoginRequiredMixin, View):

    def post(self, request):
        is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'

        if is_ajax:
            if request.method == 'POST':
                try:
                    data = get_object_or_404(models.FamiliesModels, pk=request.POST.get('pk'))
                    old_dt = data.r107
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

class FilterFamiliyRequestClassView(LoginRequiredMixin, View):
        
        def post(self, request):
            is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
            if is_ajax:
                if request.method == 'POST':
                    req = int(request.POST.get('req'))
                    
                    if req == 1:
                        opts = models.PopulationsModels.r518.field.choices
                    elif req == 2:
                        opts = models.FamiliesModels.r301.field.choices
                    elif req == 3:
                        opts = models.FamiliesModels.r302.field.choices
                    elif req == 4:
                        opts = models.FamiliesModels.r303.field.choices
                    elif req == 5:
                        opts = models.FamiliesModels.r304.field.choices
                    elif req == 6:
                        opts = models.FamiliesModels.r305.field.choices
                    elif req == 7:
                        opts = models.FamiliesModels.r306.field.choices
                    elif req == 8:
                        opts = models.FamiliesModels.r307.field.choices
                    elif req == 9:
                        opts = models.FamiliesModels.r308.field.choices
                    else:
                        opts = models.FamiliesModels.r310.field.choices

                    html = '<option value="">----</option>'
                    for opt in opts:
                        html += f'<option value="{opt[0]}">{opt[1]}</option>'

                    return JsonResponse({"data": html}, status=200)
                
            return JsonResponse({'status': 'Invalid request'}, status=400)
        

class FilterPopulationRequestClassView(LoginRequiredMixin, View):
        
    def post(self, request):
        is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
        if is_ajax:
            if request.method == 'POST':
                req = int(request.POST.get('req'))
                if req == 1:
                    opts = models.PopulationsModels.r506.field.choices
                elif req == 2:
                    opts = models.PopulationsModels.r504.field.choices
                elif req == 3:
                    opts = models.PopulationsModels.r505.field.choices
                elif req == 4:
                    opts = models.PopulationsModels.r517.field.choices
                elif req == 5:
                    opts = models.PopulationsModels.r518.field.choices
                elif req == 6:
                    opts = models.PopulationsModels.r510.field.choices
                elif req == 7:
                    opts = models.PopulationsModels.r511.field.choices
                elif req == 8:
                    opts = models.PopulationsModels.r512.field.choices
                elif req == 9:
                    opts = models.PopulationsModels.r513.field.choices
                elif req == 10:
                    opts = models.PopulationsModels.r519.field.choices
                else:
                    opts = models.PopulationsModels.r520a.field.choices
                    
                html = '<option value="">----</option>'
                for opt in opts:
                    html += f'<option value="{opt[0]}">{opt[1]}</option>'

                return JsonResponse({"data": html}, status=200)
            
        return JsonResponse({'status': 'Invalid request'}, status=400)

class ManajemenPopulationsClassView(LoginRequiredMixin, View): 
        
    def get(self, request):
        pencacah = models.OfficerModels.objects.filter(role = '1').all()
        pemeriksa = models.OfficerModels.objects.filter(role = '2').all()
        hasil = models.FamiliesModels.r206.field.choices

        filters = [
            [1, 'Jenis Kelamin'],
            [2, 'Hubungan dengan Kepala Rumah Tangga'],
            [3, 'Keberadaan Anggota Keluarga'],
            [4, 'Partisipasi Sekolah'],
            [5, 'Pendidikan Terakhir'],
            [6, 'Status Pernikahan'],
            [7, 'Agama'],
            [8, 'Suku'],
            [9, 'Kegiatan Utama ART'],
            [10, 'Kepemikikan Jaminan Kesehatan'],
            [11, 'Keterangan Disabilitas']
        ]
        
        context = {
            'title' : 'Manajemen Penduduk',
            'pencacah' : pencacah,
            'pemeriksa' : pemeriksa,
            'hasil' : hasil,
            'filters' : filters,
            'province_regions' : models.RegionAdministrativeModels.objects.annotate(text_len=Length('reg_code')).filter(text_len=2).order_by('reg_code')
   
        }
       
        return render(request, 'app/master/master-penduduk.html', context)

class ManajemenPopulationsAddClassView(LoginRequiredMixin, View):

    def get(self, request):
        
        context = {
            'title' : 'Manajemen Penduduk',
            'form'  : forms.PopulationsForm(),
            'province_regions' : models.RegionAdministrativeModels.objects.annotate(text_len=Length('reg_code')).filter(text_len=2).order_by('reg_code')
        }
        return render(request, 'app/master/master-penduduk-add.html', context)
    
    def post(self, request):
        
        is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'

        if is_ajax:
            if request.method == 'POST':

                data_art = json.loads(request.POST.get('form_art'))
                data_art = helpers.transform_data(data_art)
                forms_errors = dict()

                form_art = forms.PopulationsForm(data_art[0])
                if form_art.is_valid() is False:
                    for key, val in form_art.errors.items():
                        forms_errors[key] = val

                if len(forms_errors) > 0:
                    return JsonResponse({"status": 'failed', "error": forms_errors}, status=400)

                family = list(models.PopulationsModels.objects.filter(family_id=data_art[0]['family_id']).values_list('r504', flat=True))
                if data_art[0]['r504'] == '1':
                    if '1' in family:
                        forms_errors['r504'] = ['Keluarga hanya bisa memiliki 1 kepala keluarga (terdapat ART lain berstatus kepala keluarga)']
                        return JsonResponse({"status": 'failed', "error": forms_errors}, status=400)

                form_art.save()
                return JsonResponse({"status": f'Data ART {data_art[0]["r503"]} berhasil ditambahkan'}, status=200)

        return JsonResponse({'status': 'Invalid request'}, status=400)
    

class ManajemenPopulationsEditClassView(LoginRequiredMixin, View):

    def get(self, request):

        if request.GET.get('id') is not None:
            model = models.PopulationsModels.objects.filter(pk = int(request.GET.get('id')))
            if model.exists():
                model = model.first()
                form = forms.PopulationsForm(instance=model)

                context = {
                    'title' : 'Edit Data Penduduk',
                    'pk' : model.pk,
                    'form' : form,
                }

                return render(request, 'app/master/master-penduduk-edit.html', context)
            
        return redirect('app:mnj_population')
    
    def post(self, request):
        
        is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'

        if is_ajax:
            if request.method == 'POST':
                
                data = json.loads(request.POST.get('form_art'))
                data_art = helpers.transform_data(data)[0]

                if data[0].get('id') is not None:
                    instance = models.PopulationsModels.objects.filter(pk = int(data_art['id']))

                    data_art['family_id'] = instance.first().family_id
                    data_art['art_id'] = instance.first().pk

                    forms_errors = dict()

                    if instance.exists():
                        form = forms.PopulationsForm(data_art, instance=instance.first())
                        if form.is_valid() is False:
                            for key, val in form.errors.items():
                                forms_errors[key] = val

                        if len(forms_errors) > 0:
                            return JsonResponse({"status": 'failed', "error": forms_errors}, status=400)

                        family = list(models.PopulationsModels.objects.filter(family_id=instance.first().family_id).exclude(Q(pk=instance.first().id)).values_list('r504', flat=True))

                        if data_art['r504']  == '1' and data_art['r504'] != instance.first().r504:
                            if '1' in family:
                                forms_errors['r504'] = ['Keluarga hanya bisa memiliki 1 kepala keluarga (terdapat ART lain berstatus kepala keluarga)']
                                return JsonResponse({"status": 'failed', "error": forms_errors}, status=400)

                        form.save()
                        return JsonResponse({"status": f'Data ART {data_art["r503"]} berhasil diupdate'}, status=200)

        return JsonResponse({'status': 'Invalid request'}, status=400)
    
class ManajemenPopulationsFetchNumClassView(LoginRequiredMixin, View):

    def post(self, request):
        is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
        if is_ajax:
            if request.method == 'POST':
                model = models.PopulationsModels.objects.filter(family_id = int(request.POST.get('id'))).order_by('-r501')
                last_num = model.first().r501 + 1
                return JsonResponse({'status' : 'success', 'message': last_num})

        return JsonResponse({'status': 'Invalid request'}, status=400)

class ManajemenPopulationsDeleteClassView(LoginRequiredMixin, View):

    def post(self, request):
        is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
        if is_ajax:
            if request.method == 'POST':
                model = get_object_or_404(models.PopulationsModels, pk = int(request.POST.get('pk')))
                old_data = model.r503
                model.delete()
                return JsonResponse({'status' : 'success', 'message': f'Data <b>{old_data}</b> berhasil dihapus'})

        return JsonResponse({'status': 'Invalid request'}, status=400)



class ManajemenPopulationFetchTableClassView(LoginRequiredMixin, View):

    def post(self, request):
        
        data = self._datatables(request)
        return HttpResponse(json.dumps(data, cls=DjangoJSONEncoder), content_type='application/json')
		
    def _datatables(self, request):
        
        # Define default column for ordering first request
        def_col = 'r503' 

        datatables = request.POST

        # Get Draw
        draw = int(datatables.get('draw'))
        start = int(datatables.get('start'))
        search = datatables.get('search[value]')

        order_idx = int(datatables.get('order[0][column]')) # Default 1st index for
        order_dir = datatables.get('order[0][dir]') # Descending or Ascending
        order_col = 'columns[' + str(order_idx) + '][data]'
        order_col_name = datatables.get(order_col)

        if 'no' in order_col_name:
            order_col_name = def_col

        if (order_dir == "desc"):
            order_col_name =  str('-' + order_col_name)

        model = models.PopulationsModels.objects

        id_def_data = list(model.order_by(def_col).values_list('id'))
        id_def_data = [list((idx+1, ) + id_def_data[idx]) for idx in range(len(id_def_data))]
        
        records_total = model.count()
        records_filtered = records_total
        
        if datatables.get('region'):
            model = model.filter(family_id__r104__reg_code__icontains = datatables.get('region'))

        if datatables.get('region_sls'):
            model = model.filter(family_id__r105__reg_sls_code__icontains = datatables.get('region_sls'))

        if datatables.get('r201'):
            model = model.filter(family_id__r201 = datatables.get('r201'))

        if datatables.get('r204'):
            model = model.filter(family_id__r204 = datatables.get('r204'))

        if datatables.get('r206'):
            model = model.filter(family_id__r206 = datatables.get('r206'))

        if datatables.get('filter'):
            req, val = datatables.get('filter').split('_')

            if req == '1':
                model = model.filter(r506 = val)
            elif req == '2':
                model = model.filter(r504 = val)
            elif req == '3':
                model = model.filter(r505 = val)
            elif req == '4':
                model = model.filter(r517 = val)
            elif req == '5':
                model = model.filter(r518 = val)
            elif req == '6':
                model = model.filter(r510 = val)
            elif req == '7':
                model = model.filter(r511 = val)
            elif req == '8':
                model = model.filter(r512 = val)
            elif req == '9':
                model = model.filter(r513 = val)
            elif req == '10':
                model = model.filter(r519 = val)
            else:
                model = model.filter(
                    Q(r520a = val) |
                    Q(r520b = val) |
                    Q(r520c = val) |
                    Q(r520d = val) |
                    Q(r520e = val) |
                    Q(r520f = val) |
                    Q(r520g = val) |
                    Q(r520h = val)
                )

        if search:
            model = model.filter(
                Q(r503__icontains=search) |
                Q(r502__icontains=search) |
                Q(r508__icontains=search) |
                Q(r518__icontains=search)|
                Q(r504__icontains=search) |
                Q(r505__icontains=search)
            )

            records_total = model.count()
            records_filtered = records_total
        
        model = model.order_by(order_col_name)
            
        # Conf Paginator
        length = int(datatables.get('length')) if int(datatables.get('length')) > 0 else len(model)
        page_number = int(start / length + 1)
        paginator = Paginator(model, length)

        try:
            object_list = paginator.page(page_number).object_list
        except PageNotAnInteger:
            object_list = paginator.page(1).object_list
        except EmptyPage:
            object_list = paginator.page(1).object_list

        data = []

        for obj in object_list:
             
            data.append(
            {
                'no': [x for x in id_def_data if obj.id == x[1]][0][0],
                'r503' : obj.r503,
                'r502': obj.r502,
                'r508': obj.age,
                'r518' : obj.get_r518_display(),
                'r504' : obj.get_r504_display(),
                'r505' : obj.get_r505_display(),
                'actions': f'<a href="{reverse_lazy("app:mnj_population_edit")}?id={obj.id}" target="_blank" class="btn btn-sm icon btn-edit p-0" data-id="{obj.id}"><i class="mdi mdi-account-edit"></i></a>\
                <button class="btn btn-sm icon btn-delete p-0" data-id="{obj.id}"><i class="mdi mdi-trash-can-outline"></i></button>'
            })

        return {    
            'draw': draw,
            'recordsTotal': records_total,
            'recordsFiltered': records_filtered,
            'data': data,
        }

