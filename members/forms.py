from django import forms
from accounts.models import Profile
from members.models import PaymentMethod

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["full_name", "postal_code", "address", "phone", "birthday", "job"]

class PaymentForm(forms.ModelForm):
    class Meta:
        model = PaymentMethod
        fields = ["card_type", "card_name", "card_number", "expiration_date", "security_code"]

class SubscriptionForm(forms.Form):
    card_holder = forms.CharField(
        label="カード名義人",
        max_length=100,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "山田 太郎"})
    )
    card_number = forms.CharField(
        label="カード番号",
        max_length=16,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "4242424242424242"})
    )
    exp_month = forms.CharField(
        label="有効期限(月)",
        max_length=2,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "12"})
    )
    exp_year = forms.CharField(
        label="有効期限(年)",
        max_length=4,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "2030"})
    )
    cvc = forms.CharField(
        label="セキュリティコード",
        max_length=4,
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "123"})
    )
    postal_code = forms.CharField(
        label="郵便番号",
        max_length=7,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "1234567"})
    )
