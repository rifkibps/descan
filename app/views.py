from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class DashboardClassView(LoginRequiredMixin, View):
    
    def get(self, request):
        context = {
            'title' : 'Halaman Dashboard'
        }
        return render(request, 'app/dashboard.html', context)
