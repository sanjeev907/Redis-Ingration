from rest_framework import serializers
from .models import todo

class todoSerializer(serializers.Serializer):
    name = serializers.CharField(required = True , error_messages = {'name':'name is required'})
    phone = serializers.IntegerField(required = True , error_messages = {'phone':'phone is required'})
    address = serializers.CharField(required = True , error_messages = {'address':'address is required'})
    subject = serializers.CharField(required = True , error_messages = {'subject':'subject is required'})