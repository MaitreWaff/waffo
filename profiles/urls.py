from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
# admin.autodiscover()
from profile import views

#import django.views.defaults

# handler404 = 'path.to.views.custom404'

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'waffo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^$', views.archive, name='archive'),
    url(r'^profile/$', views.blogs, name='profile'),
    # url(r'^home/$', views.home, name='home'),

    # url(r'^login/$', auth_views.login, {'template_name': 'registration/login.html', 'authentication_form': LoginForm}, name='login'),
    # url(r'^logout/$', auth_views.logout, {'template_name': 'registration/logged_out.html'}, name='logout'),

    # url(r'^about/$', views.about, name='about'),
)
#from django.views.generic import *
from waff.form import LoginForm

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
