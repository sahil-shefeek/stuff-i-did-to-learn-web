from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse("Hello world!")

def greetUser(request, name):
    return HttpResponse(f"Hello, {name.capitalize()}")