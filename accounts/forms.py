from django import forms
from accounts.models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["furigana", "postal_code", "address", "phone_number", "birthday", "job"]