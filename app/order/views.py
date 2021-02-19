from django.shortcuts import render

from app.order.forms import OrderForm
from app.order.models import Order


def listOrders(request):
    template_name = 'list_order.html'
    orders = Order.objects.all()
    context = {'orders': orders}

    return render(request, template_name, context)


def createOrder(request, menu_id):
    template_name = 'create_order.html'

    if request.method == 'GET':
        form = OrderForm(menu_id=menu_id)
    else:
        form = OrderForm(request.POST, menu_id=menu_id)
        print(form)
        if form.is_valid():
            form.save()

    return render(request, template_name, {'form': form})
