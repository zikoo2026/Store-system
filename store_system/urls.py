from django.urls import path
from . import views

app_name = 'store_system'

urlpatterns = [
    path('inventory/', views.index, name='index'),
    path('categories/', views.categories, name='categories'),
    path('warehouses/', views.warehouses, name='warehouses'),
    path('items/', views.items, name='items'),
]