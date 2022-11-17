from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def indexPageView(request):
    return render(request, 'datingpages/index.html')



def aboutPageView(request):
    return render(request, 'datingpages/about.html')


def contactPageView(request):
     return render(request, 'datingpages/contact.html')