from django.urls import path
from . import views

app_name = 'app'
urlpatterns = [
    path('', views.DashboardClassView.as_view(), name="dashboard"),
    path('tabulasi/keluarga', views.TabulationsFamiliesClassView.as_view(), name="tab_families"),
    path('tabulasi/penduduk', views.TabulationsPopulationsClassView.as_view(), name="tab_populations"),
    path('tabulasi/keluarga/fetch-data', views.TabulationsFamiliesFetchClassView.as_view(), name="tab_families_fetch"),
    path('tabulasi/penduduk/fetch-data', views.TabulationsPopulationsFetchClassView.as_view(), name="tab_populations_fetch"),

    path('manajemen-keluarga/', views.ManajemenFamiliesClassView.as_view(), name="mnj_families"),
    path('manajemen-keluarga/keluarga-baru', views.FamiliesAddClassView.as_view(), name="mnj_families_add"),
    
    path('manajemen-penduduk/', views.ManajemenPopulationsClassView.as_view(), name="mnj_population"),
]

