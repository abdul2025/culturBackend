from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *
from .queries import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser

# Create your views here.

class ListTracksView(generics.ListAPIView):
    queryset = Tracks.objects.all()
    serializer_class = TracksSerializer
    # permission_classes = [IsAdminUser]


class ListPhasesView(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        track = get_track(id=pk)
        phase = get_phase_by_track(id=track)
        serializer = PhaseSerializer(phase, many=True)

        return Response(serializer.data)


class ListPillarView(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        phase = get_phase(id=pk)
        phase = get_pillar_by_phase(phase=phase)
        serializer = PillarSerializer(phase, many=True)


        return Response(serializer.data)

class ListScreeningView(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        track = get_track(id=pk)
        screening = get_screening_by_track(track=track)
        serializer = ScreeningSerializer(screening, many=True)

        return Response(serializer.data)


