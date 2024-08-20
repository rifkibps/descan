from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from . import models, helpers
from django.http import JsonResponse
from pprint import pprint
from django.db.models import Q, Count


# Create your views here.
class DashboardClassView(LoginRequiredMixin, View):
    
    def get(self, request):
        context = {
            'title' : 'Halaman Dashboard'
        }
        return render(request, 'app/dashboard/dashboard.html', context)


class TabulationsFamiliesClassView(LoginRequiredMixin, View):
    
    def get(self, request):

        families = models.FamiliesModels.objects.count()
        populations = len(models.PopulationsModels.objects.all())
        welfare_recips = helpers.count_of_welfare_recips().count()
        labor_force = helpers.labor_participation()

        education_levels = models.PopulationsModels.r415.field.choices
        home_ownership_state = models.FamiliesModels.r301a.field.choices

        tabulations = helpers.get_tab_families()
        context = {
            'title' : 'Tabulasi Data Keluarga',
            'families' : families,
            'populations' : populations,
            'welfare_recips' : welfare_recips,
            'labor_force' : labor_force,
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
                # Kloset

        return JsonResponse({'status': 'Invalid request'}, status=400)



class TabulationsPopulationsClassView(LoginRequiredMixin, View):
    
    def get(self, request):

        families = models.FamiliesModels.objects.all()
        context = {
            'title' : 'Tabulasi Data Penduduk',
            'families' : families
        }
        return render(request, 'app/tabulasi/tabulasi-penduduk.html', context)
