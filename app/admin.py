from django.contrib import admin
from app import models

# Register your models here.

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'code',
        'name',
        'quantity',
    )
    ordering = ('-id',)
    search_fields = ('code', 'name',)
    list_per_page = 10
    list_max_show_all = 500
    list_editable = ('quantity',)
    list_display_links = ('id', 'code',)

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'category_name',
    )
    ordering = ('-id',)
    search_fields = ('category_name',)
    list_per_page = 10
    list_max_show_all = 500
    list_display_links = ('id', 'category_name',)

@admin.register(models.Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'supplier_code',
        'supplier_name',
    )
    ordering = ('-id',)
    search_fields = ( 'suppier_code','supplier_name',)
    list_per_page = 10
    list_max_show_all = 500
    list_display_links = ('id',)