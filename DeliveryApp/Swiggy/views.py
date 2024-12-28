from django.shortcuts import render
from .models import Products as V
# Create your views here.



def home(request):
    title='Swiggy'
    Foods=V.objects.all()
    return render(request,'Swiggy/home.html',{'Heading':title,'Items':Foods})
def about(request):
    title='Zomoto'
    Foods=[{'id':1,'Name':'Idli','price':10},
           {'id':2,'Name':'Dosa','price':50},
           {'id':3,'Name':'Parotta','price':15},
           {'id':4,'Name':'Briyani','price':230},
           {'id':5,'Name':'Curdrice','price':50},
           {'id':6,'Name':'Noodles','price':190}]
    return render(request,'swiggy/about.html',{'Heading':title,'Items':Foods})
def content(request):
    return render(request,'Swiggy/content.html')