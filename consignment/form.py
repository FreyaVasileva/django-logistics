from django import forms

from consignment.models import Consignment


class ConsignmentForm(forms.ModelForm):
    class Meta:
        model = Consignment
        fields = '__all__'


class FilterForm(forms.Form):
    ORDER_ASC = 'asc'
    ORDER_DESC = 'desc'

    ORDER_CHOICES = (
        (ORDER_ASC, 'Ascending'),
        (ORDER_DESC, 'Descending'),
    )

    text = forms.CharField(
        required=False,
    )
    order = forms.ChoiceField(
        choices=ORDER_CHOICES,
        required=False,
    )
