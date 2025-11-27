from django.contrib import admin
from .models import Category, Warehouse, Item

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_id', 'category_name']
    search_fields = ['category_name']


@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):
    list_display = ['warehouse_id', 'warehouse_name']
    search_fields = ['warehouse_name']


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['item_id', 'item_name', 'unit', 'category']
    list_filter = ['category']
    search_fields = ['item_name']
