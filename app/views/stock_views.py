from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from app.models import Product, Category, Supplier
from django.core.paginator import Paginator

def stock(request):
    products = Product.objects.all().order_by('-id')

    paginator = Paginator(products, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
    }
    return render(
        request,
        'app/stock.html',
        context,
    )

def search(request):
    search_value = request.GET.get('q', '').strip()

    if search_value == '':
        return redirect('app:stock')

    products = Product.objects.filter(
        Q(name__icontains=search_value) | 
        Q(code__icontains=search_value) |
        Q(serial_number__icontains=search_value)
    ).order_by('-id')

    paginator = Paginator(products, 6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'search_value': search_value,
    }
    return render(
        request,
        'app/stock.html',
        context,
    )

def productDetail(request, product_code):
    product_detail = get_object_or_404(Product, code=product_code)

    context = {
        'product': product_detail
    }
    return render(
        request,
        'app/product.html',
        context,
    )

def categoryDetail(request, category_name):
    category_detail = get_object_or_404(Category, category_name=category_name)

    context = {
        'category': category_detail,
    }
    return render(
        request,
        'app/category.html',
        context,
    )

def supplierDetail(request, supplier_name):
    supplier_detail = get_object_or_404(Supplier, supplier_name=supplier_name)

    context = {
        'supplier': supplier_detail,
    }
    return render(
        request,
        'app/supplier.html',
        context,
    )
