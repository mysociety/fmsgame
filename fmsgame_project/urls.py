from django.conf.urls.defaults   import patterns, url, include
from django.views.generic.simple import direct_to_template
import django.views.static
import settings
import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', direct_to_template, {'template': 'login.html'}),
    url(r'^geolocate$', direct_to_template, {'template': 'geolocate.html'}, name='geolocate'),

    (r'^find_issues', views.find_issues),
    (r'^issue/(?P<issue_id>[\d]+)/$', views.issue),
    url(r'^success', views.success, name='success'),
    
    # openid login/registration
    (r'^openid/', include('django_openid_auth.urls')),
    url(r'^scoreboard', views.scoreboard, name='scoreboard'),
                       )

if settings.SERVE_STATIC_FILES:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 
         django.views.static.serve, 
         {'document_root':settings.MEDIA_ROOT}),
    )
