from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['first_name', 'last_name', 'city', 'subject']


        labels = {
            'first_name': 'Adınız',
            'last_name': 'Soy Adınız',
            'city': 'Şehir',
            'subject': 'Konu',
        }
