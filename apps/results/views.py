from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.urls import reverse

from .models import *
from RubikVNdotOrg.lib.formatter import ResultFormatter
from RubikVNdotOrg.lib.paginator import Paginator


def ranking(request):
    if request.method != "GET":
        # should return an error code if the method is not GET
        return redirect("homepage")
    else:
        return render(request, "results/ranking.html")


def api_ranking(request):
    """
    The original implementation of the ranking page involves refreshing the page
    every time the user changes a ranking criteria, which can be quite annoying
    especially if reloading takes a lot of time. This method seeks to resolve
    that issue and improve user experience.

    This method acts as an endpoint that returns JSON of ranking results,
    based on the GET requests, so that Ajax calls can easily be performed
    from the client browser.
    """
    context = {}

    if request.method != "GET":
        context["error"] = "Http method not supported!"
    else:
        eventid = request.GET.get("eventid", "333").lower()
        category = request.GET.get("category", "single").lower()
        query = request.GET.get("query", "").lower()
        page = request.GET.get('page', '1').lower()
        limit = request.GET.get("limit", "50").lower()
        event_name = Event.get_event_name(eventid)
        results = []

        if category == "single":
            results = RankSingle.get_rank_single(eventid, query)
        elif category == "average":
            results = RankAverage.get_rank_average(eventid, query)

        p = Paginator(results, limit)
        results = p.get_page(page)

        f = ResultFormatter(results, "best", eventid, category)
        results = list(f.format())

        context = {
            "success" : True,
            "event_name": event_name,
            "eventid": eventid,
            "limit": limit,
            "category": category,
            "query": query,
            "results": results,
            "last_page": p.get_last_page(),
        }

    return JsonResponse(context)
