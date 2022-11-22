from django.contrib import admin
from .models import *


class ItemAdmin(admin.ModelAdmin):
    """Админка пунктов"""
    list_display = ('name', 'price')
    fields = ('name', 'description', 'price', 'order', 'currency')


class OrdersAdmin(admin.ModelAdmin):
    """Админка заказов"""
    list_display = ('name',)
    fields = ('name', 'currency')


admin.site.register(Item, ItemAdmin)
admin.site.register(Orders, OrdersAdmin)
