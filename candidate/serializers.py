from rest_framework import serializers
from .models import *
from accounts.serializers import CustomUserSerializer
from crm.serializers import *


excludeFields = ('created_at', 'modified_at', 'hidden')
class CandidatePillarSubApplicationSerializer(serializers.ModelSerializer):
    pillar_name = PillarSerializer(read_only=True, many=True)
    pillar_stander = PallarStanderSerializer(read_only=True, many=True)


    def get_pillar_name(self, obj):
        return obj.pillar.name
    class Meta:
        model = CandidatePillarSubApplication
        exclude = excludeFields
class CandidateSubApplicationSerializer(serializers.ModelSerializer):
    phase_name = serializers.SerializerMethodField()
    phase_pillars = serializers.SerializerMethodField()


    def get_phase_name(self, obj):
        return obj.phase.name

    def get_phase_pillars(self, obj):
        return CandidatePillarSubApplicationSerializer(obj.candidates_pillar, many=True).data
    class Meta:
        model = CandidateSubApplication
        exclude = excludeFields

class CandidateApplicationSerializer(serializers.ModelSerializer):
    sub_application_phases = serializers.SerializerMethodField()
    track_name = serializers.SerializerMethodField()

    def get_sub_application_phases(self, obj):
        return CandidateSubApplicationSerializer(obj.candidates_tracks, many=True).data

    def get_track_name(self, obj):
        return obj.track.name
    class Meta:
        model = CandidateApplication
        exclude = excludeFields



class CandidateAppSerializer(serializers.ModelSerializer):
    class Meta:
        model = CandidateApplication
        exclude = excludeFields


class ProfileSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()
    applications = serializers.SerializerMethodField()

    def get_applications(self, obj):
        return CandidateApplicationSerializer(obj.applications, many=True).data
    class Meta:
        model = CandidateProfile
        exclude = excludeFields




# class PhaseSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Phase
#         exclude = excludeFields

# class PallarStanderSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = PallarStander
#         exclude = excludeFields

# class PillarSerializer(serializers.ModelSerializer):
#     pallarStander = PallarStanderSerializer(many=True)
#     phase = PhaseSerializer()

#     class Meta:
#         model = Pillar
#         exclude = excludeFields







# class ScreeningSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Screening
#         exclude = excludeFields