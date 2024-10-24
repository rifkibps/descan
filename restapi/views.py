from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from app import models
from .serializers import PopulationsSerializer, TokenObtainSerializer
from .permissions import DeveloperPermission
from rest_framework_simplejwt.views import TokenObtainPairView


class CustomObtainPairView(TokenObtainPairView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = TokenObtainSerializer


class PopulationsListApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated, DeveloperPermission]
    
    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the populations
        '''

        populations = models.PopulationsModels.objects
        serializer = PopulationsSerializer(populations, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
