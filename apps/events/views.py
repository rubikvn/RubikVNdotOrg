from django.contrib import auth
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils.http import urlencode

from RubikVNdotOrg.settings import server_configs
from .forms import UserCreationForm, UserUpdateForm


def login(request):
    """
    Let user choose whether to login with WCA account
    or with an email + password combo
    """
    if request.user.is_authenticated:
        return redirect("homepage")
    else:
        return render(request, "registration/login_method.html")

def login_oauth(request):
    """
    Perform OAuth login
    """
    if request.user.is_authenticated:
        return redirect("homepage")
    else:
        payload = {
            "client_id" : server_configs.oauth_client_id,
            "redirect_uri" : server_configs.oauth_callback_uri["login"],
            "scope" : server_configs.oauth_default_scope,
            "response_type" : "code",
        }
        url_authorize = server_configs.oauth_base_url_authorize + urlencode(payload)
        return redirect(url_authorize)

def login_oauth_callback(request):
    """
    OAuth handler for logging in user
    """
    code = request.GET.get("code")
    if code is None:
        return redirect("homepage")
    else:
        user = auth.authenticate(request, code=code)

        if user:
            auth.login(request, user)

        return redirect("homepage")

def register(request):
    """
    Allow a user to sign up to our website with their email, name and password
    """
    # TODO: Email verification
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login_password")

    form = UserCreationForm()
    ctx = {"form": form}
    return render(request, "registration/register.html", ctx)

# TODO: add button to synchronize information with WCA account
@login_required
def profile(request):
    """
    Let a user view and edit their personal information.
    This page also provides an option to connect user to their WCA account
    """
    if request.method == "POST":
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("homepage")

    form = UserUpdateForm(instance=request.user)
    ctx = {
        "form": form,
    }
    return render(request, "registration/profile.html", ctx)

@login_required
def profile_connect(request):
    """
    Connect a profile with WCA account
    """
    if request.user.wca_id is not None:
        return redirect("homepage")
    payload = {
        "client_id" : server_configs.oauth_client_id,
        "redirect_uri" : server_configs.oauth_callback_uri["connect"],
        "scope" : server_configs.oauth_default_scope,
        "response_type" : "code",
    }
    url_authorize = server_configs.oauth_base_url_authorize + urlencode(payload)
    return redirect(url_authorize)

@login_required
def profile_connect_callback(request):
    """
    OAuth handler for connecting a profile with WCA account
    """
    code = request.GET.get("code")
    if code is None or request.user.wca_id is not None:
        return redirect("homepage")
    else:
        try:
            user = auth.authenticate(request, code=code)
        except KeyError:
            return redirect("profile")
        if user:
            pass

        return redirect("profile")
