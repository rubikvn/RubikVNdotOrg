from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponseNotAllowed, JsonResponse

from RubikVNdotOrg.settings import server_configs
from ..models import *


def browse_events(request):
    """
    Browse events view.

    :param request:
    :return:
    """
    if request.method != "GET":
        return HttpResponseNotAllowed(request)
    else:
        return render(request, "events/events.html")


def event_details(request):
    """
    View details about an event.

    :param request:
    :return:
    """
    if request.method != "GET":
        return HttpResponseNotAllowed(request)
    else:
        return render(request, "events/event_details.html")


@login_required()
def event_register(request):
    """
    Register for an event.

    :param request:
    :return:
    """
    if request.method == "POST":
        # TODO: process form
        pass
    elif request.method == "GET":
        return render(request, "events/event_register.html")
    else:
        return HttpResponseNotAllowed(request)


@login_required()
def event_create(request):
    """
    Create an event.

    :param request:
    :return:
    """
    if request.method == "POST":
        # TODO: process form
        pass
    elif request.method == "GET":
        return render(request, "events/event_create.html")
    else:
        return HttpResponseNotAllowed(request)


@login_required()
def event_manage(request):
    """
    Manage an event.

    :param request:
    :return:
    """
    if request.method == "POST":
        # TODO: process form
        pass
    elif request.method == "GET":
        return render(request, "events/event_manage.html")
    else:
        return HttpResponseNotAllowed(request)


def api_browse_events(request):
    """
    Json endpoint for browsing events.

    :param request:
    :return:
    """
    if request.method != "GET":
        return HttpResponseNotAllowed(request)
    else:
        context = {}

        return JsonResponse(context)
