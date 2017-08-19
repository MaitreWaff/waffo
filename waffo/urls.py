from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from django.conf.urls import *

from django.contrib.auth import views as auth_views
# from profiles import views as profile_views
from profiles import views as profile_views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'waffo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # registration.backends.default.urls
    url(r'^account/login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^account/logout/$', 'django.contrib.auth.views.logout', name='logout'),
    url(r'^account/register/$', profile_views.signup, name='register'),
    # url(r'^signup/', profile_views.signup, name='signup'),
    # url(r'^account/', include('registration.backends.simple.urls')),
    # url(r'^accounts/', auth_views.LoginView.as_views()), # include('registration.backends.simple.urls')), # registration.backends.default.urls
    # url(r'^pages/', include('django.contrib.flatpages.urls')),
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls), name='admin'),
    url(r'^$', 'django.contrib.auth.views.login'),
    url(r'^home/$', profile_views.userhome),

    url(r'^register/success/$', profile_views.userregister_success),

    url(r'^blog/', include('blog.urls')),
    # url(r'^account/login/$', LoginView.as_view(), name='login'),
    # url(r'^account/login/$', 'django.contrib.auth.views.login', name='login'),
    # url(r'^logout/$', userlogout, name='logout'),
    # url(r'^login/$', profile_views.login, name='login'),
    # url(r'^logout/$', profile_views.logout, name='logout'),
    # url(r'^', include('django.contrib.auth.urls')),
    # url(r'^login/$', auth_views.login, {'template_name': 'registration/login.html'}, name='auth_login'),
    # url(r'^logout/$', auth_views.logout, {'next_page': '/login/'}, name='auth_logout'),
    # url(r'^profile/', include('profiles.urls')),
    # url(r'^signup/', profile_views.signup, name='signup'),
    # url(r'^waffo/', include('waff.urls')),
    # url(r'', include('django.contrib.auth.urls')),
)

