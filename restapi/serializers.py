from rest_framework import serializers
from app import models
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .permissions import DeveloperPermission

class TokenObtainSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        permission_classes = [DeveloperPermission(self.user).has_permission()]

        refresh = self.get_token(self.user)

        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)
        data["status"] = "success"

        return data

class PopulationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PopulationsModels
        fields = "__all__"