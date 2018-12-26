from django.contrib import auth
from django.contrib.auth import views as auth_views
from django.shortcuts import render, redirect
from django.utils.http import urlencode

from RubikVNdotOrg.settings import server_configs
from .forms import UserCreationForm


def login(request):
    # Let user choose whether to login with WCA account
    # or with email + password
    if request.user.is_authenticated:
        return redirect("homepage")
    else:
        return render(request, "registration/login_method.html")

def login_oauth(request):
    # Perform OAuth login
    if request.user.is_authenticated:
        return redirect("homepage")
    else:
        payload = {
            "client_id" : server_configs.oauth_client_id,
            "redirect_uri" : server_configs.oauth_callback_uri,
            "scope" : server_configs.oauth_default_scope,
            "response_type" : "code",
        }
        url_authorize = server_configs.oauth_base_url_authorize + urlencode(payload)
        return redirect(url_authorize)

def login_oauth_callback(request):
    code = request.GET.get("code")
    if code is None:
        return redirect("homepage")
    else:
        user = auth.authenticate(request, code=code)

        if user:
            auth.login(request, user)

        return redirect("homepage")

# TODO: Views for registering and updating profile, with an option to
# connect with WCA account.
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login_pw")

    form = UserCreationForm()
    ctx = {"form": form}
    return render(request, "registration/register.html", ctx)
