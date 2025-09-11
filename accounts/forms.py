from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["full_name_kana", "postal_code", "address", "phone", "birthday", "job"]

# CustomUser ではなく標準 User を使う
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

class EmailAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(label="メールアドレス", widget=forms.EmailInput(attrs={
        "class": "form-control",
        "placeholder": "メールアドレス",
        "required": "true",
    }))
    password = forms.CharField(label="パスワード", widget=forms.PasswordInput(attrs={
        "class": "form-control",
        "placeholder": "パスワード",
        "required": "true",
    }))