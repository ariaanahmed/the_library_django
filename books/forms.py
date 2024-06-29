from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Book, Review


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(
        max_length=60,
        required=True,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Username"}),
    )


    first_name = forms.CharField(
        max_length=60,
        required=True,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "First name"}),
    )


    last_name = forms.CharField(
        max_length=60,
        required=True,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Last name"}),
    )


    email = forms.EmailField(
        max_length=50,
        label="",
        required=True,
        widget=forms.EmailInput(attrs={"placeholder": "Email address"}),
    )


    password1 = forms.CharField(
        label="",
        required=True,
        widget=forms.PasswordInput(attrs={"placeholder": "Password"}),
    )


    password2 = forms.CharField(
        label="",
        required=True,
        widget=forms.PasswordInput(attrs={"placeholder": "Confirm password"}),
    )


    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        ]


class DepositForm(forms.Form):
    amount = forms.DecimalField(label="Amount to Deposit")


class ReturnForm(forms.Form):
    book_id = forms.IntegerField(label="Book ID")


class UserProfileForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name"]


class BorrowBookForm(forms.Form):
    book = forms.ModelChoiceField(queryset=Book.objects.all(), empty_label=None)


class ReturnBookForm(forms.Form):
    book = forms.ModelChoiceField(queryset=Book.objects.all(), empty_label=None)


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["text", "rating"]