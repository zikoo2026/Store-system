from django.db import models

# Create your models here.

class Category(models.Model):
    """جدول التصنيفات"""
    category_id = models.AutoField(primary_key=True, verbose_name="معرف التصنيف")
    category_name = models.CharField(max_length=100, verbose_name="اسم التصنيف")
    
    class Meta:
        verbose_name = "التصنيف"
        verbose_name_plural = "التصنيفات"
    
    def __str__(self):
        return self.category_name


class Warehouse(models.Model):
    """جدول المستودعات"""
    warehouse_id = models.AutoField(primary_key=True, verbose_name="معرف المستودع")
    warehouse_name = models.CharField(max_length=100, verbose_name="اسم المستودع")
    
    class Meta:
        verbose_name = "المستودع"
        verbose_name_plural = "المستودعات"
    
    def __str__(self):
        return self.warehouse_name


class Item(models.Model):
    """جدول المواد"""
    item_id = models.AutoField(primary_key=True, verbose_name="معرف المادة")
    item_name = models.CharField(max_length=100, verbose_name="اسم المادة")
    unit = models.CharField(max_length=50, verbose_name="الوحدة")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="التصنيف")
    
    class Meta:
        verbose_name = "المادة"
        verbose_name_plural = "المواد"
    
    def __str__(self):
        return self.item_name
