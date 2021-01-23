from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Rango says hey there partner! Go to <a href='/rango/about/'>About</a>")

def about(request):
    return HttpResponse("This is the 'About' page! Go back to <a href='/rango'>Index</a>")
