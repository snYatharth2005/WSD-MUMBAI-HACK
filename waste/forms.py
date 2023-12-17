# myapp/forms.py
from django import forms

class UserInputForm(forms.Form):
    user_input = forms.CharField(label='User Input')