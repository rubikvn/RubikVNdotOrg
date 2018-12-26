from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager

from apps.results.models import Country


# Create your models here.
class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, name, password=None, **extra_fields):
        if not email:
            raise ValueError("The given email must be set")
        else:
            email = self.normalize_email(email)
            user = self.model(email=email, name=name, **extra_fields)
            user.set_password(password)
            user.save(self._db)
            return user

    def create_user(self, email, name, password=None, **extra_fields):
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, name, password, **extra_fields)


    def create_superuser(self, email, name, password=None, **extra_fields):
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_superuser") is False:
            raise ValueError("Superuser must have is_superuser = True.")
        return self._create_user(email, name, password, **extra_fields)

    def get_by_natural_key(self, email):
        return self.get(email=email)


class User(AbstractBaseUser):
    # Personal info
    email = models.EmailField(primary_key=True, max_length=80)      # Email used by WCA account will override email used for signup
    wca_id = models.CharField(unique=True, max_length=10, null=True)
    name = models.CharField(max_length=80)
    date_of_birth = models.DateField(null=True)
    gender = models.CharField(max_length=1, null=True)
    country = models.ForeignKey(Country, models.DO_NOTHING, null=True)
    manage_competitions = models.BooleanField(default=False, null=True)

    # OAuth token
    access_token = models.CharField(max_length=80, null=True)
    refresh_token = models.CharField(max_length=80, null=True)
    token_type = models.CharField(max_length=20, null=True)
    token_scope = models.CharField(max_length=50, null=True)
    token_created_at = models.IntegerField(null=True)
    token_expiry = models.IntegerField(null=True)

    # Permissions
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ('name',)

    objects = UserManager()

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

    @property
    def is_active_property(self):
        return self.is_active

    @property
    def is_superuser_property(self):
        return self.is_superuser

    def __str__(self):
        return f"Name: {self.name}, WCA ID: {self.wca_id}, email: {self.email}"
