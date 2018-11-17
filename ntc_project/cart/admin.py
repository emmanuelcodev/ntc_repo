from django.contrib import admin
from .models import CartItems
# Register your models here.


class CartItemsManager(admin.ModelAdmin):
    list_display = ['id']
admin.site.register(CartItems, CartItemsManager)
