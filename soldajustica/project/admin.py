from django.contrib import admin
from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('date_created', 'last_update',)
    list_display = ('name', 'active',)
    list_editable = ('active',)