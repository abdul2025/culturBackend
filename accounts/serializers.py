from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .services import AccountService
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
        return AccountService.optain_access_token(
            user=user,
            group=GroupEnum.REGULAR_GROUP,
            token=token
        )

class CandidateTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        return AccountService.optain_access_token(
            user=user,
            group=GroupEnum.CANDIDATE_GROUP,
            token=token
        )