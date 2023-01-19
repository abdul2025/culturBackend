from django.contrib import admin
from .models import *
# Register your models here.

class CandidateProfileAdmin(admin.ModelAdmin):
    model = CandidateProfile
    list_display = [
        'user',
        'national_id',
        'city',
        'region',
        'is_saudi',
        'gender',
        'status',
    ]
    list_filter = [
        'user',
        'created_at',
    ]
class CandidateApplicationAdmin(admin.ModelAdmin):
    model = CandidateApplication
    list_display = [
        'profile',
        'participation_title',
        'score'

    ]
    list_filter = [
        'created_at',
    ]

class CandidateTrackApplicationAdmin(admin.ModelAdmin):
    model = CandidateTrackApplication
    list_display = [
        'application',
        'phase',

    ]
    list_filter = [
        'created_at',
    ]

class CandidatePillarInline(admin.TabularInline):
    model = CandidatePillar
    extra = 0
    exclude = ['hidden']
    list_display = [
        'candidate_phase',
        'questions',
        # 'number_of_judges'
    ]
    list_filter = [
        'created_at',
    ]


class CandidatePillarAdmin(admin.ModelAdmin):
    model = CandidatePillar
    list_display = [
        'candidate_phase',
        'questions',
        # 'number_of_judges'
    ]
    list_filter = [
        'created_at',
    ]


class CandidatePhaseAdmin(admin.ModelAdmin):
    model = CandidatePhase
    inlines = [CandidatePillarInline]
    list_display = [
        'application',
        'pillar',
        'score',
        # 'number_of_judges'
    ]
    list_filter = [
        'created_at',
    ]

admin.site.register(CandidateProfile, CandidateProfileAdmin)
admin.site.register(CandidateApplication, CandidateApplicationAdmin)
admin.site.register(CandidateTrackApplication, CandidateTrackApplicationAdmin)
admin.site.register(CandidatePhase, CandidatePhaseAdmin)
admin.site.register(CandidatePillar, CandidatePillarAdmin)

