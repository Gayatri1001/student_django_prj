
from rest_framework import serializers
from .models import  student

class Studentserializers(serializers.ModelSerializer):

    class Meta:
        model = student
        fields = ('first_name', 'last_name', 'mobile_no', 'address', 'standard')

