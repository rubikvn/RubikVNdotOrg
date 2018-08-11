from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse

from .models import *
from django.db.models import Min

# TODO: create views
def rank(request):
    #return HttpResponse("You are at the ranking index page.")
    return render(request, "ranking/rank.html")
def index(request):
    return render(request, "ranking/index.html")
# def person(request, wca_id):
#     try:
#         person = Vietnamese.objects.get(pk = wca_id)
#     except Vietnamese.DoesNotExist:
#         raise Http404("Person does not exist")
#     context = {
#         "person": person,
#     }
#     return render(request, "ranking/person.html", context)
#
# def rank(request):
#     try:
#         event_id = '333'
#         results = Viresults.objects.filter(
#                 eventid = event_id,
#                 best__gt = 0
#             ).values(
#                 'personid', 'competitionid'
#             ).annotate(
#                 Min('best')
#             ).order_by(
#                 'best__min',
#             )
#         res = Viresults.objects.all()
#         print(results.query)
#     except Viresults.DoesNotExist:
#         raise Http404("Error occurred.")
#     context = {
#         "event_name": event_id,
#         # "results": result_list,
#         "results": results
#     }
#     return render(request, "ranking/rank.html", context)
