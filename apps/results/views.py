from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse
from django.core.paginator import Paginator

from .models import *
from lib.utils_wca import ResultFormatter
# from datetime import datetime

def ranking(request):
    # start = datetime.now()
    eventid = request.GET.get("eventid", "333")
    limit = request.GET.get("limit", "100")
    category = request.GET.get("category", "single")
    pattern = request.GET.get("q", "")
    page = request.GET.get('page')
    event_name = Event.get_event_name(eventid)
    results = []

    if category == "single":
        results = RankSingle.get_rank_single(eventid, limit, pattern)
    elif category == "average":
        results = RankAverage.get_rank_average(eventid, limit, pattern)

    paginator = Paginator(results, 25)
    results = paginator.get_page(page)

    f = ResultFormatter(results.object_list, "best", eventid, category)
    results.object_list = f.format()

    context = {
        "event_name": event_name,
        "eventid":eventid,
        "limit": limit,
        "category": category,
        "pattern": pattern,
        "results": results,

    }
    # r = render(request, "results/ranking.html", context)
    # end = datetime.now()
    # diff = (end-start).total_seconds()
    # print(f"Took {diff} seconds")
    # return r
    return render(request, "results/ranking.html", context)


def index(request):
    return render(request, "results/index.html")
