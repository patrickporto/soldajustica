"""
Definition of urls for soldajustica.
"""
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

from django.conf.urls import include
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('app.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
