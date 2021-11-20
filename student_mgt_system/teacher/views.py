from django.shortcuts import render
from django.db.models.query import QuerySet
from django.http import response
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status
from.models import teacher
from teacher.serializers import Teacherserializers

# Create your views here.


class TeacherData(APIView):

    def get(self, request):
        teacher1=teacher.objects.all()
        serializer=Teacherserializers(teacher1,many=True)
        return Response(serializer.data)

    def post(self):
        pass