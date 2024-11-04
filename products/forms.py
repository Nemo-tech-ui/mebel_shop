from django import forms
from .models import Messages

class Message_forms(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'contact__section-input', 'placeholder': 'Имя'
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'contact__section-input', 'placeholder': 'Адрес электронной почты'
    }))
    message = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'contact__section-input', 'placeholder': ' Пиши Сообшение'
    }))
    class Meta:
        model = Messages
        fields  =('name', 'email', 'message')
