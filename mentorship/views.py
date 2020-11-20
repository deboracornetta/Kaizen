from django.shortcuts import render
from .models import Student


def home(request):
    return render(request, 'mentorship/home.html')

def about(request):

    return render(request, 'mentorship/about.html')