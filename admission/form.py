from django import forms
from .models import Admission
from django.contrib.auth.models import User

class AdmissionForm(forms.ModelForm):
    class Meta:
        model = Admission
        fields = '__all__'

class SignUpform(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','password','first_name','last_name','email']