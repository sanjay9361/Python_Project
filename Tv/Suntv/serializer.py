from rest_framework .serializers import*
from .models import*

class Fund_form(ModelSerializer):
    class Meta:
        model=Fund
        fields='__all__'


class Coopen_form(ModelSerializer):
    class Meta:
        model=Coopen
        fields='__all__'