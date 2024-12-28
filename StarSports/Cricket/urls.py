from django.urls import path
from . import views

urlpatterns = [
    
    path('1/',views.home, name="HOME"),
    path('2/',views.LogIn_Page, name="LOGINPAGE"),
    path('3/',views.LogOut_Page),
    path('4/',views.Detail),
    path('list/',views.List_Page,name="ACTION"),
    path('update/<id>',views.UpDate_Page),
    path('delete/<id>',views.Delete_Page),
    path('7/',views.Ticket_Page)
]