from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import SubscribeForms
from .models import Subscribe


def subscribe(request):
    registered = Subscribe.objects.all()

    if request.method == 'POST':
        form = SubscribeForms(request.POST)

        if form.is_valid:
            subscribe = Subscribe(email=request.POST['email'])

            if Subscribe.objects.filter(email=subscribe):
                return HttpResponseRedirect(reverse('subscribe:error'))

            else:
                subscribe.save()
                return HttpResponseRedirect(reverse('subscribe:success'))

    else:
        form = SubscribeForms()

    return render(request, 'subscribe/subscribe.html', {'form': form})


def success(request):

    return render(request, 'subscribe/success.html')


def error(request):
    
    return render(request, 'subscribe/error.html')


def unsubscribe(request):
    pass