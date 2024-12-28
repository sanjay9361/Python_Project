from django.urls import path
from . import views
urlpatterns = [
    path('1/',views.home ,name="HOME" ),
    path('2/',views.about ),
    path('3/',views.getDetails),
    path('4/',views.Billing),
    path('5/',views.Login_page ,name="login_page"),
    path('6/',views.Logout_page),
    path('action/',views.listItems, name='Action'),
    path('update/<id>',views.update_data),
    path('delete/<id>',views.delete_data),
]