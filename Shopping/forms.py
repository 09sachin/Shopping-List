from django import forms
from . import models
from .models import status


class Add_items(forms.ModelForm):
    class Meta:
        model = models.Shopping_list
        fields = ['item_name', 'item_quantity', 'item_status', 'date','person']


class Update_items(forms.ModelForm):
    class Meta:
        model = models.Shopping_list
        exclude = ['person']


class DateFilter(forms.Form):
    date = forms.DateField()


class Add_items_form(forms.Form):
    name = forms.CharField(max_length=500)
    quantity = forms.CharField(max_length=500)
    status = forms.ChoiceField(choices=status)
    date = forms.DateField()
