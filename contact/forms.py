from django import forms
from .models import Contactclass
from django.forms import  TextInput , Textarea
class contactform(forms.ModelForm):
    class Meta:
        model = Contactclass
        fields = ['subject','message']
        widgets = {
            'subject': TextInput(attrs={
                'class': "form-control",
                
                'placeholder': ' subject '
                }),
                'message': Textarea(attrs={
                'class': "form-control", 
                
                'placeholder': ' write your message here... '
                })
        }