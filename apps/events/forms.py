from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import User


class UserCreationForm(forms.ModelForm):
    """
    Form for creating new users. Required fields are:
        - Email
        - Name
        - Password
        - Password confirmation
    """
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ("email", "name", )

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Password don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserUpdateForm(forms.ModelForm):
    """
    A form for updating user profiles. This form includes all the editable
    fields on the user, but replaces the password field with admin's password
    hash display field.s
    """
    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)
        instance = getattr(self, "instance", None)
        if instance and instance.wca_id:
            self.fields["name"].widget.attrs["readonly"] = True
            self.fields["date_of_birth"].widget.attrs["readonly"] = True
            self.fields["gender"].widget.attrs["readonly"] = True
            self.fields["country"].widget.attrs["readonly"] = True
        self.fields["password"] = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = (
            "email",
            "password",
            "name",
            "date_of_birth",
            "gender",
            "country",
            "wca_id",
        )
        # Render some fields as read-only if the user has connected with WCA
        widgets = {
            "email": forms.TextInput(attrs={"readonly": True}),
            "wca_id": forms.TextInput(attrs={"readonly": True})
        }

    def clean_password(self):
        # Regardless of what the user provides, return the initial value
        # This is done here, rather than on the field
        # because the field does not have access to the initial value
        return self.initial["password"]
