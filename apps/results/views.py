from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse
from django.core.paginator import Paginator

from .models import *
from lib.utils_wca import Formatter
# from datetime import datetime

def ranking(request):
    # start = datetime.now()
    eventid = request.GET.get("eventid", "333")
    limit = request.GET.get("limit", "100")
    category = request.GET.get("category", "single")
    results = []

    if category == "single":
        results = RankSingle.get_rank_single(eventid, limit)
    elif category == "average":
        results = RankAverage.get_rank_average(eventid, limit)

    paginator = Paginator(results, 25)
    page = request.GET.get('page')
    results = paginator.get_page(page)
    f = Formatter()
    results = f.format_wca_result(results, "best", eventid, category)

    context = {
        "event_name": eventid,
        "limit": limit,
        "category": category,
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
