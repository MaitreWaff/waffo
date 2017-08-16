from django.shortcuts import render, render_to_response

from django.template import RequestContext

from django.template import loader, Context
from django.http import HttpResponse

from blog.models import Blog, BlogPost

# Create your views here.

def archive(request):
    posts = BlogPost.objects.all()
    # t = loader.get_template("blog/archive.html")
    # c = Context({ 'posts': posts })
    # return HttpResponse(t.render(c))

    context = RequestContext(request)
    context_dict = {'posts': posts}

    return render_to_response('blog/archive.html', context_dict, context)

def blogs(request):
    bloglist = Blog.objects.all()

    context = RequestContext(request)
    context_dict = {'blogslist': bloglist}

    return render_to_response('blog/blog-home-base.html', context_dict, context)


def home(request):
    blogslist = BlogPost.objects.all()

    context = RequestContext(request)
    context_dict = {'posts': blogslist}

    return render_to_response('blog/blog-home.html', context_dict, context)