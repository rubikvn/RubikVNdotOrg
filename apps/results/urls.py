from django.urls import path

from . import views

# Create url scheme
urlpatterns = [
    path("", views.index, name="index"),
    path("ranking/", views.ranking, name="ranking"),

    # path("ranks/", views.rank, name="rank"),
    # path("<slug:wca_id>/", views.person, name="person"),
]
