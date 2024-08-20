from django.urls import path
from . import views

app_name = 'app'
urlpatterns = [
    path('app/', views.DashboardClassView.as_view(), name="dashboard"),
    path('tabulasi/keluarga', views.TabulationsFamiliesClassView.as_view(), name="tab_families"),
    path('tabulasi/keluarga/fetch-data', views.TabulationsFamiliesFetchClassView.as_view(), name="tab_families_fetch"),


    path('tabulasi/penduduk', views.TabulationsPopulationsClassView.as_view(), name="tab_populations"),
    path('manajemen-keluarga/', views.TabulationsFamiliesClassView.as_view(), name="mnj_families"),
    path('manajemen-penduduk/', views.TabulationsPopulationsClassView.as_view(), name="mnj_population"),
]

