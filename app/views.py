from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from . import models, helpers
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

        families = models.FamiliesModels.objects.count()
        populations = len(models.PopulationsModels.objects.all())
        welfare_recips = helpers.count_of_welfare_recips().count()
        labor_force = helpers.labor_participation()

        education_levels = models.PopulationsModels.r415.field.choices
        home_ownership_state = models.FamiliesModels.r301a.field.choices
        context = {
            'title' : 'Tabulasi Data Keluarga',
            'families' : families,
            'populations' : populations,
            'welfare_recips' : welfare_recips,
            'labor_force' : labor_force,
            'education_levels' : education_levels,
            'home_ownership_state' : home_ownership_state
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
