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