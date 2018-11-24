from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser

from apps.results.models.wca.country import Country

# Create your models here.
class CuberManager(models.Manager):
    def get_by_natural_key(self, wca_id):
        return self.get(wca_id=wca_id)

class Cuber(AbstractBaseUser):
    wca_id = models.CharField(primary_key=True, max_length=10)
    name = models.CharField(max_length=80, blank=True)
    email = models.EmailField(default='')
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, blank=True, null=True)
    country = models.ForeignKey(Country, models.DO_NOTHING, default='')
    manage_competitions = models.BooleanField(default=False)

    # TODO: store access tokens for wca api, and expiry dates as well
    access_token = models.CharField(max_length=80)
    refresh_token = models.CharField(max_length=80)
    token_type = models.CharField(max_length=20)
    token_scope = models.CharField(max_length=50)
    token_created_at = models.IntegerField()
    token_expiry = models.IntegerField()

    USERNAME_FIELD = 'wca_id'
    EMAIL_FIELD = 'email'

    objects = CuberManager()

    def fill_personal_info_from_api_dict(self, api_dict):
        self.wca_id = api_dict["me"]["wca_id"]
        self.name = api_dict["me"]["name"]
        self.gender = api_dict["me"]["gender"]
        self.country = Country.get_country_from_iso2(api_dict["me"]["country_iso2"])
        self.email = api_dict["me"]["email"]
        self.date_of_birth = api_dict["me"]["dob"]

    def fill_login_info_from_api_dict(self, api_dict):
        self.access_token = api_dict["access_token"]
        self.refresh_token = api_dict["refresh_token"]
        self.token_type = api_dict["token_type"]
        self.token_scope = api_dict["scope"]
        self.token_created_at = api_dict["created_at"]
        self.token_expiry = api_dict["expires_in"]

    def can_manage_comps(self):
        return self.manage_competitions

    def __str__(self):
        return f"Name: {self.name}, WCA ID: {self.wca_id}"
