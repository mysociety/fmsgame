from django.conf.urls.defaults   import patterns, url, include
from django.views.generic.simple import direct_to_template

# import djangoproj.settings


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


    (r'^$', direct_to_template, { 'template': 'login.html', } ),

    # openid login/registration
    (r'^openid/',              include( 'django_openid_auth.urls' )),    
)
