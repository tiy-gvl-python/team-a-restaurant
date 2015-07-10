from django.contrib import admin

# Register your models here.

from .models import Order, Item, Category, Menu

admin.site.register(Item)
admin.site.register(Order)
admin.site.register(Category)
admin.site.register(Menu)

