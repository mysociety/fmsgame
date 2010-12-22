from django.conf.urls.defaults   import patterns, url, include
from django.views.generic.simple import direct_to_template
import django.views.static
import settings
import views


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^fmsgame/', include('fmsgame.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),


    (r'^$',          direct_to_template, { 'template': 'login.html', } ),
    (r'^geolocate$', direct_to_template, { 'template': 'geolocate.html', } ),
    (r'^issue/(P?<issue_id>\d*)/$', views.issue ),

    # openid login/registration
    (r'^openid/',              include( 'django_openid_auth.urls' )),    
)

if settings.SERVE_STATIC_FILES:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 
         django.views.static.serve, 
         {'document_root':settings.MEDIA_ROOT}),
    )
