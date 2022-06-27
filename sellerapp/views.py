from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.http import HttpResponse
# Create your views here.



def index(request):
    return render(request,'index.html')

def reg(request):
    if request.method=='POST':
        a=regform(request.POST)
        if a.is_valid():
            un=a.cleaned_data['usname']
            nm=a.cleaned_data['name']
            ph=a.cleaned_data['phone']
            em=a.cleaned_data['email']
            ps=a.cleaned_data['pswd']
            cps=a.cleaned_data['cpswd']
            if ps==cps:
                b=regmodel(usname=un,name=nm,phone=ph,email=em,pswd=ps)
                b.save()
                return redirect(eml)
        else:
            return HttpResponse("failed")

    return render(request,'registration.html')

def eml(request):
    return render(request,'email send.html')

def log(request):
    if request.method=='POST':
        a=logform(request.POST)
        if a.is_valid():
            em=a.cleaned_data['email']
            ps=a.cleaned_data['pswd']
            b=regmodel.objects.all()
            for i in b:
                if i.email==em and i.pswd==ps:
                    # return HttpResponse("login success")
                    return render(request,'index.html')
            else:
                return HttpResponse("login failed")

    return render(request,'login.html')

def add(request):
    return render(request,'add.html')

def profile_view(request):
    return render(request,'profile.html')

def post_product(request):
    return render(request,'post_product.html')