from django import forms

class edit_cart(forms.Form):
    quantitat = forms.IntegerField(min_value=1, widget=forms.NumberInput(attrs={'autofocus':'autofocus'}))