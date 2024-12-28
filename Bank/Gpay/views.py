from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render,redirect
from .models import Foods as V
from  .forms import *
# Create your views here.


title='STATE BANK'
Manage=V.objects.all()

def home(request):
    
    return render(request,'server/home.html',{'Heading':title,'Items':Manage})

def about(request):
    return render(request,'server/about.html')

def getDetails(request):
    if request.method =="POST":
         data=Foods_form(request.POST)
         if data.is_valid:
              print(request.POST)
              data.save()
    return render(request,'server/getDetails.html',{'form':Foods_form()})

def Billing(request):
    if request.method =="POST":
        data=Bill_Items_Form(request.POST)
        if data.is_valid:
            print(request.POST)
            data.save()
    return render(request,'server/Bill_Desk.html',{'Bill':Bill_Items_Form})


def Login_page(request):
    if request.method =="POST":
        user =authenticate(username=request.POST['username'],password=request.POST['password'])
        print(user)
        if user is not None:
            login(request,user)
            return redirect("HOME")
        else:
            context={'error':'Invalid Username or Password'}
        return render(request,'server/LogInPage.html',context)
    return render(request,'server/LogInPage.html')


def Logout_page(request):
    logout(request)
    return redirect("login_page")


def delete_data(request,id):
    data=V.objects.get(id=id)
    data.delete()
    return redirect('Action')


def listItems(request):
    data=V.objects.all()
    return render(request,'server/list.html',{'Items':data})

def update_data(request,id):
    data=V.objects.get(id=id)
    data1=Foods_form(request.POST,request.FILES, instance=data)
    print(data1)
    if request.method=="POST":
        data.Name=request.POST['name']
        data.Price=request.POST['price']
        data.Image=request.FILES['image']
        data.save()
        return redirect('Action')
    return render(request,'server/update.html',{'Items':data})

