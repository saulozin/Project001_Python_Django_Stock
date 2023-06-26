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

def category(request):
    categories = Category.objects.all().order_by('-id')

    paginator = Paginator(categories, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
    }
    return render(
        request,
        'app/category.html',
        context,
    )

def supplier(request):
    suppliers = Supplier.objects.all().order_by('-id')

    paginator = Paginator(suppliers, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
    }
    return render(
        request,
        'app/supplier.html',
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

    paginator = Paginator(products, 10)
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

def search_category(request):
    search_value = request.GET.get('q', '').strip()

    if search_value == '':
        return redirect('app:category')
    
    categories = Category.objects.filter(
        category_name__icontains=search_value,
    ).order_by('-id')

    paginator = Paginator(categories, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'search_value': search_value,
    }
    return render(
        request,
        'app/category.html',
        context,
    )

def search_supplier(request):
    search_value = request.GET.get('q', '').strip()

    if search_value == '':
        return redirect('app:supplier')
    
    suppliers = Supplier.objects.filter(
        Q(supplier_code__icontains=search_value) |
        Q(supplier_name__icontains=search_value)
    ).order_by('-id')

    paginator = Paginator(suppliers, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'search_value': search_value,
    }
    return render(
        request,
        'app/supplier.html',
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
        'app/category-detail.html',
        context,
    )

def supplierDetail(request, supplier_code):
    supplier_detail = get_object_or_404(Supplier, supplier_code=supplier_code)

    context = {
        'supplier': supplier_detail,
    }
    return render(
        request,
        'app/supplier-detail.html',
        context,
    )
