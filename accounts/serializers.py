from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import GroupEnum
from rest_framework import serializers
from .models import CustomUser




class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('name', 'phone_number', 'email', )

class RugularTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['group'] = list(user.groups.all().values())
        return token
