from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from waff import views

#import django.views.defaults

# handler404 = 'path.to.views.custom404'

#from django.views.generic import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'waffo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^$', views.index, name='index'),
    # url(r'^about/$', views.about, name='about'),
)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
