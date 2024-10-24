# todo/todo_api/urls.py : API urls.py
from django.urls import path
from .views import (
    PopulationsListApiView,
    CustomObtainPairView
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

app_name = 'restapi'
urlpatterns = [
    path('api', PopulationsListApiView.as_view()),
    path('api/token/', CustomObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]