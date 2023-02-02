from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *
from .queries import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import viewsets
from .services import *


# Create your views here.

class ListProfilesView(generics.ListAPIView):
    queryset = CandidateProfile.objects.all()
    serializer_class = ProfileSerializer
    # permission_classes = [IsAdminUser]

class RetriveProfilesView(APIView):
    # permission_classes = [IsAdminUser]
    def get(self, request, pk):
        profile = get_profile(id=pk)
        serializer = ProfileSerializer(profile)

        return Response(serializer.data)

class ListCandidateApplicationsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, truckid):
        applications = get_applications(truckid=truckid, request=request)

        serializer = CandidateAppSerializer(applications, context={'request': request}, many=True)

        return Response(serializer.data)


class RetriveCandidateApplicationView(APIView):
    # permission_classes = [IsAdminUser]
    def get(self, request, pk):
        applications = get_application(id=pk)
        serializer = CandidateCustomApplicationSerializer(applications, context={'request': request})

        return Response(serializer.data)



class NewCndidateApplicationView(APIView):
    # permission_classes = [IsAdminUser]




    def get(self, request):
        appid = request.query_params.get('pk')
        applications = get_application(id=appid)
        serializer = CandidateCaptureAppSerializer(applications)
        return Response(serializer.data)

    def post(self, request):
        data = JSONParser().parse(request)
        stage = data.get('application_stage')
        appId = data.get('id')
        track = data.get('track')
        applications = get_application(id=appId)

        try:
            track['screening'][0]['questions']
            track['phases'][0]['name']
            track['phases'][0]['pillars']
            track['phases'][1]['name']
            track['phases'][1]['pillars']
        except Exception as er:
            raise APIError(Error.PHASE_NOT_FOUND, extra=[er])

        if stage == 0:
            data = {'application':appId,
                    'screening':track['screening'][0]['questions'],
                    'reviewer':request.user.id}
            serializer = CandidateScreeningSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)


        elif stage == 1:
            print("Filtering")
            sub_app = SubApplicationServices.CreateSubApplications(
                application=applications,
                ### 0 index of first phase as filtering
                phase=track['phases'][0]['name'],
                pillars=track['phases'][0]['pillars'],
                reviewer=request.user
            )
            serializer = CandidateCaptureAppSerializer(applications)
            return Response(serializer.data)


        else:
            print("judeging")
            sub_app = SubApplicationServices.CreateSubApplications(
                application=applications,
                ### 1 index of first phase as judeging
                phase=track['phases'][1]['name'],
                pillars=track['phases'][1]['pillars'],
                reviewer=request.user
            )
            serializer = CandidateCaptureAppSerializer(applications)
            return Response(serializer.data)

        # #### New Service
        ### Create SubApplication
        ### Create Pilllar
        ### Create Stander


    def patch(self, request):
        data = JSONParser().parse(request)
        if data is not None:
            questions = data.get('questions')
            app = SubApplicationServices.updateSubApplicationsQuestions(
                questions=questions,
            )
            serializer = CandidateCaptureAppSerializer(app)
            return Response(serializer.data)

class ScreeningCndidateApplicationView(viewsets.ViewSet):
    # permission_classes = [IsAdminUser]

    def retrieve(self, request, pk):
        applications = get_application(id=pk)
        screening = get_candidate_screening_by_app(app=applications)
        serializer = CandidateScreeningSerializer(screening, many=True)
        return Response(serializer.data)


    # def list(self, request):
    #     screenings = CandidateScreening.objects.all()
    #     serializer = CandidateScreeningSerializer(screenings, many=True)
    #     return Response(serializer.data)


    def create(self, request):
        data = JSONParser().parse(request)
        serializer = CandidateScreeningSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)






