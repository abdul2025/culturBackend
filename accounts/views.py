from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from .serializers import *
from .services import AccountService
# Create your views here.


class RugularTokenObtainPairView(TokenObtainPairView):

    def post(self, request):
        print(request.data)
        serializer = RugularTokenObtainPairSerializer(
            data=request.data)
        serializer.is_valid(raise_exception=True)
        AccountService.login(request.data.get('username'))
        return Response(serializer.validated_data)



