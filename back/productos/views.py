from django.shortcuts import render
#======================= MODELOS ===============================
from productos.models import productos
#======================= Serializers =================================
from productos.serializers import productosSerializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

# Create your views here.
class productosOne(APIView):
    def get(self, request,*args, **kwargs):
        pk = kwargs.get('pk')
        print(pk) 
        queryset= productos.objects.get(pk=pk)
        serializer = productosSerializers(queryset)
        return Response(serializer.data)

class productosList(APIView):
    def get(self, request, format=None):
        queryset= productos.objects.all()
        serializer = productosSerializers(queryset,many=True)
        return Response(serializer.data)
    
    def post (self, request, format=None):
        serializer = productosSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            response = datas
            return Response (response, status=status.HTTP_201_CREATED)
        response = serializer.errors
        return Response (response, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        queryset = productos.objects.get(pk=pk)
        serializer = productosSerializers(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request,*args, **kwargs):
        pk = kwargs.get('pk')
        print(pk) 
        queryset= productos.objects.get(pk=pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)