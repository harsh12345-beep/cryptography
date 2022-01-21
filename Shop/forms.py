from django import forms
from django.forms import fields
from .models import User
from django.contrib.auth.forms import UserCreationForm

class registerform(UserCreationForm):
    Firstname = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-2','placeholder':'Enter Firstname'}))
    Lastname = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-2','placeholder':'Enter Lastname'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-2','placeholder':'Enter username'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control my-2','placeholder':'Enter Email'}))
    password1=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-2','placeholder':'Enter Password','type':'password'}))
    password2=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-2','placeholder':'Confirm Password','type':'password'}))
    class Meta:
        model = User
        fields = ['Firstname','Lastname','username','email','password1','password2']