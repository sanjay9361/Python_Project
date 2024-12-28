from django.urls import path
from . import views

urlpatterns = [
    path('1/', views.home, name="Home"),
      path('2/', views.about),
      path('3/',views.Login_Page, name="logout" ),
      path('4/',views.Logout_page),
      path('action/',views.listItems ,name='Action'),
      path('delete/<id>',views.delete_data),
      path('update/<id>',views.update_data),

]