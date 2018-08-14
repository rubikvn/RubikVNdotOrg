from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse

from .models import *

def ranking(request):
    eventid = request.GET.get("eventid", "333")
    limit = request.GET.get("limit", "100")
    category = request.GET.get("category", "single")
    results = []
    if category == "single":
        results = RankSingle.get_rank_single(eventid, limit)
    elif category == "average":
        results = RankAverage.get_rank_average(eventid, limit)
    for result in results:
        seconds = result.best / 100
        if seconds >= 60:
            result.best = f"{int(seconds/60):02d}:{seconds%60:05.2f}"
        else:
            result.best = f"{seconds:.2f}"
    context = {
        "event_name": eventid,
        "results": results
    }
    return render(request, "results/ranking.html", context)


def index(request):
    return render(request, "results/index.html")
