from django.shortcuts import render
from django.views.generic import View

# Create your views here.

def landingView(request):
    return render(request,'home/landing.html')