from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import User
from .forms import UserCreationForm, UserUpdateForm


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserUpdateForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model
    # These override the definitions on the base UserAdmin that reference
    # specific fields on auth.User
    list_display = ("email", "name", "date_of_birth", "is_superuser", )
    list_filter = ("is_superuser", )
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal info", {"fields": ("date_of_birth", "wca_id")}),
        ("Permissions", {"fields": ("is_superuser",)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin overrides
    # get fields_sets to user this attribute when creating a user
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "name", "password1", "password2")
        }),
    )
    search_fields = ("email",)
    ordering = ("email",)
    readonly_fields = ("email", "wca_id", )
    filter_horizontal = ()

# Register the new UserAdmin
admin.site.register(User, UserAdmin)
# Since we're not using Django's built-in permissions,
# unregister the Group model from admin
admin.site.unregister(Group)
