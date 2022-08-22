from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    TOWN_CHOICES = (
        ('Lagos', 'Lagos'),
        ('Abuja', 'Abuja'),
        ('Ekiti', 'Ekiti '),
    )

    LOCAL_GOVERNMENT_CHOICES = (
        ('Ikeja', 'Ikeja'),
        ('Wuse', 'Wuse'),
        ('Ado', 'Ado'),
    )

    PAYMENT_METHOD_CHOICES = (
        ('Paystack', 'Paystack'),
        ('Flutterwave', 'Flutterwave'),
        ('Quickteller', 'Quickteller')
    )

    division = forms.ChoiceField(choices=TOWN_CHOICES)
    district = forms.ChoiceField(choices=LOCAL_GOVERNMENT_CHOICES)
    payment_method = forms.ChoiceField(
        choices=PAYMENT_METHOD_CHOICES, widget=forms.RadioSelect())   

class Meta:
    model = Order
    fields = ['name', 'email', 'phone', 'address', 'town', 'local_government',
            'zip_code', 'payment_method', 'account_no', 'transaction_id']