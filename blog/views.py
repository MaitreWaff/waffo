from django.contrib.auth.decorators import login_required
from django.views import generic
from django.utils import timezone

from django.shortcuts import render, render_to_response, get_object_or_404
from django.core import serializers

from django.template import RequestContext

from django.template import loader, Context
from django.http import HttpResponse, HttpResponseRedirect

from blog.models import *
from blog.form import *
#Blog, BlogPost, BlogSection, SectionSection

# Create your views here.



# @login_required
class Desktop(generic.edit.CreateView):
    model = BlogPost
    # queryset = BlogPost.objects.filter(blogs.auteur=self.request.user)

    fields = ['titre', 'text', 'blog']
    success_url = '/blog/feed-news/'
    # template_name = 'base.html'
    template_name = 'blog/feednews.html'
    #
    # def get_context_data(self, **kwargs):
    #     context = super(FeedNews, self).get_context_data(**kwargs)
    #     context['posts'] = BlogPost.objects.all()
    #     context['blogs'] = Blog.objects.all()
    #     context['blog_form'] = BlogForm()
    #     return context
    #
    # def get_user_blogs(self):
    #     return Blog.objects.filter(auteur=self.request.user)
    #     # return get_object_or_404(Blog, auteur=self.request.user)
    #
    # def get_form(self, form_class):
    #     # form = super(generic.CreateView, self).get_form(form_class)
    #     form = super(generic.edit.CreateView, self).get_form(form_class)
    #     # form = super(FeedNews, self).get_form(form_class)
    #     form.fields['blog'].queryset = self.get_user_blogs()
    #     return form
    #
    # def get_initial(self):
    #     initial_dict = {'posts': BlogPost.objects.all()}
    #     # initial_dict = {'blog': self.request.session.get('blogs')}
    #     return initial_dict

    def form_valid(self, form):
        # Ajouter les liens entre le post et un blog.
        return super(Desktop, self).form_valid(form)













@login_required
def desktop(request):
    context_dict = dict()
    blogs = Blog.objects.all()
    posts = BlogPost.objects.all()
    context_dict['blogs'] = blogs
    context_dict['posts'] = posts
    if request.method == 'POST':
        context_dict['blog_form'] = DesktopBlogForm(request.POST)
        context_dict['post_form'] = DesktopPostForm(request.user.userprofilemodel, request.POST)


    else:
        context_dict['blog_form'] = DesktopBlogForm()
        context_dict['post_form'] = DesktopPostForm(request.user.userprofilemodel)


    return render(request, 'blog/desktop.html', context_dict)
    # return render(request, 'desktop.html', context_dict)











def archive(request):
    posts = BlogPost.objects.all()
    post_form = PostForm(request)
    # t = loader.get_template("blog/archive.html")
    # c = Context({ 'posts': posts })
    # return HttpResponse(t.render(c))

    context = RequestContext(request)
    context_dict = {'posts': posts, 'postform': post_form}

    return render_to_response('blog/blog-home.html', context_dict, context)

def blogs(request):
    bloglist = Blog.objects.all()

    context = RequestContext(request)
    context_dict = {'blogslist': bloglist}

    return render_to_response('blog/blogslist.html', context_dict, context)


def home(request):
    blogpostslist = BlogPost.objects.all()

    context = RequestContext(request)
    context_dict = {'posts': blogpostslist}

    return render_to_response('blog/blog-home.html', context_dict, context)


# Vues generiques d'Affichage.
class BlogPostDetailView(generic.detail.DetailView):

    model = BlogPost
    template_name = 'blog/post-detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super(BlogPostDetailView, self).get_context_data(**kwargs)
        # context['now'] = timezone.now() #
        return context

class BlogPostListView(generic.list.ListView):
    model = BlogPost
    template_name = 'blog/post-list.html'
    # template_name = 'blog/index.html'
    context_object_name = 'all_blog_posts'

    def get_context_data(self, **kwargs):
        context = super(BlogPostListView, self).get_context_data(**kwargs)
        # context['now'] = timezone.now() #
        context['form'] = DesktopPostForm #() #User.objects.first())
        return context

class BlogDetailView(generic.DetailView):
    model = Blog
    template_name = 'blog/blog-detail.html'
    context_object_name = 'blog'

    # def get_queryset(self):
    #     return Blog.objects.get_or_create(slug=self.kwargs['slug'])
    #
    # def get_context_data(self, **kwargs):
    #     context = super(BlogDetailView, self).get_context_data(**kwargs)
    #     context['blogid'] =
    #     return context


