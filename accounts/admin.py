# admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from core.utility import linkify
from .models import *

class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('password', 'username')}),
        (('Personal info'), {
         'fields': ('name', )}),
        (('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'is_blocked',
                                      'groups', 'user_permissions')}),
        (('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide', ),
            'fields': ('username', 'password1', 'password2'),
        }),
    )
    list_display = ['username', 'name', 'is_staff']
    search_fields = ('username', 'name')
    ordering = ('email', )




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