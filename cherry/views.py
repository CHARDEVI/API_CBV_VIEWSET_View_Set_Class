from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ViewSet
from cherry.models import *
from cherry.serializers import *
from rest_framework.response import Response



class ProductCRUD_VS(ViewSet):
    def list(self,request):
        PQS=Product.objects.all()
        PSD=ProductSerializer(PQS,many=True)
        return Response(PSD.data)
    def create(self,request):
        SD=ProductSerializer(data=request.data)
        if SD.is_valid():
            SD.save()
            return Response ({'success':'Product is Created'})
        else:
            return Response ({'Failed':'Product is not Created'})
        
    def retrieve(self,request,pk):
        SPO=Product.objects.get(pk=pk)
        SPD=ProductSerializer(SPO)
        return Response(SPD.data)
    
    def update(self,request,pk):
        SPO=Product.objects.get(pk=pk)
        SPD=ProductSerializer(SPO,data=request.data)
        if SPD.is_valid():
            SPD.save()
            return Response({'Updated':'Product is Updated'})
        else:
            return Response({'Failed':'Product is Not Updated'})


    def partial_update(self,request,pk):
        SPO=Product.objects.get(pk=pk)
        SPD=ProductSerializer(SPO,data=request.data,partial=True)
        if SPD.is_valid():
            SPD.save()
            return Response({'Updated':'Product is Partially Updated'})
        else:
            return Response({'Failed':'Product is Not Partially Updated'})
        

    def destroy(self,request,pk):
        Product.objects.get(pk=pk).delete()
        return Response({'Deleted':'Product is Deleted'})
                
    