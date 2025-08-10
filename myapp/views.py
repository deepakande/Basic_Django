from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello World")

def greet(request):
    return HttpResponse("Hello World Deepa,welcome to Django!")
