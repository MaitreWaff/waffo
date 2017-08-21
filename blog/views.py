from django.views import generic
from django.utils import timezone

from django.shortcuts import render, render_to_response

from django.template import RequestContext

from django.template import loader, Context
from django.http import HttpResponse

from blog.models import *
#Blog, BlogPost, BlogSection, SectionSection

# Create your views here.

def archive(request):
    posts = BlogPost.objects.all()
    # t = loader.get_template("blog/archive.html")
    # c = Context({ 'posts': posts })
    # return HttpResponse(t.render(c))

    context = RequestContext(request)
    context_dict = {'posts': posts}

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
    template_name = 'blog/blog-detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super(BlogPostDetailView, self).get_context_data(**kwargs)
        context['now'] = timezone.now() #
        return context

class BlogPostListView(generic.list.ListView):
    model = BlogPost
    template_name = 'blog/blog-list.html'
    # template_name = 'blog/index.html'
    context_object_name = 'all_blog_posts'

    def get_context_data(self, **kwargs):
        context = super(BlogPostListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now() #
        return context

class BlogDetailView(generic.DetailView):
    model = Blog
    template_name = 'blog/blog-detail.html'
    # context_object_name = 'blog'

    def get_queryset(self):
        return Blog.objects.get_or_create(slug=self.kwargs['slug'])
    #
    # def get_context_data(self, **kwargs):
    #     context = super(BlogDetailView, self).get_context_data(**kwargs)
    #     context['blogid'] =
    #     return context


class BlogListView(generic.ListView):
    model = Blog
    template_name = 'blog/blog-list.html'
    context_object_name = 'all_blog'

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















