from django.db import models
from django.utils import timezone
from django import *

class Vm(models.Model):
    VM_Name = models.CharField(max_length=100,primary_key=True)
    VM_ip = models.CharField(max_length=20)
    Program = models.CharField(max_length=30)
    Port = models.CharField(max_length=10)
    Fuzzer = models.CharField(max_length=30)
    Os=models.CharField(max_length=10)

class Crash(models.Model):
    Crash_Name = models.CharField(max_length=100,primary_key=True)
    Exploitable = models.CharField(max_length=50)
    Date = models.DateTimeField(blank=True, null=True)
    Program = models.CharField(max_length=50)
    VM_ip = models.CharField(max_length=20)

class Docker(models.Model):
    Docker_Name = models.CharField(max_length=30,primary_key=True)
    Program = models.CharField(max_length=30)
    Fuzzer = models.CharField(max_length=30)
    Port = models.CharField(max_length=30)
