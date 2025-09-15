from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Profile


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

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        # username を email と同じにする（管理画面でも扱いやすい）
        user.username = self.cleaned_data["email"]

        if commit:
            user.save()
            # Profile も一緒に作成
            Profile.objects.create(
                user=user,
                full_name=self.cleaned_data["full_name"],
                full_name_kana=self.cleaned_data["full_name_kana"],
                postal_code=self.cleaned_data["postal_code"],
                address=self.cleaned_data["address"],
                phone=self.cleaned_data["phone"],
                birthday=self.cleaned_data.get("birthday"),
                job=self.cleaned_data.get("job"),
            )
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
