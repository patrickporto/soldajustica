"""
Definition of urls for soldajustica.
"""
from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'app.views.home', name='home'),
    url(r'^contact$', 'app.views.contact', name='contact'),
    url(r'^about', 'app.views.about', name='about'),
    url(r'^projects', 'app.views.projects', name='projects'),
    url(r'^get-involved', 'app.views.get_involved', name='get-involved'),
    url(r'^donate', 'app.views.donate', name='donate'),
)
