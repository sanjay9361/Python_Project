from rest_framework .serializers import *
from .models import *

class Create_form(ModelSerializer):
    class Meta:
        model=Create
        fields='__all__'

class Types_form(ModelSerializer):
    class Meta:
        model=Types
        fields='__all__'