from django import forms
from django.core import validators
from .models import Products, Order


class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = "name","price","description","discount"

class OrderForms(forms.ModelForm):
    class Meta:
        model = Order
        fields = "user","products","products","delivery_address"