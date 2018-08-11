from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse

from .models import *

# TODO: create views
def index(request):
    return HttpResponse("You are at the ranking index page.")
