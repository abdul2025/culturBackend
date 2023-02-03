from rest_framework import serializers
from .models import *


excludeFields = ('created_at', 'modified_at', 'hidden')

class TracksSerializer(serializers.ModelSerializer):
    phases = serializers.SerializerMethodField()
    screening = serializers.SerializerMethodField()


    def get_phases(self, obj):
        return PhaseSerializer(obj.tracks, many=True).data

    def get_screening(self, obj):
        return ScreeningSerializer(obj.tracks_screening, many=True).data

    class Meta:
        model = Tracks
        exclude = excludeFields


class TracksCustomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tracks
        exclude = excludeFields



class PhaseSerializer(serializers.ModelSerializer):
    pillars = serializers.SerializerMethodField()



    def get_pillars(self, obj):
        return PillarSerializer(obj.phases, many=True).data

    class Meta:
        model = Phase
        exclude = excludeFields

class PallarStanderSerializer(serializers.ModelSerializer):
    highest_rate_score = serializers.SerializerMethodField()

    def get_highest_rate_score(self, obj):
        # pillarStanders = list(obj.pillar.pallarStander.all())
        print(obj.pillar)
        standers = PallarStander.objects.filter(pillar=obj.pillar)
        numberOfQuestions = 0
        ### Calculate questions weight
        for stander in standers:
            numberOfQuestions += len(stander.pillarStanderQuestions)
        questionHighestWeight = round(obj.pillar.weight / numberOfQuestions, 2)
        return questionHighestWeight
    class Meta:
        model = PallarStander
        exclude = excludeFields

class PillarSerializer(serializers.ModelSerializer):
    pillar_standers = serializers.SerializerMethodField()


    def get_pillar_standers(self, obj):
        return PallarStanderSerializer(obj.pillar, many=True).data

    class Meta:
        model = Pillar
        exclude = ('created_at', 'modified_at', 'hidden')

class ScreeningSerializer(serializers.ModelSerializer):

    class Meta:
        model = Screening
        fields = ('questions',)