from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pim.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', 'auth.views.logged_in'),
    url(r'^logout/$', 'auth.views.logout'),
    url(r'^done/$', 'auth.views.done', name='done'),
    url(r'', include('social.apps.django_app.urls', namespace='social'))


)
