from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .models import Production as P
from .forms import *
# Create your views here.

Manage=P.objects.all()
def home(request):
    return render(request,'home.html',{'Items':Manage})

def about(request):
    if request.method =="POST":
         data=Production_form(request.POST,request.FILES)
         if data.is_valid:
             print(request.POST)
             data.save()
    return render(request,'about.html',{'form':Production_form})

def Login_Page(request):
    if request.method =="POST":
        user=authenticate(username=request.POST['username'],password=request.POST['password'])
        print(user)
        if user is not None:
            login(request,user)
            return redirect("Home")
        else:
            context={'error':'Invalid username or password'}
        return render(request,'LogInPage.html',context)
    return render(request,'LogInPage.html')

def Logout_page(request):
    logout(request)
    return redirect("logout")

def delete_data(request,id):
    data=P.objects.get(id=id)
    data.delete()
    return redirect('Action')

def listItems(request):
    data=P.objects.all()
    return render(request,'list.html',{'Items':data})


def update_data(request,id):
    data=P.objects.get(id=id)
    data1=Production_form(request.POST,request.FILES, instance=data)
    print(data1)
    if request.method =="POST":
        data.Name=request.POST['name']
        data.Price=request.POST['price']
        data.Image=request.FILES['image']
        data.save()
        return redirect('Action')
    return render(request,'update.html',{'Items':data})
