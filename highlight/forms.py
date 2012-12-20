from django import forms
from django.forms import Textarea, ModelForm
from highlight.models import Code

class CodeForm(forms.ModelForm):
    
    class Meta:
        model = Code
        exclude = ('owner',)
        widgets = {
            'snippet': Textarea(attrs={'cols': 300, 'rows': 30}),
        }
        