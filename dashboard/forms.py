from django import forms
from .models import Vm,Crash,Docker
from django import *

Program_list= [
    ('Select','Select'),
    ('ijgjpeg', 'ijgjpeg'),
    ('Git', 'Git'),
    ('Linux', 'Linux'),
]
onchange="""(function() {

if(this.value=='ijgjpeg'){
    document.getElementById('user_p').value = 'ijgjpeg';
    document.getElementById('dock_hub').value = 'ssgskid/afl-ijgjpeg';
    document.getElementById('fuzzer').value = 'afl';
}
else if(this.value=='Git'){
    document.getElementById('user_p').value = 'Git';
    document.getElementById('dock_hub').value = 'https://Git.com';
    document.getElementById('fuzzer').value = 'afl';
}
else if(this.value=='Linux'){
    document.getElementById('user_p').value = 'Linux';
    document.getElementById('dock_hub').value = 'https://Linux.com';
    document.getElementById('fuzzer').value = 'afl';
}
document.getElementById('user_p').readOnly = true;
document.getElementById('dock_hub').readOnly = true;
document.getElementById('fuzzer').readOnly = true;
if(this.value=='Select'){
    document.getElementById('user_p').value = '';
    document.getElementById('dock_hub').value = '';
    document.getElementById('fuzzer').value = '';
    document.getElementById('user_p').readOnly = false;
    document.getElementById('dock_hub').readOnly = false;
    document.getElementById('fuzzer').readOnly = false;
    }

}.bind(this))()
"""
class DockerForm(forms.ModelForm):
    Program = forms.ChoiceField(choices=Program_list, widget=forms.Select(attrs={'onChange': onchange}),required = False)
    User_Program = forms.CharField(max_length=30,required = False, widget=forms.TextInput(attrs={'class': 'form-control','id':'user_p'}))
    DockerHub = forms.CharField(max_length=70, widget=forms.TextInput(attrs={'placeholder': 'Docker Hub Repo','class':'form-control','id':'dock_hub'}),required = False)
    Docker_Name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'}))
    Fuzzer = forms.CharField(max_length=30,required = False, widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'afl','id':'fuzzer'}))
    Port = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control','value':'35.200.9.22'}))
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