class BlogListView(generic.ListView):
    model = Blog
    template_name = 'blog/blog-list.html'
    context_object_name = 'all_blogs'

    def get_queryset(self):
        return Blog.objects.all()





# Fonction accessoires.

def getUserBlog(blog_id):
    # return Blog.objects.get_or_create(auteur=request.user.profile)[0]
    # return Blog.objects.get_or_create(auteur=profile)[0]
    return Blog.objects.get_or_create(blog=blog_id)[0]

def getPost(blogid):
    return BlogPost.objects.get(pk=blogid)





# Create vues

class CreateBlog(generic.edit.CreateView):
    model = Blog
    fields = ['theme']

    def form_valid(self, form):
        form.instance.auteur = self.request.user.profile
        return super(CreateBlog, self).form_valid(form)


class CreatePost(generic.edit.CreateView):
    model = BlogPost
    fields = ['titre', 'text']

    def form_valid(self, form):
        form.instance.auteur = self.request.user.profile
        form.instance.blog = getUserBlog(self.kwargs['blog_id'])
        return super(CreatePost, self).form_valid(form)


class CreateComment(generic.edit.CreateView):
    model = CommentBlogPost
    fields = ['commentaire',]
    success_url = '/blog/post/list/'
    # success_url = '/blog/post/details/'

    def form_valid(self, form):
        form.instance.auteur = self.request.user.profile
        form.instance.blogpost = getPost(self.kwargs['postid'])
        return super(CreateComment, self).form_valid(form)


# @login_required
class FeedNews(generic.edit.CreateView):
    model = BlogPost
    # queryset = BlogPost.objects.filter(blogs.auteur=self.request.user)

    fields = ['titre', 'text', 'blog']
    success_url = '/blog/feed-news/'
    # template_name = 'base.html'
    template_name = 'blog/feednews.html'
    #
    # def get_context_data(self, **kwargs):
    #     context = super(FeedNews, self).get_context_data(**kwargs)
    #     context['posts'] = BlogPost.objects.all()
    #     context['blogs'] = Blog.objects.all()
    #     context['blog_form'] = BlogForm()
    #     return context
    #
    # def get_user_blogs(self):
    #     return Blog.objects.filter(auteur=self.request.user)
    #     # return get_object_or_404(Blog, auteur=self.request.user)
    #
    # def get_form(self, form_class):
    #     # form = super(generic.CreateView, self).get_form(form_class)
    #     form = super(generic.edit.CreateView, self).get_form(form_class)
    #     # form = super(FeedNews, self).get_form(form_class)
    #     form.fields['blog'].queryset = self.get_user_blogs()
    #     return form
    #
    # def get_initial(self):
    #     initial_dict = {'posts': BlogPost.objects.all()}
    #     # initial_dict = {'blog': self.request.session.get('blogs')}
    #     return initial_dict

    def form_valid(self, form):
        # Ajouter les liens entre le post et un blog.
        return super(FeedNews, self).form_valid(form)



class CreateBlog(generic.edit.CreateView):
    model = Blog
    # form_class = BlogForm
    form_class = DesktopBlogForm #() #User.objects.first()) # TODO: Get User in request.
    # fields = ['auteur', 'theme']

    # fields = ['theme']
    # success_url = '/blog/feed-news/'
    success_url = 'desktop'
    # success_url = '/blog/list/'
    template_name = 'blog/blog-list.html'


    def get_user(self):
        return UserProfileModel.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super(CreateBlog, self).get_context_data(**kwargs)
        context['all_blogs'] = Blog.objects.order_by('-date_blog')
        return context
    #
    # def get_form(self, form_class):
    #     form = super(CreateBlog, self).get_form(form_class)
    #     # form.fields['auteur'].queryset = self.get_user()
    #     return form


    def form_valid(self, form):
        # obj = form.save(commit=False)
        # obj.auteur = self.request.user.profile
        # obj.save()
        # form['auteur'] = self.request.user.profile

        # self.object = form.save(commit=False)
        # self.object.auteur = self.request.user.profile
        # self.object.save()
        form.instance.auteur = UserProfileModel.objects.get(user=self.request.user)

        return super(CreateBlog, self).form_valid(form)
        # return HttpResponseRedirect(self.get_success_url())



def feednews_update(request, id):
    response = HttpResponse()
    response['Content-Type'] = 'text/javascript'
    response.write(serializers.serialize("json", BlogPost.objects.filter(pk__gt=id), indent=2, use_natural_keys=True))
    return response





















