# todo/todo_api/urls.py : API urls.py
from django.urls import path
from .views import (
    PopulationsListApiView,
    CustomObtainPairView,
    RestApiTest
)
from rest_framework_simplejwt.views import  TokenRefreshView

app_name = 'api'
urlpatterns = [
    path('api', PopulationsListApiView.as_view(), name='api_gate'),
    path('api/token', CustomObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/test', RestApiTest.as_view(), name='api_test'),
]