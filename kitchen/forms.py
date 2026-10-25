from django import forms


class DishSearchForm(forms.Form):
    name = forms.CharField(required=False)