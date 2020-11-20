from django.shortcuts import render


def home(request):
    return render(request, 'mentorship/home.html')

def about(request):
    
    return render(request, 'mentorship/about.html')