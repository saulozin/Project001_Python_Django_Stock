from django.shortcuts import render, redirect, get_object_or_404
from app.forms import StockForm
from django.urls import reverse
from app.models import Product
from django.contrib.auth.decorators import login_required

@login_required(login_url='perfil:login')
def registerProduct(request):
    form_action = reverse('app:register-product')

    if request.method == 'POST':

        form = StockForm(request.POST, request.FILES)

        if form.is_valid():
            #print('Form é válido')
            product = form.save()
            return redirect('app:update-product', product_code=product.code)
        
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
def updateProduct(request, product_code):
    product = get_object_or_404(Product, code=product_code)
    form_action = reverse('app:update-product', args=(product_code,))

    if request.method == 'POST':

        form = StockForm(request.POST, request.FILES, instance=product)

        if form.is_valid():
            #print('Form é válido')
            product = form.save()
            return redirect('app:update-product', product_code=product.code)
        
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
def removeProduct(request, product_code):
    product = get_object_or_404(Product, code=product_code)

    confirmation = request.POST.get('confirmation', 'no')

    if confirmation == 'yes':
        product.delete()
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