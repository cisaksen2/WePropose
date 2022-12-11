from django.shortcuts import render
from django.http import HttpResponse
from datebuilder.models import DateType

# Create your views here.
def showdatesPageView(request):
    return render(request, 'datebuilder/showDates.html')

def showfirstdatePageView(request):
    data = DateType.objects.filter(date_activity=1)

    context = {
        "dates" : data
    }
    return render(request, 'datebuilder/firstDateDate.html', context)

def showcasualPageView(request):
    data = DateType.objects.filter(date_activity=2)

    context = {
        "dates" : data
    }
    return render(request, 'datebuilder/casualDate.html', context)

def showoutdoorsPageView(request):
    data = DateType.objects.filter(date_activity=3)

    context = {
        "dates" : data
    }
    return render(request, 'datebuilder/outdoorsDate.html', context)

def showfancyPageView(request):
    data = DateType.objects.filter(date_activity=4)

    context = {
        "dates" : data
    }
    return render(request, 'datebuilder/fancyDate.html', context)

def showspiritualPageView(request):
    data = DateType.objects.filter(date_activity=5)

    context = {
        "dates" : data
    }
    return render(request, 'datebuilder/spiritualDate.html', context)

def showproposalPageView(request):
    data = DateType.objects.filter(date_activity=6)

    context = {
        "dates" : data
    }
    return render(request, 'datebuilder/proposalDate.html', context)

def showuserPageView(request):
    data = DateType.objects.filter(date_activity__isnull=True)

    context = {
        "dates" : data
    }
    return render(request, 'datebuilder/userDates.html', context)

def addDatePageView(request) :

    if request.method == 'POST' :
        date = DateType()

        date.title = request.POST['title']
        date.hours = request.POST['hours']
        date.cost = request.POST['cost']
        date.activity_date = request.POST['date']

        date.save()

        return showuserPageView(request)
    else :
        return render(request, 'datebuilder/addDate.html')

def showSingleDatePageView(request, date_id) :
    data = DateType.objects.get(id = date_id)

    context = {
        'record' : data, 
    }

    return render(request, 'datebuilder/editDate.html', context)

def editDatePageView(request) :
    if request.method == 'POST' :
        date_id = request.POST['date_id']

        date = DateType.objects.get(id=date_id)

        date.title = request.POST['title']
        date.hours = request.POST['hours']
        date.cost = request.POST['cost']
        date.activity_date = request.POST['date']

        date.save()
    
    return showdatesPageView(request)

def deleteDatePageView(request, date_id) :
    data = DateType.objects.get(id=date_id)

    data.delete()

    return showdatesPageView(request)
