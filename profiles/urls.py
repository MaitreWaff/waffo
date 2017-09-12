from django.conf.urls import include, url #, patterns
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
# admin.autodiscover()
from profiles import views

#import django.views.defaults

# handler404 = 'path.to.views.custom404'

# urlpatterns = patterns('',
urlpatterns = [
    # Examples:
    # url(r'^$', 'waffo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^$', views.archive, name='archive'),
    url(r'^update/$', views.update_profile, name='profile'),
    url(r'^user/$', views.profile, name='userprofile'),
    # url(r'^(?P<pk>\d+)/$', views.viewuserprofile, name='viewuserprofile'),
    url(r'^(?P<slug>[-\w]+)/$', views.viewuserprofile, name='viewuserprofile'),
    # url(r'^accounts/', include('registration.backends.simple.urls')),
    # url(r'^home/$', views.home, name='home'),

    # url(r'^login/$', auth_views.login, {'template_name': 'registration/login.html', 'authentication_form': LoginForm}, name='login'),
    # url(r'^logout/$', auth_views.logout, {'template_name': 'registration/logged_out.html'}, name='logout'),

    # url(r'^about/$', views.about, name='about'),
# )
]
#from django.views.generic import *
from waff.form import LoginForm

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
