from django.conf.urls import patterns, include, url
from ccdjango.views import hello, current_datetime, hours_ahead, display_meta
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^hello/$', hello),
    (r'^time/$', current_datetime),
    (r'^time/plus/(\d{1,2})$', hours_ahead),
    (r'^display/$', display_meta),
    # Examples:
    # url(r'^$', 'ccdjango.views.home', name='home'),
    # url(r'^ccdjango/', include('ccdjango.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
)
