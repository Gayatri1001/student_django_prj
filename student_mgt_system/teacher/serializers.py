from rest_framework import serializers
from .models import teacher 

class Teacherserializers(serializers.ModelSerializer):

    class Meta:
        model = teacher
        fields = ('teacher_first_name', 'teacher_last_name', 'teacher_mobile_no', 'teacher_address','teacher_education', 'teacher_allocated_class')

