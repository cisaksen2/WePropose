from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def indexPageView(request):
    return HttpResponse("Home Page- general information and welcome to")

def datePageView(request):
    return HttpResponse("Date Page- all functions and work will be done here")

def contactPageView(request):
    return HttpResponse("Contact Page- contact info and humor")