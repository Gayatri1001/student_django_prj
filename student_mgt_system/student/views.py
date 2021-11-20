from django.db.models.query import QuerySet
from django.http import response
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status
from.models import student
from student.serializers import Studentserializers
# Create your views here.

class StudentData(APIView):

    def get(self,request):
        student1=student.objects.all()
        serializer=Studentserializers(student1,many=True)
        return Response(serializer.data)

    def post(self):
        pass

