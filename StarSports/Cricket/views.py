from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render,redirect
from .models import Sports as S
from .forms import *
# Create your views here.


Manage=S.objects.all()

def home(request):
    return render(request,'home.html',{'Items':Manage})



def LogIn_Page(request):
    if request.method =="POST":
        user=authenticate(username=request.POST['username'],password=request.POST['password'])
        print(user)
        if user is not None:
            login(request,user)
            return redirect("HOME")
        else:
            context={'error':'Invalid Username and PassWord'}
        return render(request,'loginpage.html',context)
    return render(request,'loginpage.html')

def LogOut_Page(request):
    logout(request)
    return redirect("LOGINPAGE")

def Detail(request):
    if request.method =="POST":
        data=Sports_form(request.POST, request.FILES)
        print(request.POST)
        if data.is_valid:
            data.save()
    return render(request,'detail.html',{'form':Sports_form()})

def List_Page(request):
    data=S.objects.all()
    return render(request,'list.html',{'Items':data})

def UpDate_Page(request,id):
    data=S.objects.get(id=id)
    data1=Sports_form(request.POST,request.FILES,instance=data)
    print(data1)
    if request.method =="POST":
        data.Name=request.POST['Name']
        data.Image=request.FILES['Image']
        data.Time=request.POST['Time']
        data.save()
        return redirect("ACTION")
    return render(request,'update.html',{'Items':data})

def Delete_Page(request,id):
    data=S.objects.get(id=id)
    data.delete()
    return redirect("ACTION")

def Ticket_Page(request):
    return render(request,'ticket.html')





