import requests

from RubikVNdotOrg.settings import server_configs
from apps.events.models import Cuber
from apps.results.models.wca.country import Country

# print(server_configs.oauth_client_id)
class OAuthBackend():

    def authenticate(self, request, code):
        token_info, user_info = self._oauth_authorize(request, code)

        try:
            user_wca_id = user_info["me"]["wca_id"]
            user = Cuber.objects.get(wca_id=user_wca_id)

        except Cuber.DoesNotExist:
            user = Cuber()

            user.fill_personal_info_from_api_dict(user_info)
            user.fill_login_info_from_api_dict(token_info)

            user.save()

        return user

    def get_user(self, wca_id):
        try:
            return Cuber.objects.get(pk=wca_id)
        except Cuber.DoesNotExist:
            return None

    def _oauth_authorize(self, request, code):
        payload = {
            "grant_type" : "authorization_code",
            "client_id" : server_configs.oauth_client_id,
            "client_secret" : server_configs.oauth_client_secret,
            "redirect_uri" : server_configs.oauth_callback_uri,
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
