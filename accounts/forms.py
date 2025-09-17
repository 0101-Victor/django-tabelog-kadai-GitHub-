from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Profile
from django.core.exceptions import ValidationError


# User + Profile 同時登録用フォーム
class UserProfileCreationForm(UserCreationForm):
    # Userフィールド
    email = forms.EmailField(required=True)

    # Profileフィールド
    full_name = forms.CharField(max_length=100, required=True)
    full_name_kana = forms.CharField(max_length=100, required=True)
    postal_code = forms.CharField(max_length=10, required=True)
    address = forms.CharField(max_length=255, required=True)
    phone = forms.CharField(max_length=15, required=True)
    birthday = forms.DateField(required=False, widget=forms.DateInput(attrs={"type": "date"}))
    job = forms.CharField(max_length=50, required=False)

    class Meta:
        model = User
        fields = ("email", "password1", "password2")

    def clean_email(self):
        email = self.cleaned_data["email"]
        if User.objects.filter(email=email).exists():
            raise ValidationError("このメールアドレスはすでに登録されています。")
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        # username を email と同じにする（管理画面でも扱いやすい）
        user.username = self.cleaned_data["email"]

        if commit:
            user.save()
        return user


# メールアドレスでログインするフォーム
class EmailAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(
        label="メールアドレス",
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "メールアドレス",
                "required": "true",
            }
        ),
    )
    password = forms.CharField(
        label="パスワード",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "パスワード",
                "required": "true",
            }
        ),
    )


# プロフィール編集用フォーム ← ★ここを追加
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            "full_name",
            "full_name_kana",
            "postal_code",
            "address",
            "phone",
            "birthday",
            "job",
        ]
