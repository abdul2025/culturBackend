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

class CandidateSubApplicationInline(admin.TabularInline):
    model = CandidateSubApplication
    extra = 0
    exclude = ['hidden']
    list_display = [
        'application',
        'phase',
        'phase_score',
        'reviewer',
    ]
    list_filter = [
        'created_at',
    ]

class CandidateSubApplicationAdmin(admin.ModelAdmin):
    model = CandidateSubApplication
    list_display = [
        'application',
        'phase',
        'phase_score',
        'reviewer',
    ]
    list_filter = [
        'created_at',
    ]


class CandidateApplicationAdmin(admin.ModelAdmin):
    model = CandidateApplication
    inlines = [CandidateSubApplicationInline]
    list_display = [
        'profile',
        'participation_title',
        'score',
        'application_stage'
    ]
    list_filter = [
        'created_at',
    ]

class CandidatePillarSubApplicationAdmin(admin.ModelAdmin):
    model = CandidatePillarSubApplication
    list_display = [
        # 'sub_application'
        'pillar',
        'score_per_pillar',
    ]
    list_filter = [
        'created_at',
    ]



admin.site.register(CandidateProfile, CandidateProfileAdmin)
admin.site.register(CandidateApplication, CandidateApplicationAdmin)
admin.site.register(CandidateSubApplication, CandidateSubApplicationAdmin)
admin.site.register(CandidatePillarSubApplication, CandidatePillarSubApplicationAdmin)


