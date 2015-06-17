from django.contrib import admin
from .models import Slide


@admin.register(Slide)
class SlideAdmin(admin.ModelAdmin):
    list_display = ('title', 'active',)
    list_editable = ('active',)