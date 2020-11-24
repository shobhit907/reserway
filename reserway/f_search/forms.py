from django import forms

class SearchForm(forms.Form):
    source = forms.CharField(label='Source Station:', max_length=100, required=True)
    destination = forms.CharField(label='Destination Station:', max_length=100, required=True)