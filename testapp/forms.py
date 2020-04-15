from django import forms
from testapp.models import Register

class Registration_Form(forms.ModelForm):
    class Meta():
        model=Register
        fields="__all__"
