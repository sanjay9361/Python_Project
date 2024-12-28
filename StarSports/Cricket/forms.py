from django.forms import *
from . models import *

class Sports_form(ModelForm):
    class Meta:
        model=Sports
        fields='__all__'