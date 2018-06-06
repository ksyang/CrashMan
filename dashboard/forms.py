from django import forms
from .models import Vm,Crash,Docker
from django import *

Program_list= [
    ('ImageMagick', 'ImageMagick'),
    ('cantaloupe', 'Cantaloupes'),
    ('mango', 'Mangoes'),
    ('honeydew', 'Honeydews'),
]

class DockerForm(forms.ModelForm):
    Program = forms.CharField(max_length=30, widget=forms.Select(choices=Program_list),required = False)
    User_Program = forms.CharField(max_length=30,required = False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    DockerHub = forms.CharField(max_length=70, widget=forms.TextInput(attrs={'placeholder': 'https://example.com','class':'form-control'}),required = False)
    Docker_Name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'}))
    Fuzzer = forms.CharField(max_length=30,required = False, widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'afl'}))
    Port = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Docker
        exclude = ()
'''
class UserForm(forms.Form):
    first_name= forms.CharField(max_length=100)
    last_name= forms.CharField(max_length=100)
    email= forms.EmailField()
    age= forms.IntegerField()
    favorite_fruit= forms.CharField(label='What is your want run program', widget=forms.Select(choices=FRUIT_CHOICES))
    '''