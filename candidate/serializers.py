from rest_framework import serializers
from .models import *
from accounts.serializers import CustomUserSerializer
from crm.serializers import *


excludeFields = ('created_at', 'modified_at', 'hidden')

class CandidateCustomApplicationSerializer(serializers.ModelSerializer):
    track = TracksSerializer()

    rated = serializers.SerializerMethodField()
    track_name = serializers.SerializerMethodField()

    def get_track_name(self, obj):
        return obj.track.name

    def get_rated(self, obj):
        # check if user already submitted a subapp for this as reviwer
        request = self.context.get('request', None)
        subapps = list(obj.candidates_application.all())
        if subapps:
            for sub in subapps:
                print(type(request.user))
                if request.user == sub.reviewer:
                    return True
        else:
            return False
    class Meta:
        model = CandidateApplication
        exclude = excludeFields


class CandidateAppSerializer(serializers.ModelSerializer):
    candidate_name = serializers.SerializerMethodField()
    rated = serializers.SerializerMethodField()
    track_name = serializers.SerializerMethodField()

    def get_candidate_name(self, obj):
        return obj.profile.user.name
    def get_track_name(self, obj):
        return obj.track.name

    def get_rated(self, obj):
        # check if user already submitted a subapp for this as reviwer
        request = self.context.get('request', None)
        subapps = list(obj.candidates_application.all())
        if subapps:
            for sub in subapps:
                if request.user == sub.reviewer:
                    return True
        else:
            return False



    class Meta:
        model = CandidateApplication
        exclude = excludeFields




class ProfileSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()
    # applications = serializers.SerializerMethodField()

    # def get_applications(self, obj):
    #     return CandidateApplicationSerializer(obj.applications, many=True).data
    class Meta:
        model = CandidateProfile
        exclude = excludeFields

class CandidateScreeningSerializer(serializers.ModelSerializer):
    class Meta:
        model = CandidateScreening
        exclude = excludeFields

class CandidateSubApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CandidateSubApplication
        exclude = excludeFields



class CandidateStandersSerializer(serializers.ModelSerializer):
    highest_rate_score = serializers.SerializerMethodField()

    def get_highest_rate_score(self, obj):
        # pillarStanders = list(obj.pillar.pallarStander.all())


        ### This has bad smell of retriving by name


        standers = PallarStander.objects.filter(name=obj.stander_name)

        numberOfQuestions = 0
        ### Calculate questions weight
        for stander in standers:
            numberOfQuestions += len(stander.pillarStanderQuestions)
        questionHighestWeight = round(stander.pillar.weight / numberOfQuestions, 2)
        return questionHighestWeight


    class Meta:
        model = CandidateStanders
        exclude = excludeFields








class CandidatePillarSubApplicationSerializer(serializers.ModelSerializer):
    standers = serializers.SerializerMethodField()

    def get_standers(self, obj):
        standers = CandidateStanders.objects.filter(candidate_pillar=obj)
        return CandidateStandersSerializer(standers, many=True).data
    class Meta:
        model = CandidatePillarSubApplication
        exclude = excludeFields



class CustomCandidateSubApplicationSerializer(serializers.ModelSerializer):
    pillars = serializers.SerializerMethodField()

    #### include all canidates pillars and standers
    def get_pillars(self, obj):
        pillars = CandidatePillarSubApplication.objects.filter(sub_application=obj)
        return CandidatePillarSubApplicationSerializer(pillars, many=True).data
    class Meta:
        model = CandidateSubApplication
        exclude = excludeFields


class CandidateCaptureAppSerializer(serializers.ModelSerializer):
    candidate_name = serializers.SerializerMethodField()
    phases = serializers.SerializerMethodField()


    def get_candidate_name(self, obj):
        return obj.profile.user.name

    def get_phases(self, obj):
        subapp = CandidateSubApplication.objects.filter(application=obj)
        return CustomCandidateSubApplicationSerializer(subapp, many=True).data
    class Meta:
        model = CandidateApplication
        exclude = excludeFields