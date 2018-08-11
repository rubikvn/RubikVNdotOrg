from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse

from .models import *

# TODO: create views
def rank(request):
    return render(request, "ranking/rank.html")
    
    
def index(request):
    return render(request, "ranking/index.html")
