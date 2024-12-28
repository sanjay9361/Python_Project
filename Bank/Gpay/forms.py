from django.forms import *
from .models import *

class Foods_form(ModelForm):

    class Meta:
        model =Foods
        fields='__all__'

class Bill_Items_Form(ModelForm):

    class Meta:
        model=Bill_Items
        fields='__all__' #['Name','Price','Quantity']