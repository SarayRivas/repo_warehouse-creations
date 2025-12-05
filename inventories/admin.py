from django.contrib import admin
from . models import  Product, Warehouse, Shelve, WarehouseCreation, Inventory

admin.site.register(Inventory)
admin.site.register(Product)
admin.site.register(Warehouse)
admin.site.register(Shelve)
admin.site.register(WarehouseCreation)
