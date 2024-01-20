from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Section, Student
from .serializers import *



class SectionListCreateView(generics.ListCreateAPIView):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer

class SectionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer

class StudentListCreateView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer