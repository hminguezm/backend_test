from datetime import datetime

from django.shortcuts import render, redirect
from .models import Menu
from .forms import MenuForm


def listMenus(request):
    template_name = 'list_menus.html'
    menus_with_lunches = []
    menus = Menu.objects.all()

    for menu in menus:
        lunches = []
        lunches_by_menu = Menu.objects.get(id=menu.id).lunches.all()

        for lunch in lunches_by_menu:
            lunches.append(lunch.name)

        menus_with_lunches.append({
            'menu_id': str(menu.id),
            'lunches': ' - '.join(lunches),
            'published_at': str(menu.published_at),
            'created_at': str(menu.create_at),
        })

    context = {'menus': menus_with_lunches}

    return render(request, template_name, context)


def createMenu(request):
    template_name = 'create_menu.html'
    if request.method == 'GET':
        form = MenuForm()
    else:
        form = MenuForm(request.POST)
        form.date = datetime.now()
        if form.is_valid():
            form.save()

        return redirect('index')

    return render(request, template_name, {'form': form})


def editMenu(request, menu_id):
    template_name = 'create_menu.html'
    menu = Menu.objects.get(id=menu_id)
    if request.method == 'GET':
        form = MenuForm(instance=menu)
        context = {
            'form': form
        }
    else:
        form = MenuForm(request.POST, instance=menu)
        if form.is_valid():
            form.save()
        context = {
            'form': form
        }
        return redirect('index')

    return render(request, template_name, context)
