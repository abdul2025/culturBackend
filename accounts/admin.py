# admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from core.utility import linkify
from .models import *

class CustomUserAdmin(UserAdmin):
    list_display = (
        'email', 'phone_number', 'name', 'is_staff',
        'is_blocked'
        )

    fieldsets = (
        (None, {
            'fields': ('email', 'password')
        }),
        ('Personal info', {
            'fields': ('name', 'phone_number')
        }),
        ('Permissions', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser',
                'groups', 'user_permissions', 'is_blocked',
                )
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        })
    )

    add_fieldsets = (
        (None, {
            'fields': ('email', 'password1', 'password2')
        }),
        ('Personal info', {
            'fields': ('name',)
        }),
        ('Permissions', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser',
                'groups', 'user_permissions', 'is_blocked'
                )
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        }),
    )




class JudgersAdmin(admin.ModelAdmin):
    model = Judgers
    list_display = [
        'user',
        linkify(field_name='tracks'),
    ]
class FilteringAdmin(admin.ModelAdmin):
    model = Filtering
    list_display = [
        'user',
        linkify(field_name='tracks'),
    ]

class SorterAdmin(admin.ModelAdmin):
    model = Sorter
    list_display = [
        'user',
        linkify(field_name='tracks'),
    ]


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Judgers, JudgersAdmin)
admin.site.register(Filtering, FilteringAdmin)
admin.site.register(Sorter, SorterAdmin)