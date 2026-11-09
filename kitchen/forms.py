from django import forms


class DishSearchForm(forms.Form):
    name = forms.CharField(required=False)


class CookSearchForm(forms.Form):
    username = forms.CharField(required=False)


class DishTypeSearchForm(forms.Form):
    name = forms.CharField(required=False)
