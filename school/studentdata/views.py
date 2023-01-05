from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from studentdata.models import *
from rest_framework import generics
from studentdata.serializers import *

# Create your views here. 
class ClassApiView(generics.ListCreateAPIView):
    queryset= classdetails.objects.all()
    serializer_class= ClassSerializer

class ClassDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset= classdetails
    serializer_class= ClassSerializer



class StudentApiView(generics.ListCreateAPIView):
    queryset= student.objects.all()
    serializer_class= StudentSerializer

class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset= student
    serializer_class= StudentSerializer

class StudentDetailByClass(APIView):
    def get(self, request):
        allStudents=student.objects.all().filter(stdclass=request.query_params['classid']).values()
        return Response({"Message":"List of Students","Students List":allStudents})
    

