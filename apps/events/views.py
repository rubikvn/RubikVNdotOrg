from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.utils.http import urlencode

from RubikVNdotOrg.settings import server_configs


def oauth_login(request):
    if request.user.is_authenticated:
        return redirect("/")
    else:
        payload = {
            "client_id" : server_configs.oauth_client_id,
            "redirect_uri" : server_configs.oauth_callback_uri,
            "scope" : server_configs.oauth_default_scope,
            "response_type" : "code",
        }
        url_authorize = server_configs.oauth_base_url_authorize + urlencode(payload)
        return redirect(url_authorize)

def oauth_handler(request):
    code = request.GET.get("code")
    if code is None:
        return redirect("/")
    else:
        user = authenticate(request, code=code)

        if user:
            login(request, user)

        return redirect("/")

def oauth_logout(request):
    if not request.user.is_authenticated:
        pass
    else:
        logout(request)
    return redirect("/")
