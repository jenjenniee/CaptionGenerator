from django import forms
from .models import Caption

class CaptionForm(forms.ModelForm):
    class Meta:
        model = Caption
        fields = ['image']
