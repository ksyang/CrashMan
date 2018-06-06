from django.db import models
from django.utils import timezone


class Vm(models.Model):
    VM_Name = models.CharField(max_length=30)
    VM_ip = models.CharField(max_length=20)
    Program = models.CharField(max_length=30)
    Port = models.CharField(max_length=10)
    Fuzzer = models.CharField(max_length=30)
class Crash(models.Model):
    Crash_Name = models.CharField(max_length=30)
    Exploitable = models.CharField(max_length=30)
    Date = models.DateTimeField(blank=True, null=True)
    Program = models.CharField(max_length=30)
    VM_ip = models.CharField(max_length=20)
