from django.urls import path
from . import views


urlpatterns = [
    path('app/', views.DashboardClassView.as_view(), name="dashboard")
]

