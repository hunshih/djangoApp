from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# more like a request handler. Take request, spit response

def calc():
    x = 1
    y = 2
    return x

def say_hello(request):
    x = calc()
    return HttpResponse('Hellow World')
