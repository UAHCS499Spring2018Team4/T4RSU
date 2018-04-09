from django import forms

class HomeForm(forms.Form):
    address = forms.CharField()
    description = forms.CharField()
    isOccupied = forms.BooleanField()



