from rest_framework import serializers
from .models import *


excludeFields = ('created_at', 'modified_at', 'hidden')

class TracksSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tracks
        exclude = excludeFields

class PhaseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Phase
        exclude = excludeFields

class PallarStanderSerializer(serializers.ModelSerializer):

    class Meta:
        model = PallarStander
        exclude = excludeFields

class PillarSerializer(serializers.ModelSerializer):
    pallarStander = PallarStanderSerializer(many=True)
    phase = PhaseSerializer()

    class Meta:
        model = Pillar
        exclude = excludeFields







class ScreeningSerializer(serializers.ModelSerializer):

    class Meta:
        model = Screening
        exclude = excludeFields