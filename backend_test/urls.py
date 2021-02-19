from django.contrib import admin
from django.urls import path

from app.employee.views import createEmployee
from app.lunch.views import createLunch
from app.menu.views import createMenu, listMenus, editMenu
from app.order.views import createOrder, listOrders

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', listMenus, name='index'),
    path('create_menu/', createMenu, name='create_menu'),
    path('create_lunch/', createLunch, name='create_lunch'),
    path('list_menus/', listMenus, name='list_menus'),
    path('edit_menu/<str:menu_id>/', editMenu, name='edit_menu'),
    path('create_employee/', createEmployee, name='create_employee'),
    path('nora.cornershop.io/menu/<str:menu_id>', createOrder, name='create_order'),
    path('list_order/', listOrders, name='list_order'),
]
