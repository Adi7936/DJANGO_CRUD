from rest_framework import serializers
from .models import *




#student serilizers
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'



#Section serializers
class SectionSerializer(serializers.ModelSerializer):
    students = StudentSerializer(many=True, read_only=True)

    class Meta:
        model = Section
        fields = '__all__'
