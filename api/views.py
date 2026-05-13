from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from .models import Student
from .serializers import StudentSerializers
from rest_framework.decorators import api_view

@api_view(["GET","POST"])
def StudentView(request):
    if request.method == "GET":
        data = Student.objects.all()
        serializer = StudentSerializers(data , many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method == "POST":
        serializer = StudentSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    
