from django.urls import path
from . import views

app_name = 'app'
urlpatterns = [
    path('', views.DashboardClassView.as_view(), name="dashboard"),
    path('fetch-region/', views.RegionFetchDataClassView.as_view(), name="fetch-region"),
    path('tabulasi/keluarga', views.TabulationsFamiliesClassView.as_view(), name="tab_families"),
    path('tabulasi/penduduk', views.TabulationsPopulationsClassView.as_view(), name="tab_populations"),
    path('tabulasi/keluarga/fetch-data', views.TabulationsFamiliesFetchClassView.as_view(), name="tab_families_fetch"),
    path('tabulasi/penduduk/fetch-data', views.TabulationsPopulationsFetchClassView.as_view(), name="tab_populations_fetch"),

    path('manajemen-keluarga/', views.ManajemenFamiliesClassView.as_view(), name="mnj_families"),
    path('manajemen-keluarga/edit', views.ManajemenFamiliesEditClassView.as_view(), name="mnj_families_edit"),
    path('manajemen-keluarga/delete', views.ManajemenFamiliesDeleteClassView.as_view(), name="mnj_families_del"),
    path('manajemen-keluarga/keluarga-baru', views.ManajemenFamiliesAddClassView.as_view(), name="mnj_families_add"),
    
    path('manajemen-penduduk/', views.ManajemenPopulationsClassView.as_view(), name="mnj_population"),
    path('manajemen-penduduk/add', views.ManajemenPopulationsAddClassView.as_view(), name="mnj_population_add"),
    path('manajemen-penduduk/get_num', views.ManajemenPopulationsFetchNumClassView.as_view(), name="mnj_population_fetch_num"),
    path('manajemen-penduduk/delete', views.ManajemenPopulationsDeleteClassView.as_view(), name="mnj_population_del"),
    path('manajemen-penduduk/edit', views.ManajemenPopulationsEditClassView.as_view(), name="mnj_population_edit"),

    
]
