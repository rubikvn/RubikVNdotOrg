import requests

from RubikVNdotOrg.settings import server_configs
from apps.events.models import User

from apps.results.models import Country


class OAuthBackend():

    def authenticate(self, request, code):
        # TODO: Check for referrer and confirm it's WCA
        token_info, user_info = self._oauth_authorize(request, code)

        try:
            email = user_info["me"]["email"]
            user = User.objects.get(email=email)

            if request.user.is_authenticated:
                raise KeyError("That WCA account has been claimed by another person")

        except User.DoesNotExist:
            if request.user.is_authenticated:
                user = request.user
            else:
                user = User()

        user.fill_personal_info_from_api_dict(user_info)
        user.fill_login_info_from_api_dict(token_info)

        user.save()

        return user

    def get_user(self, email):
        try:

            return User.objects.get(pk=email)
        except User.DoesNotExist:
            return None

    def _oauth_authorize(self, request, code):
        callback = ""

        if request.user.is_authenticated:
            callback = "connect"
        else:
            callback = "login"
        payload = {
            "grant_type" : "authorization_code",
            "client_id" : server_configs.oauth_client_id,
            "client_secret" : server_configs.oauth_client_secret,
            "redirect_uri" : server_configs.oauth_callback_uri[callback],
            "code" : code,
        }

        r = requests.post(server_configs.oauth_base_url_fetch_token, json=payload)
        token_info = r.json()
        access_token = token_info["access_token"]

        headers = {
            "Authorization" : "Bearer {}".format(access_token)
        }

        url_api = server_configs.oauth_base_url_api + "me"
        r = requests.get(url_api, headers=headers)

        user_info = r.json()

        return (token_info, user_info)
