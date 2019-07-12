from django import forms

class ZipCode(forms.Form):
    zip_code = forms.CharField(max_length=5)
