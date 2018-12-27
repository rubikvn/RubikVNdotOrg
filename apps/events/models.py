from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from apps.results.models import Country
from apps.results.models import Event
from django.utils import timezone
from datetime import datetime
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


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
    country = models.ForeignKey(Country, models.DO_NOTHING, default='', blank=True)
    manage_competitions = models.BooleanField(default=False)

    # TODO: store access tokens for wca api, and expiry dates as well
    access_token = models.CharField(max_length=80, blank=True)
    refresh_token = models.CharField(max_length=80, blank=True)
    token_type = models.CharField(max_length=20, blank=True)
    token_scope = models.CharField(max_length=50, blank=True)
    token_created_at = models.IntegerField(blank=True, null=True)
    token_expiry = models.IntegerField(blank=True, null=True)

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
    type_of_event = (
        ('wca', 'WCA events'),
        ('offline', 'Offline events')
    )
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100, choices=type_of_event, default='offline')
    delegates = models.ManyToManyField(User, related_name='delagated_events')
    non_wca_organizers = models.CharField(max_length=200, blank=True)
    wca_organizers = models.ManyToManyField(User)
    registered = models.ManyToManyField(User, through='CompletedRegistration', related_name='registered_events')
    waitlisted = models.ManyToManyField(User, through='PendingRegistration', related_name='waitlisted_events')
    city_name = models.CharField(max_length=100)
    # info_url = models.
    registration_open = models.DateTimeField()
    registration_close = models.DateTimeField()
    registration_pay_open = models.DateTimeField(blank=True)
    registration_pay_close = models.DateTimeField(blank=True)
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
            self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if(self.registration_pay_open is None):
            self.registration_pay_open = self.registration_open
        if (self.registration_pay_close is None):
            self.registration_pay_close = self.registration_close
        self.full_clean()
        return super(CubingEvent, self).save(*args, **kwargs)

    def clean(self):
        self.__registration_validate()
        self.__start_end_date_validate()
        self.__valid_time_validate()

    def __registration_validate(self):
        if (self.registration_open is None or self.registration_close is None):
            raise ValidationError(
                "Neither registration open date nor registration close date can be null")
    def __start_end_date_validate(self):
        if(self.start_date is None or self.end_date is None):
            raise ValidationError(
                "Neither start_date nore end date can be null"
            )
    def __valid_time_validate(self):
        # Code refactor will be done in future
        if (self.end_date < self.start_date):
            raise ValidationError(
                "End date cannot be before start date"
            )
        if (self.registration_close < self.registration_open):
            raise ValidationError(
                "Registration close date cannot be before registration open date"
            )
        if (self.registration_pay_close < self.registration_pay_open):
            raise ValidationError(
                "Registration pay close date cannot be before registration pay open date"
            )
        if (self.start_date < self.registration_open):
            raise ValidationError(
                "Start date cannot be before registration open date"
            )
        if (self.end_date < self.registration_close):
            raise ValidationError(
                "End date cannot be before registration close date"
            )
        if (self.registration_pay_open < self.registration_open):
            raise ValidationError(
                "Registration pay open date cannot be before registration open date"
            )
        if (self.registration_close < self.registration_pay_close):
            raise ValidationError(
                "Registration close date cannot be before registration pay close date"
            )



class Registration(models.Model):
    cubing_event = models.ForeignKey(CubingEvent, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE,default='null', blank=False)
    events = models.ManyToManyField(Event)
    request = models.TextField(max_length=500, blank=True)
    comment = models.TextField(max_length=500, blank=True)
    class Meta:
        abstract = True
    def save(self, *args, **kwargs):
        self.full_clean()
        return super(Registration, self).save(*args, **kwargs)
class CompletedRegistration(Registration):
    is_completed = True

    def clean(self, exclude=None):
        try: 
            PendingRegistration.objects.get(user=self.user)
        except:
            return;
        else:
            raise ValidationError("An user can only have 1 reg")    

class PendingRegistration(Registration):
    is_completed = False
    def clean(self, exclude=None):
        try:
            CompletedRegistration.objects.get(user=self.user)
        except:
            return;
        else:
            raise ValidationError("An user can only have 1 reg")
