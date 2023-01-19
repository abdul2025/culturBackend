from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *
from .queries import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser

# Create your views here.

class ListProfilesView(generics.ListAPIView):
    queryset = CandidateProfile.objects.all()
    serializer_class = ProfileSerializer
    # permission_classes = [IsAdminUser]

class RetriveProfilesView(APIView):
    # queryset = CandidateProfile.objects.all()
    # serializer_class = ProfileSerializer
    # permission_classes = [IsAdminUser]
    def get(self, request, pk):
        profile = get_profile(id=pk)
        serializer = ProfileSerializer(profile)

        return Response(serializer.data)

