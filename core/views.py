from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


def index(request):

    return render(request, 'core/index.html')


def about(request):

    return render(request, 'core/about.html')


def contact(request):
    
    return render(request, 'core/contact.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('core:index')
    else:
        form = UserCreationForm()

    context = {
        'form': form
    }
    
    return render(request, 'registration/signup.html', context)