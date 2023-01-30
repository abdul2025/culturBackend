from django.contrib import admin
from .models import *
from core.utility import linkify

# Register your models here.

class TracksAdmin(admin.ModelAdmin):
    model = Tracks
    list_display = [
        'name',
        'created_at',
    ]
    list_filter = [
        'name',
        'created_at',
    ]
class PhaseAdmin(admin.ModelAdmin):
    model = Phase
    list_display = [
        'name',
        'get_track',
        'created_at',
    ]
    list_filter = [
        'name',
        'created_at',
    ]

    @admin.display(ordering='tracks__name', description='Tracks')
    def get_track(self, obj):
        return obj.tracks.name


class PillarAdmin(admin.ModelAdmin):
    model = Pillar
    list_display = [
        'name',
        'phase',
        'weight',
        'created_at',

    ]
    list_filter = [
        'name',
        'phase',
        'weight',
        'created_at',
    ]
class PallarStanderAdmin(admin.ModelAdmin):
    model = PallarStander
    list_display = [
        'name',
        linkify(field_name='pillar'),
        'created_at',
    ]
    list_filter = [
        'name',
        'created_at',
    ]

class ScreeningAdmin(admin.ModelAdmin):
    model = Screening
    list_display = [
        'name',
        linkify(field_name='tracks'),
        'created_at',
    ]
    list_filter = [
        'name',
        'created_at',
    ]


admin.site.register(Tracks, TracksAdmin)
admin.site.register(Phase, PhaseAdmin)
admin.site.register(Pillar, PillarAdmin)
admin.site.register(PallarStander, PallarStanderAdmin)
admin.site.register(Screening, ScreeningAdmin)