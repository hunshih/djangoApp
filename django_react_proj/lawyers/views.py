from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Lawyer
from .serializers import *

# Create your views here.
# more like a request handler. Take request, spit response

def calc():
    x = 1
    y = 2
    return x

def say_hello(request):
    x = calc()
    return HttpResponse('Hellow World')

@api_view(['GET', 'POST'])
def lawyers_list(request):
    if request.method == 'GET':
        data = Lawyer.objects.all()

        serializer = LawyerSerializer(data, context={'request': request}, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = LawyerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'DELETE'])
def lawyers_detail(request, pk):
    try:
        lawyer = Lawyer.objects.get(pk=pk)
    except Lawyer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = LawyerSerializer(lawyer, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        lawyer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)