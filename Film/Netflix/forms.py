from django.forms import *
from .models import *

class Production_form(ModelForm):
    class Meta:
        model=Production
        fields='__all__'



