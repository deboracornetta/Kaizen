from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
#message.debug / info / success/ warning/ error

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'{username} registrado com sucesso!')
            return redirect('site-home')
    else:
        form = UserRegisterForm
    form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

