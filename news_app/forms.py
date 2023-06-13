from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = '__all__'  # ['name','email','message'] shuni orniga __all__ dan foydalandik

class SubscriptionForm(forms.Form):
    subject = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField()








