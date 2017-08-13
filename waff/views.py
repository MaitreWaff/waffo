from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import RequestContext

from django.contrib.auth.decorators import login_required

from django.views import generic

# CONSTANTES

# Create your views here.
def index(request):
    """
    Page d'Acceuil.
    :param request:
    :return:
    """
    context = RequestContext(request)
    context_dict = {}

    return render_to_response('waffo/index.html', context_dict, context)

@login_required(login_url='/waffo/login/')
def home(request):
    """
    Page Dashboard.
    :param request:
    :return:
    """
    context = RequestContext(request)
    context_dict = {}

    return render_to_response('waffo/home.html', context_dict, context)
