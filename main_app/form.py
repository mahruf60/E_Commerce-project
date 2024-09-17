from django import forms
from main_app.models import ContactInfo



class Contactfrom(forms.ModelForm):
    class Meta:
        model=ContactInfo
        fields='__all__'