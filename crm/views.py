from django.shortcuts import render
from rest_framework import generics
from .models import *
from accounts.models import GroupEnum
from .serializers import *
from .queries import *
from .services import CrmService
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser

# Create your views here.

class ListTracksView(generics.ListAPIView):
    queryset = Tracks.objects.all()
    serializer_class = TracksCustomSerializer
    # permission_classes = [IsAdminUser]


class RetriveTracksView(APIView):
    """List tracks per user group"""
    # permission_classes = [IsAdminUser]
    def get(self, request):
        tracks = []
        for i in list(request.user.groups.all()):
            if str(i) == GroupEnum.SORT_GROUP.value:
                tracks.append(CrmService.getsortTracksbyUser(user=request.user))
            if str(i) == GroupEnum.FILTERING_GROUP.value:
                tracks.append(CrmService.getfilteringTracksbyUser(user=request.user))
            if str(i) == GroupEnum.JUDGEMENT_GROUP.value:
                tracks.append(CrmService.getJudgeTracksbyUser(request.user))

        flat_list = [item for sublist in tracks for item in sublist]
        tracks = CrmService.getTrackInstances(ids=flat_list)
        serializer = TracksCustomSerializer(tracks, many=True)

        return Response(serializer.data)


# class ListPhasesView(APIView):
#     # permission_classes = [IsAuthenticated]

#     def get(self, request, pk):
#         track = get_track(id=pk)
#         phase = get_phase_by_track(id=track)
#         serializer = PhaseSerializer(phase, many=True)

#         return Response(serializer.data)


# class ListPillarView(APIView):
#     # permission_classes = [IsAuthenticated]

#     def get(self, request, pk):
#         phase = get_phase(id=pk)
#         phase = get_pillar_by_phase(phase=phase)
#         serializer = PillarSerializer(phase, many=True)


#         return Response(serializer.data)

# class ListScreeningView(APIView):
#     # permission_classes = [IsAuthenticated]

#     def get(self, request, pk):
#         track = get_track(id=pk)
#         screening = get_screening_by_track(track=track)
#         serializer = ScreeningSerializer(screening, many=True)

#         return Response(serializer.data)


