from django.contrib import admin
from django.urls import path

from app.lunch.views import createLunch
from app.menu.views import createMenu, listMenus, editMenu

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create_menu/', createMenu, name='create_menu'),
    path('create_lunch/', createLunch, name='create_lunch'),
    path('list_menus/', listMenus, name='list_menus'),
    path('edit_menu/<str:menu_id>/', editMenu, name='edit_menu'),
]
