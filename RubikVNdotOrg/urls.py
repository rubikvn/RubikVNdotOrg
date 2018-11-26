"""RubikVNdotOrg URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

import apps.events.views as eviews

urlpatterns = [
    path("", TemplateView.as_view(template_name="unv.html")),
    # path("admin/", admin.site.urls),
    # path("login/", eviews.oauth_login, name="login"),
    # path("login/oauth_handler", eviews.oauth_handler, name="oauth_handler"),
    # path("logout/", eviews.oauth_logout, name="logout"),
    # path("results/", include("apps.results.urls")),
    # path("events/", include("apps.events.urls")),
]
