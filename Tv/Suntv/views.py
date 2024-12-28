# Create your views here.


from rest_framework import viewsets
from rest_framework.response import Response
from .models import*
from .serializer import*


class Details(viewsets.ModelViewSet):

    queryset=Fund.objects.all()
    serializer_class=Fund_form

class Gift(viewsets.ModelViewSet):

    queryset=Coopen.objects.all()
    serializer_class=Coopen_form


