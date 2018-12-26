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
from django.views.generic import TemplateView, RedirectView
from django.contrib.auth import views as auth_views

from apps.events import views as ev

urlpatterns = [
    path("", RedirectView.as_view(url="home")),
    path("home", TemplateView.as_view(template_name="index.html"), name="homepage"),
    path("admin/", admin.site.urls),
    path("login/", ev.login, name="login"),
    path("login/oauth/", ev.login_oauth, name="login_oauth"),
    path("login/oauth/callback", ev.login_oauth_callback, name="login_oauth_callback"),
    path("login/pw/",
        auth_views.LoginView.as_view(
            template_name="registration/login.html",
            redirect_field_name="homepage",
            redirect_authenticated_user=True
        ),
        name="login_pw"
    ),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("results/", include("apps.results.urls")),
    path("events/", include("apps.events.urls")),
]
