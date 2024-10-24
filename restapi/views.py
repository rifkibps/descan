from django.views import View
from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from app import models
from .serializers import PopulationsSerializer, TokenObtainSerializer
from .permissions import DeveloperBasePermission
from rest_framework_simplejwt.views import TokenObtainPairView

class CustomObtainPairView(TokenObtainPairView):
    serializer_class = TokenObtainSerializer
 
class PopulationsListApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated, DeveloperBasePermission]
    
    def get(self, request, *args, **kwargs):
        '''
        List all the populations
        '''
        populations = models.PopulationsModels.objects
        serializer = PopulationsSerializer(populations, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
import os
import requests as req
import json

class RestApiTest(View):

    def get(self, request):
        token = {
            'access' : 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI5NzgzNDczLCJpYXQiOjE3Mjk3ODMxNzMsImp0aSI6ImUxYjVjYWNkZGZiYTQ2MDhiYjYzYTZlYWM3YWQ0OThkIiwidXNlcl9pZCI6MTN9.OM7I9EC1R0wAtdB5cG-zPlo_5iDFDQ4jBlMh-P03tLAl',
            'refresh' : 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTczNzU1OTE3MywiaWF0IjoxNzI5NzgzMTczLCJqdGkiOiJlNmQ4NjVjMzNjZGI0MTI5YTdiYzRiM2RkMzBmNTU1ZiIsInVzZXJfaWQiOjEzfQ.pVlbuQYxR82VnhSX6rmA0NyFrij52Mi5VYHyGpfGCrs1azxd'
        }
        
        state = False
        response = ''
        while (state is False):
            api = req.get('http://127.0.0.1:8000/api', headers={'Authorization':'Bearer %s' % token['access']})
            if api.status_code != 200:
                new_token = req.post('http://127.0.0.1:8000/api/token/refresh', data={'refresh' : token['refresh']})
                if new_token.status_code == 200:
                    json = new_token.json()
                    token['access'] = json['access']
                    token['refresh'] = json['refresh']
                else:
                    raise Exception("Sorry, it looks like your token has expired. Please log in to access the new token")
            else:
                response = api
                break
            
        return HttpResponse(response)
    