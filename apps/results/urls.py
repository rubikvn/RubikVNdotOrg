from django.urls import path
from django.views.generic.base import RedirectView

from . import views

app_name = "results"
urlpatterns = [
    path("", RedirectView.as_view(pattern_name="results:ranking"), name="index"),
    path("ranking/", views.ranking, name="ranking"),
    path("api/ranking", views.api_ranking, name="api_ranking"),
]
