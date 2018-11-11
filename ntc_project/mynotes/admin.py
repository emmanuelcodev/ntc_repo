from django.contrib import admin
from .models import MyPurchases



# Register your models here.

class MyPurchasesManager(admin.ModelAdmin):
    list_display = ['notes_id','id']

admin.site.register(MyPurchases, MyPurchasesManager)
