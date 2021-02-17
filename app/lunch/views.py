from datetime import datetime

from django.shortcuts import render
from .models import Lunch
from .forms import LunchForm


def createLunch(request):
    template_name = 'create_menu.html'
    if request.method == 'GET':
        form = LunchForm()
    else:
        form = LunchForm(request.POST)

        if form.is_valid():
            form.save()
            print('Saved')

    return render(request, template_name, {'form': form})


def ListLunches(request):
    template_name = 'list_lunches.html'
    lunches = Lunch.objects.all()

    return render(request, template_name, {'lunches': lunches})
