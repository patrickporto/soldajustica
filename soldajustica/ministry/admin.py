from django.contrib import admin
from .models import (
    Ministry,
    MinistryMember,
)


@admin.register(Ministry)
class MinistryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    filter_horizontal = ('members',)
    readonly_fields = ('date_created', 'last_update',)


@admin.register(MinistryMember)
class MinistryMemberAdmin(admin.ModelAdmin):
    pass