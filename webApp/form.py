from django import forms
from .models import *


class ProductForm(forms.Form):
    
    Name = forms.CharField(max_length=200)
    Price = forms.FloatField()
    Quantity = forms.IntegerField()
    # Entrance_Date = forms.DateField()
    # Expired_Date = forms.DateField()
    # Approved_By = forms.ModelMultipleChoiceField(queryset = User.objects.all())
    # Total_Price = forms.FloatField(default=0)


class SellForm(forms.Form):
    name = forms.ModelChoiceField(queryset= Product.objects.all())
    # print(name)
    # price = forms.FloatField()
    quantity = forms.IntegerField()


class SolledBy(forms.Form):
    # item = forms.ModelChoiceField(queryset = Solled.objects.all())
    user = forms.ModelChoiceField(queryset = Profile.objects.all())
