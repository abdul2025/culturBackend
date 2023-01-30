from .models import LoginLog, GroupEnum, CustomUser
from core.errors import Error, APIError

class AccountService:

#     @staticmethod
#     def optain_regular_access_token(user: CustomUser, token: dict) -> dict:
#         if not user.groups.filter(name=GroupEnum.REGULAR_GROUP.value).exists():
#             raise APIError(Error.NO_ACTIVE_ACCOUNT)
#         # Add custom claims
#         token['roles'] = list(user.groups.all().values())
#         return token


#     @staticmethod
#     def optain_candidate_access_token(user: CustomUser, token: dict) -> dict:
#         if not user.groups.filter(name=GroupEnum.CANDIDATE_GROUP.value).exists():
#             raise APIError(Error.NO_ACTIVE_ACCOUNT)
#         # Add custom claims
#         token['roles'] = list(user.groups.all().values())
#         return token


#     @staticmethod
#     def optain_access_token(group: GroupEnum, user: CustomUser, token: dict) -> dict:

#         if user.is_blocked:
#             raise APIError(Error.BLOCKED_USER)
#         if group == GroupEnum.REGULAR_GROUP:
#             return AccountService.optain_regular_access_token(
#                 user=user, token=token)
#         if group == GroupEnum.CANDIDATE_GROUP:
#             return AccountService.optain_candidate_access_token(
#                 user=user, token=token)
#         else:
#             raise APIError(Error.NO_ACTIVE_ACCOUNT)

    @staticmethod
    def login(email: str) -> None:
        LoginLog.objects.create(email=email)