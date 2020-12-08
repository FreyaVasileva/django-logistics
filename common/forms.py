from django.forms import ModelForm
from django.forms import Textarea

from common.models import Contact


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
