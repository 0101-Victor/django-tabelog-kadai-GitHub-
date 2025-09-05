from django import forms
from accounts.models import Profile
from members.models import PaymentMethod

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["furigana", "postal_code", "address", "phone_number", "birthday", "job"]

class PaymentForm(forms.ModelForm):
    class Meta:
        model = PaymentMethod
        fields = ["card_type", "card_name", "card_number", "expiration_date", "security_code"]