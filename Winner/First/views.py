from rest_framework import viewsets
from rest_framework.response import Response
from . models import *
from .serializers import *




class FoodProducts(viewsets.ModelViewSet):
#     def get(self,request):
#         values=Create.objects.all()
#         json_format=Create_form(values,  many=True)
#         return Response(json_format.data)

  queryset=Create.objects.all()
  serializer_class=Create_form 


class TypeProducts(viewsets.ModelViewSet):
  queryset=Types.objects.all()
  serializer_class=Types_form


    
#     def post(self,request):
#         json_data=Create_form(data=request.data)
#         if json_data. is_valid():
#             json_data.save()
#         return Response("Data Saved Sanjay")
    
# class CreateProducts(viewsets.ModelViewSet):
#     def delete(self,request,id):
#         deleteProduct=Create.objects.get(id=id)
#         deleteProduct.delete()
#         return Response("Deleted Sucessfully")
    

#     def patch(self,request,id):
#         json_data=Create_form(data=Create.objects.filter(id=id))
#         print(request.data)
#         if json_data.is_valid():
#             json_data.update()
#         return Response("UpDated Sucessfully")


