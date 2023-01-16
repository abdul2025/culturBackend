from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .services import AccountService
from .models import GroupEnum


class RugularTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        return AccountService.optain_access_token(
            user=user,
            group=GroupEnum.REGULAR_GROUP,
            token=token
        )