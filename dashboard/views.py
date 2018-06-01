from django.shortcuts import render
from .models import Vm,Crash

def post_list(request):
	Vms = Vm.objects.all()
	Vm_number=Vm.objects.all().count()
	Crash_number=Crash.objects.all().count()
	return render(request, 'dashboard/post_list.html', {'Vm':Vms,'Vmnum':Vm_number,'Crashnum':Crash_number})

def form_view(request):
	return render(request, 'dashboard/form.html')
