from django.shortcuts import render, redirect, get_object_or_404


# Create your views here.
def BASE(request):
    return render(request, 'base.html')

def home(request):
    return render(request, 'home.html')

