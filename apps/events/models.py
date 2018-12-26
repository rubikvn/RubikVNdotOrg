from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from apps.results.models import Country
from apps.results.models import Event
from django.utils import timezone

# Create your models here.
class CuberManager(models.Manager):
    def get_by_natural_key(self, wca_id):
        return self.get(wca_id=wca_id)

class User(AbstractBaseUser):
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


class CubingEvent(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    delegates = models.ManyToManyField(User, related_name='delagated_events')
    non_wca_organizers = models.CharField(max_length=200, blank=True)
    wca_organizers = models.ManyToManyField(User)
    registered = models.ManyToManyField(User, through='CompletedRegistration', related_name='registered_events')
    waitlisted = models.ManyToManyField(User, through='PendingRegistration', related_name='waitlisted_events')
    city_name = models.CharField(max_length=100)
    # info_url = models.
    registration_open = models.DateTimeField()
    registration_close = models.DateTimeField()
    registration_pay_open = models.DateTimeField(blank=True, default=registration_open)
    registration_pay_close = models.DateTimeField(blank=True, default=registration_close)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    contact_number = models.BigIntegerField(blank=True)
    contact_email = models.EmailField(blank=True)
    location = models.CharField(max_length=500)
    attendant_limit = models.IntegerField(blank=True, default=1000)
    events = models.ManyToManyField(Event)
    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField()
    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        return super(CubingEvent, self).save(*args, **kwargs)
class Registration(models.Model):
    cubing_event = models.ForeignKey(CubingEvent, on_delete=models.CASCADE)
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    events = models.ManyToManyField(Event)
    request = models.TextField(max_length=500, blank=True)
    comment = models.TextField(max_length=500, blank=True)
    class Meta:
        abstract = True
class CompletedRegistration(Registration):
    is_completed = True

class PendingRegistration(Registration):
    is_completed = False