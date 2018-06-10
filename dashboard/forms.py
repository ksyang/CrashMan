from django import forms
from .models import Vm,Crash,Docker
from django import *

Program_list= [
    ('Select','Select'),
    ('ijgjpeg', 'ijgjpeg'),
    ('binutils', 'binutils'),
    ('pcre2', 'pcre2'),
]
onchange="""(function() {

if(this.value=='ijgjpeg'){
    document.getElementById('user_p').value = 'ijgjpeg';
    document.getElementById('dock_hub').value = 'ssgskid/afl-ijgjpeg';
    document.getElementById('fuzzer').value = 'afl';
}
else if(this.value=='binutils'){
    document.getElementById('user_p').value = 'binutils';
    document.getElementById('dock_hub').value = 'ssgskid/afl-binutils';
    document.getElementById('fuzzer').value = 'afl';
}
else if(this.value=='pcre2'){
    document.getElementById('user_p').value = 'pcre2';
    document.getElementById('dock_hub').value = 'ssgskid/afl-pcre2';
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
    Port = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control','value':'http://35.200.9.22:30001'}))
    class Meta:
        model = Docker
        exclude = ()
