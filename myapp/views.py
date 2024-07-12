# from django.shortcuts import render
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from rest_framework.authtoken.models import Token
# from .models import custumers
# from .serializers import CustumerSerializer
# from django.shortcuts import render
from django.contrib.auth import authenticate
from django.http import HttpResponse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from .models import custumers
from .serializers import CustumerSerializer
from django.shortcuts import render
from rest_framework.decorators import api_view
# Create your views here.
@api_view(['POST'])
def register(request):
    if request.method=='POST':
        serializer=CustumerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'saved successfully','data':serializer.data})
        
@api_view(['GET'])
def display(request):
# def display(request,id):
    if request.method=='GET':
        data=custumers.objects.all()
        # data=custumers.objects.get(email="email")
        # data=custumers.objects.get(password="password")
        
        serializer=CustumerSerializer(data,many=True,context={'request':request})
        return Response(serializer.data)
    
# @api_view(['GET'])
#     def displays(request):
# def display(request,id):
#     try:
    
@api_view(['DELETE'])
def delete(request,id):
    try:
        instance=custumers.objects.get(id=id)
    except custumers.DoesNotExist:
        return Response({"error":"Not Found"},status=status.HTTP_404_NOT_FOUND)
    if request.method=="DELETE":
        instance.delete()
        return Response({"data":"deleted"})
    
@api_view(['PUT'])
def update(request,id):
    try:
        instance=custumers.objects.get(id=id)
    except custumers.DoesNotExist:
        return Response({"error":"Not Found"},status=status.HTTP_404_NOT_FOUND)
    if request.method=="PUT":
        serializer=CustumerSerializer(instance,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
