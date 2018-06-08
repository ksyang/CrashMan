from django.shortcuts import render,redirect,HttpResponse
from .models import Vm,Crash,Docker
from .forms import DockerForm

def post_list(request):
    Vms = Vm.objects.all()
    Vm_number=Vm.objects.all().count()
    Crash_number=Crash.objects.all().count()
    Docker_number=Docker.objects.all().count()
    return render(request, 'dashboard/post_list.html', {'Vm':Vms,'Vmnum':Vm_number,'Crashnum':Crash_number,'Dockernum':Docker_number})

def form_view(request):
    form=DockerForm()
    Dockers=Docker.objects.all()
    if request.method == "POST":
        form = DockerForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            dockerhub_url=request.POST['DockerHub']
            if request.POST['User_Program']!="":
                form.Program=request.POST['User_Program']
            if form.Fuzzer=="":
                form.Fuzzer="afl"
            form.save()
            return redirect('form_view')
        else:
            form = DockerForm()
    return render(request, 'dashboard/form.html',{'form':form,'Dockers':Dockers})

def crash_view(request,ip,program):
    Crashs = Crash.objects.filter(VM_ip=ip,Program=program)
    return render(request,'dashboard/crash_list.html',{'crashs':Crashs})

def vm_delete(request,Vm_name):
    vm=Vm.objects.all().filter(VM_Name=Vm_name)
    for i in vm:
        Crash.objects.filter(Program=i.Program,VM_ip=i.VM_ip).delete()
    Vm.objects.filter(VM_Name=Vm_name).delete()
    return redirect('post_list')

def docker_delete(request,Docker_name):
    Docker.objects.filter(Docker_Name=Docker_name).delete()
    Vm.objects.filter(VM_Name=Docker_name).delete()
    return redirect('form_view')