from datetime import datetime

from django.shortcuts import render
from .models import Menu
from .forms import MenuForm


def createMenu(request):
    if request.method == 'GET':
        form = MenuForm()
    else:
        form = MenuForm(request.POST)
        form.date = datetime.now()
        if form.is_valid():
            form.save()

            print('Save')

    return render(request, 'create_menu.html', {'form': form})
