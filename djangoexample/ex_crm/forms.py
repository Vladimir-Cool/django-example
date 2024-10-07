from django import forms

from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('order_name', 'order_phone',)

        widgets = {
            'order_name': forms.TextInput(attrs={'class': 'form-control'}),
            'order_phone': forms.TextInput(attrs={'class': 'form-control'})
        }


    # order_name = forms.CharField(max_length=200)
    # order_phone = forms.CharField(max_length=200)
