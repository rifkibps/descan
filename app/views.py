from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from . import models
from pprint import pprint
# Create your views here.
class DashboardClassView(LoginRequiredMixin, View):
    
    def get(self, request):
        context = {
            'title' : 'Halaman Dashboard'
        }
        return render(request, 'app/dashboard/dashboard.html', context)


class TabulationsFamiliesClassView(LoginRequiredMixin, View):
    
    def get(self, request):

        families = models.FamiliesModels.objects.all()
        context = {
            'title' : 'Tabulasi Data Keluarga',
            'families' : families
        }
        return render(request, 'app/tabulasi/tabulasi-keluarga.html', context)
    
class TabulationsPopulationsClassView(LoginRequiredMixin, View):
    
    def get(self, request):

        families = models.FamiliesModels.objects.all()
        context = {
            'title' : 'Tabulasi Data Penduduk',
            'families' : families
        }
        return render(request, 'app/tabulasi/tabulasi-penduduk.html', context)
