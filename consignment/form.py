from django import forms

from consignment.models import Consignment


class ConsignmentForm(forms.ModelForm):
    class Meta:
        model = Consignment
        fields = '__all__'
