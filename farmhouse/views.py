from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'main.html')


def address(request):
    return render(request,'address.html')


def contactus(request):
    return render(request,'contactus.html')


def room(request):
    return render(request,'room.html')


def boating(request):
    return render(request,'boating.html')