from django.shortcuts import render,redirect,HttpResponse
from .models import Vm,Crash,Docker
from .forms import DockerForm
from .dockerLib.dockerLib import *
from .pingLib.pingLib import *

def post_list(request):

    Vms = Vm.objects.all()
    Vm_number=Vm.objects.all().count()
    Crash_number=Crash.objects.all().count()
    Docker_number=Docker.objects.all().count()
    if 'DelSuc' not in request.session:
        request.session['DelSuc']='No'
    result = request.session['DelSuc']
    request.session['DelSuc']='No'
    if result=='Suc':
        DelSuc=1
        return render(request, 'dashboard/post_list.html', {'Vm':Vms,'Vmnum':Vm_number,'Crashnum':Crash_number,'Dockernum':Docker_number,'DelSuc':DelSuc})

    if 'PingResult' not in request.session:
        request.session['PingResult']='No'
    PingResult = request.session['PingResult']
    request.session['PingResult']='No'
    if PingResult=='success':
        return render(request, 'dashboard/post_list.html', {'Vm':Vms,'Vmnum':Vm_number,'Crashnum':Crash_number,'Dockernum':Docker_number,'PingResult':PingResult})
    elif PingResult=='fail':
        return render(request, 'dashboard/post_list.html', {'Vm':Vms,'Vmnum':Vm_number,'Crashnum':Crash_number,'Dockernum':Docker_number,'PingResult':PingResult})
    
    return render(request, 'dashboard/post_list.html', {'Vm':Vms,'Vmnum':Vm_number,'Crashnum':Crash_number,'Dockernum':Docker_number})

def form_view(request):
    form=DockerForm()
    Dockers=Docker.objects.all()
    Docker_number=Docker.objects.all().count()
    if 'DocSuc' not in request.session:
        request.session['DocSuc']='No'
    docresult = request.session['DocSuc']
    request.session['DocSuc']='No'
    if 'DelSuc' not in request.session:
        request.session['DelSuc']='No'
    delresult = request.session['DelSuc']
    request.session['DelSuc']='No'
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
            dockerRun(form.Docker_Name, form.Program, form.Fuzzer, dockerhub_url, form.Port)
            request.session['DocSuc']="Suc"
            return redirect('form_view')
        else:
            form = DockerForm()
    if docresult=='Suc':
        DocSuc=1
        return render(request, 'dashboard/form.html',{'form':form,'Dockers':Dockers,'Dockernum':Docker_number,'DocSuc':DocSuc})
    if delresult=='Suc':
        DelSuc=1
        return render(request, 'dashboard/form.html',{'form':form,'Dockers':Dockers,'Dockernum':Docker_number,'DelSuc':DelSuc})
    return render(request, 'dashboard/form.html',{'form':form,'Dockers':Dockers,'Dockernum':Docker_number})

def crash_view(request,ip,program):
    Crashs = Crash.objects.filter(VM_ip=ip,Program=program)
    return render(request,'dashboard/crash_list.html',{'crashs':Crashs})

def vm_delete(request,Vm_name):
    vm=Vm.objects.all().filter(VM_Name=Vm_name)
    for i in vm:
        Crash.objects.filter(Program=i.Program,VM_ip=i.VM_ip).delete()
    Vm.objects.filter(VM_Name=Vm_name).delete()
    request.session['DelSuc']="Suc"
    return redirect('post_list')

def docker_delete(request,Docker_name):
    Docker.objects.filter(Docker_Name=Docker_name).delete()
    vm=Vm.objects.get(VM_Name=Docker_name)
    dockerStop(Docker_name)
    request.session['DelSuc']="Suc"
    Crash.objects.filter(Program=vm.Program,VM_ip=vm.VM_ip).delete()    
    Vm.objects.filter(VM_Name=Docker_name).delete()
    return redirect('form_view')

def ping(request, IP, Port):
    request.session['PingResult'] = sendPing(str(IP), int(Port))
    return redirect('post_list')
