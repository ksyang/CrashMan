from django.shortcuts import render,redirect
from .models import Vm,Crash

def post_list(request):
	Vms = Vm.objects.all()
	Vm_number=Vm.objects.all().count()
	Crash_number=Crash.objects.all().count()
	return render(request, 'dashboard/post_list.html', {'Vm':Vms,'Vmnum':Vm_number,'Crashnum':Crash_number})

def form_view(request):
	return render(request, 'dashboard/form.html')

def crash_view(request,ip,program):
	Crashs = Crash.objects.filter(VM_ip=ip,Program=program)
	return render(request,'dashboard/crash_list.html',{'crashs':Crashs})

def vm_delete(request,Vm_name):
	vm=Vm.objects.all().filter(VM_Name=Vm_name)
	for i in vm:
		print (i.VM_Name)
		Crash.objects.filter(Program=i.Program,VM_ip=i.VM_ip).delete()
	Vm.objects.filter(VM_Name=Vm_name).delete()
	
	return redirect('post_list')

