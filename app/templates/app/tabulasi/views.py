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


class TabulationsClassView(LoginRequiredMixin, View):
    
    def get(self, request):

        families = models.FamiliesModels.objects.all()
        pprint(families[0].r104.reg_name)
        context = {
            'title' : 'Tabulasi Data',
            'families' : families
        }
        return render(request, 'app/tabulasi/tabulasi-keluarga.html', context)