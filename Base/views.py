from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'home.html')

def historicalData(request):
    return render(request,'historicalData.html')

def contact(request):
    return render (request,"contact.html")

def alert(request):
    return render(request,"alerts.html")

def about(request):
    return render(request,"aboutUs.html")