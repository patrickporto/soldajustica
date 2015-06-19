from django.contrib import admin
from .models import (
    Gallery,
    GalleryImage,
)


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    filter_horizontal = ('images',)
    readonly_fields = ('date_created', 'last_update',)


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    pass