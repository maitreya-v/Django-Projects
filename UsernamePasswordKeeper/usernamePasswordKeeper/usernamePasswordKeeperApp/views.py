# admin_username=maitreya
# admin_password=maitreya
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import KeeperForm
from .models import Keeper
# Create your views here.


def add(request):
    if request.method=='POST':
        ins=KeeperForm(request.POST)
        if ins.is_valid():
         ins.save()
        ins=KeeperForm()
    else:
        ins=KeeperForm()
    info=Keeper.objects.all()    
    return render(request,'add.html',{'form':ins,'info':info})

def update(request,id):
     if request.method=='POST':
        pi=Keeper.objects.get(pk=id)
        inst=KeeperForm(request.POST,instance=pi)
        if inst.is_valid():
            inst.save()   
     else:
        pi=Keeper.objects.get(pk=id)
        inst=KeeperForm(instance=pi)                 
     return render(request,'update.html',{'inst':inst})

def delete(request,id):
     if request.method=='POST':
        inst=Keeper.objects.get(pk=id)
        inst.delete()    
     return HttpResponseRedirect('/')      