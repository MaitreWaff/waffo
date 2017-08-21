from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
# admin.autodiscover()
from blog import views

#import django.views.defaults

# handler404 = 'path.to.views.custom404'

app_name = 'blog'

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'waffo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.archive, name='archive'),
    # url(r'^(?P<slug>[-\w]+)/$', views.BlogPostDetailView.as_view(), name='blogpost-detail'),
    # url(r'^list/$', views.BlogPostDetailView.as_view(), name='blogpost-list'),
    url(r'^create/$', views.CreateBlog.as_view(), name='create-blog'),
    url(r'^post/blog/bloglist/$', views.BlogListView.as_view(), name='blog-list'),
    url(r'^post/blog/details/(?P<slug>[-\w]+)/$', views.BlogDetailView.as_view(), name='blog-detail'),
    # url(r'^post/blog/details/(?P<pk>\d+)/create/post/$', views.CreatePost.as_view(), name='blog-detail'),
    url(r'^post/create/(?P<blog_id>\d+)/$', views.CreatePost.as_view(), name='create-post'),
    url(r'^post/create/comment/(?P<postid>\d+)/$', views.CreateComment.as_view(), name='create-post-comment'),
    url(r'^post/details/(?P<slug>[-\w]+)/$', views.BlogPostDetailView.as_view(), name='blogpost-details'),
    url(r'^post/list/$', views.BlogPostListView.as_view(), name='blogpost-list'),
    url(r'^list/$', views.BlogListView.as_view(), name='blog-list'),
    url(r'^actualite/$', views.home, name='actu'),
    url(r'^blogslist/$', views.blogs, name='blogs'),
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
