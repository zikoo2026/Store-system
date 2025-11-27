from django.shortcuts import render
from .models import Category, Warehouse, Item

# Create your views here.

def index(request):
    """الصفحة الرئيسية"""
    context = {
        'categories_count': Category.objects.count(),
        'warehouses_count': Warehouse.objects.count(),
        'items_count': Item.objects.count(),
    }
    return render(request, 'store_system/index.html', context)

def categories(request):
    """عرض جميع التصنيفات"""
    categories_list = Category.objects.all()
    context = {'categories': categories_list}
    return render(request, 'store_system/categories.html', context)

def warehouses(request):
    """عرض جميع المستودعات"""
    warehouses_list = Warehouse.objects.all()
    context = {'warehouses': warehouses_list}
    return render(request, 'store_system/warehouses.html', context)

def items(request):
    """عرض جميع المواد"""
    items_list = Item.objects.select_related('category').all()
    categories_count = Category.objects.count()
    context = {
        'items': items_list,
        'categories_count': categories_count
    }
    return render(request, 'store_system/items.html', context)
