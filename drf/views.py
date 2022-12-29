from django.shortcuts import render
from rest_framework import viewsets
from drf.models import Student
from drf.serializers import StudentSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly


# Create your views here.
class StudentModelViewSet(viewsets.ModelViewSet):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer
  authentication_classes = [TokenAuthentication]
  permission_classes = [IsAuthenticated]
  #permission_classes = [IsAuthenticatedOrReadOnly]

