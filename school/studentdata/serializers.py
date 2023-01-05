from rest_framework import serializers
from .models import *

class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = classdetails
        fields= '__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = student
        fields= '__all__'
