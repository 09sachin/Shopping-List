from django import forms
from . import models


class Add_items(forms.ModelForm):
    class Meta:
        model = models.Shopping_list
        fields = ['item_name', 'item_quantity', 'item_status', 'date','person']


class DateFilter(forms.Form):
    date = forms.DateField()
