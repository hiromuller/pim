from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', 'auth.views.logged_in'),
    url(r'^logout/$', 'auth.views.logout'),
    url(r'^done/$', 'auth.views.done', name='done'),
    url(r'', include('social.apps.django_app.urls', namespace='social')),
    url(r'^main/$', 'common.views.show', name='show'),
    url(r'^', include('django.contrib.staticfiles.urls')),
)

urlpatterns += staticfiles_urlpatterns()