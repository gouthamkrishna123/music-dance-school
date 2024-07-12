from rest_framework import serializers
from .models import custumers
from django.contrib.auth.models import User
 
class CustumerSerializer(serializers.ModelSerializer):
    class Meta:
        model=custumers
        fields='__all__'