from django.shortcuts import render
from .serializers import todoSerializer
from .models import todo
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password,check_password
from rest_framework import generics
from django.http import HttpResponse
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
# Create your views here.
# def show(request):
#     return HttpResponse("welcome to my channel gyan for all")




@cache_page(60)  # Cache the view for 60 seconds
def my_view(request):
    # Your view code here
    return HttpResponse('Hello, world!')





class todoViews(generics.GenericAPIView):
    @method_decorator(cache_page(5))
    def get(self,request):
        var = todo.objects.all()
        serializers = todoSerializer(var, many = True)
        return Response(serializers.data)
    
   
    def update(self,request,id): #update
        serializers = todoSerializer(data=request.data)
        if serializers.is_valid():
            todo.objects.filter(id = id ).update(name= serializers.data['name'],phone = serializers.data['phone'],address = serializers.data['address'],subject = serializers.data['subject'])
            return Response (serializers.data)
        else:
            return Response(serializers.error_messages)
        
    def delete(self,request,id):
        var = todo.objects.get(id = id )
        var.delete()
        return Response("the object is deleted")
    
    def put(self,request,id):
        obj = todo.objects.get(id = id)
        serializers = todoSerializer(obj,data=request.data,partial = True)
        if serializers.is_valid():
            todo.objects.update(name= serializers.data['name'],phone = serializers.data['phone'],address = serializers.data['address'],subject = serializers.data['subject'])
            return Response(serializers.data)
        else:
            return Response (serializers.error_messages)
        

class post_dataView(generics.GenericAPIView):

    @method_decorator(cache_page(60 * 15))  # Cache the response for 15 minutes (adjust the duration as needed)
    def post(self, request):
        serializers = todoSerializer(data=request.data)
        if serializers.is_valid():
            todo.objects.create(name=serializers.data['name'], phone=serializers.data['phone'], address=serializers.data['address'], subject=serializers.data['subject'])
            return Response(serializers.data)
        else:
            return Response(serializers.error_messages)