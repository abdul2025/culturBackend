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
        'score'

    ]
    list_filter = [
        'user',
        'created_at',
    ]

admin.site.register(CandidateProfile, CandidateProfileAdmin)
