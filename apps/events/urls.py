from django.urls import path, include
from django.contrib import admin

from .views import scheduler

app_name = "events"
urlpatterns = [
    path("", scheduler.browse_events, name="index"),
    path("", scheduler.browse_events, name="browse"),
    path("create/", scheduler.event_create, name="create"),
    path("<slug:event_id>/", scheduler.event_details, name="details"),
    path("<slug:event_id>/register", scheduler.event_register, name="register"),
    path("<slug:event_id>/manage", scheduler.event_manage, name="manage"),
    path("api/browse", scheduler.api_browse_events, name="api_browse"),
]
