from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser

from django.contrib.auth.models import BaseUserManager

from apps.results.models import Country
from apps.results.models import Event
from django.utils import timezone
from datetime import datetime
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, name, password=None):
        """
        Creates and saves a User with the given email, name and password.
        """
        if not email:
            raise ValueError("Users must have an email address")
        user = self.model(
            email=self.normalize_email(email),
            name=name
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password=None):
        """
        Creates and saves a super User with the given email, name and password.
        """
        user = self.create_user(email,
            password=password,
            name=name
        )
        user.is_superuser = True
        user.save(using=self._db)
        return user

    def get_by_natural_key(self, email):
        return self.get(email=email)


class User(AbstractBaseUser):
    # Personal info
    # Email used by WCA account will override email used for signup
    email = models.EmailField(unique=True, max_length=80)
    name = models.CharField(max_length=80)
    date_of_birth = models.DateField(null=True)
    gender = models.CharField(max_length=1, null=True)
    country = models.ForeignKey(Country, models.DO_NOTHING, null=True)
    manage_competitions = models.BooleanField(default=False, null=True)

    # OAuth token
    wca_id = models.CharField(unique=True, max_length=10, null=True, blank=True)
    access_token = models.CharField(max_length=80, null=True, blank=True)
    refresh_token = models.CharField(max_length=80, null=True, blank=True)
    token_type = models.CharField(max_length=20, null=True, blank=True)
    token_scope = models.CharField(max_length=50, null=True, blank=True)
    token_created_at = models.IntegerField(null=True, blank=True)
    token_expiry = models.IntegerField(null=True, blank=True)

    # Permissions
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ('name',)

    objects = UserManager()

    class Meta:
        db_table = 'User'

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

    def natural_key(self):
        return 'email'

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name.split(" ")[-1]

    def can_manage_comps(self):
        return self.manage_competitions

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_superuser

    def __str__(self):
        return f"Name: {self.name}, WCA ID: {self.wca_id}, email: {self.email}"


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
        if self.registration_pay_open is None:
            self.registration_pay_open = self.registration_open
        if self.registration_pay_close is None:
            self.registration_pay_close = self.registration_close
        self.full_clean()
        return super(CubingEvent, self).save(*args, **kwargs)

    def clean(self):
        self._registration_validate()
        self._start_end_date_validate()
        self._valid_time_validate()

    def _registration_validate(self):
        if self.registration_open is None or self.registration_close is None:
            raise ValidationError(
                "Neither registration open date nor registration close date can be null")

    def _start_end_date_validate(self):
        if self.start_date is None or self.end_date is None:
            raise ValidationError(
                "Neither start_date nore end date can be null"
            )

    def _valid_time_validate(self):
        # Code refactor will be done in future
        if self.end_date < self.start_date:
            raise ValidationError(
                "End date cannot be before start date"
            )

        if self.registration_close < self.registration_open:
            raise ValidationError(
                "Registration close date cannot be before registration open date"
            )
        if self.registration_pay_close < self.registration_pay_open:
            raise ValidationError(
                "Registration pay close date cannot be before registration pay open date"
            )
        if self.start_date < self.registration_open:
            raise ValidationError(
                "Start date cannot be before registration open date"
            )
        if self.end_date < self.registration_close:
            raise ValidationError(
                "End date cannot be before registration close date"
            )
        if self.registration_pay_open < self.registration_open:
            raise ValidationError(
                "Registration pay open date cannot be before registration open date"
            )
        if self.registration_close < self.registration_pay_close:
            raise ValidationError(
                "Registration close date cannot be before registration pay close date"
            )


class Registration(models.Model):
    cubing_event = models.ForeignKey(CubingEvent, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, default=None, blank=False)
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
