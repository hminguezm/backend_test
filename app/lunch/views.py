from django.shortcuts import render, redirect
from .models import Lunch
from .forms import LunchForm


def createLunch(request):
    template_name = 'create_lunch.html'
    if request.method == 'GET':
        form = LunchForm()
    else:
        form = LunchForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('create_menu')

    return render(request, template_name, {'form': form})


def ListLunches(request):
    template_name = 'list_lunches.html'
    lunches = Lunch.objects.all()

    return render(request, template_name, {'lunches': lunches})
