from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^polls/', include('poll.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^index.html', 'poll.views.home'),
)