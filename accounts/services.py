from .models import LoginLog, GroupEnum, CustomUser
from core.errors import Error, APIError

class AccountService:

    @staticmethod
    def login(email: str) -> None:
        LoginLog.objects.create(email=email)