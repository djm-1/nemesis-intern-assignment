from django.forms import ModelForm
from .models import UserProfile
#form for registration
class RegisterForm(ModelForm):
    class Meta:
        model=UserProfile
        fields=["user","address"]