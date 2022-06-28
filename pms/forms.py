from django import forms
from .models import Pensioner

class PensionerForm(forms.ModelForm):
    
    class Meta:
        model=Pensioner
        field="__all__"
