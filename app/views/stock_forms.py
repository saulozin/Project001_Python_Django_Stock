from django.shortcuts import render, redirect, get_object_or_404
from app.forms import StockForm, CategoryForm, SupplierForm
from django.urls import reverse
from app.models import Product, Category, Supplier
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required(login_url='perfil:login')
def registerProduct(request):
    form_action = reverse('app:register-product')

    if request.method == 'POST':

        form = StockForm(request.POST, request.FILES)

        if form.is_valid():
            product = form.save(commit=False)
            product.owner = request.user
            product.save()
            messages.success(request, 'Produto cadastrado com sucesso!')
            return redirect('app:product-detail', product_code=product.code)
        
        messages.error(request, 'Não foi possível cadastrar o produto!')
        
        context = {
            'form': form,
            'form_action': form_action,
        }

        return render(
            request,
            'app/register_product.html',
            context,
        )

    context = {
        'form': StockForm(),
        'form_action': form_action,
    }

    return render(
        request,
        'app/register_product.html',
        context,
    )

@login_required(login_url='perfil:login')
def registerCategory(request):
    form_action_category = reverse('app:register-category')

    if request.method == 'POST':

        form_category = CategoryForm(request.POST, request.FILES)

        if form_category.is_valid():
            category = form_category.save(commit=False)
            category.owner = request.user
            category.save()
            messages.success(request, 'Categoria cadastrada com sucesso!')
            return redirect('app:category-detail', category_name=category.category_name)
        
        messages.error(request, 'Não foi possível cadastrar a categoria!')
        
        context = {
            'form': form_category,
            'form_action': form_action_category,
        }

        return render(
            request,
            'app/register_category.html',
            context,
        )

    context = {
        'form': CategoryForm(),
        'form_action': form_action_category,
    }

    return render(
        request,
        'app/register_category.html',
        context,
    )

@login_required(login_url='perfil:login')
def registerSupplier(request):
    form_action_supplier = reverse('app:register-supplier')

    if request.method == 'POST':

        form = SupplierForm(request.POST, request.FILES)

        if form.is_valid():
            supplier = form.save(commit=False)
            supplier.owner = request.user
            supplier.save()
            messages.success(request, 'Fornecedor cadastrado com sucesso!')
            return redirect('app:supplier-detail', supplier_code=supplier.supplier_code)
        
        messages.error(request, 'Não foi possível cadastrar o fornecedor!')
        
        context = {
            'form': form,
            'form_action': form_action_supplier,
        }

        return render(
            request,
            'app/register_supplier.html',
            context,
        )

    context = {
        'form': SupplierForm(),
        'form_action': form_action_supplier,
    }

    return render(
        request,
        'app/register_supplier.html',
        context,
    )

@login_required(login_url='perfil:login')
def updateProduct(request, product_code):
    product = get_object_or_404(Product, code=product_code, owner=request.user)
    form_action = reverse('app:update-product', args=(product_code,))

    if request.method == 'POST':

        form = StockForm(request.POST, request.FILES, instance=product)

        if form.is_valid():
            product = form.save()
            messages.success(request, 'Produto atualizado com sucesso!')
            return redirect('app:update-product', product_code=product.code)
        
        messages.error(request, 'Não foi possível atualizar o produto!')
        
        context = {
            'form': form,
            'form_action': form_action,
        }

        return render(
            request,
            'app/register_product.html',
            context,
        )

    context = {
        'form': StockForm(),
        'form': StockForm(instance=product),
        'form_action': form_action,
    }

    return render(
        request,
        'app/register_product.html',
        context,
    )

@login_required(login_url='perfil:login')
def updateCategory(request, category_name):
    category = get_object_or_404(Category, category_name=category_name, owner=request.user)
    form_action = reverse('app:update-category', args=(category_name,))

    if request.method == 'POST':

        form = CategoryForm(request.POST, request.FILES, instance=category)

        if form.is_valid():
            category = form.save()
            messages.success(request, 'Categoria atualizada com sucesso!')
            return redirect('app:update-category', category_name=category.category_name)
        
        messages.error(request, 'Não foi possível atualizar a categoria!')
        
        context = {
            'form': form,
            'form_action': form_action,
        }

        return render(
            request,
            'app/register_category.html',
            context,
        )

    context = {
        'form': CategoryForm(),
        'form': CategoryForm(instance=category),
        'form_action': form_action,
    }

    return render(
        request,
        'app/register_category.html',
        context,
    )

@login_required(login_url='perfil:login')
def updateSupplier(request, supplier_code):
    supplier = get_object_or_404(Supplier, supplier_code=supplier_code, owner=request.user)
    form_action = reverse('app:update-supplier', args=(supplier_code,))

    if request.method == 'POST':

        form = SupplierForm(request.POST, request.FILES, instance=supplier)

        if form.is_valid():
            supplier = form.save()
            messages.success(request, 'Fornecedor atualizado com sucesso!')
            return redirect('app:update-supplier', supplier_code=supplier.supplier_code)
        
        messages.error(request, 'Não foi possível atualizar o fornecedor!')
        
        context = {
            'form': form,
            'form_action': form_action,
        }

        return render(
            request,
            'app/register_supplier.html',
            context,
        )

    context = {
        'form': SupplierForm(),
        'form': SupplierForm(instance=supplier),
        'form_action': form_action,
    }

    return render(
        request,
        'app/register_supplier.html',
        context,
    )

@login_required(login_url='perfil:login')
def removeProduct(request, product_code):
    product = get_object_or_404(Product, code=product_code, owner=request.user)

    confirmation = request.POST.get('confirmation', 'no')

    if confirmation == 'yes':
        product.delete()
        messages.success(request, 'Produto deletado com sucesso!')
        return redirect('app:stock')

    context = {
        'product': product,
        'confirmation': confirmation,
    }

    return render(
        request,
        'app/product.html',
        context,
    )

@login_required(login_url='perfil:login')
def removeCategory(request, category_name):
    category = get_object_or_404(Category, category_name=category_name, owner=request.user)

    confirmation = request.POST.get('confirmation', 'no')

    if confirmation == 'yes':
        category.delete()
        messages.success(request, 'Categoria deletada com sucesso!')
        return redirect('app:category')

    context = {
        'category': category,
        'confirmation': confirmation,
    }

    return render(
        request,
        'app/category-detail.html',
        context,
    )


@login_required(login_url='perfil:login')
def removeSupplier(request, supplier_code):
    supplier = get_object_or_404(Supplier, supplier_code=supplier_code, owner=request.user)

    confirmation = request.POST.get('confirmation', 'no')

    if confirmation == 'yes':
        supplier.delete()
        messages.success(request, 'Fornecedor deletado com sucesso!')
        return redirect('app:supplier')

    context = {
        'supplier': supplier,
        'confirmation': confirmation,
    }

    return render(
        request,
        'app/supplier-detail.html',
        context,
    )