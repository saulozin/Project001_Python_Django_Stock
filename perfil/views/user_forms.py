from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.contrib.auth.forms import AuthenticationForm
from perfil.forms import RegisterForm, RegisterUpdateForm
from django.contrib.auth.decorators import login_required

def index(request):

    return render(
        request,
        'perfil/index.html',
    )

def login_view(request):
    form = AuthenticationForm(request)

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            messages.success(request, 'Usuário logado com sucesso!')
            return redirect('app:stock')
        
        messages.error(request, 'Usuário ou senha incorretos!')

    context = {
        'form': form
    }

    return render(
        request,
        'perfil/login.html',
        context,
    )

def createPerfil(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Usuário registrado com sucesso!')
            return redirect('perfil:login')
    

    context = {
        'form': form, 
    }

    return render(
        request,
        'perfil/register.html',
        context,
    )

@login_required(login_url='perfil:login')
def updatePerfil(request):
    form = RegisterUpdateForm(instance=request.user)

    if request.method == 'POST':
        form = RegisterUpdateForm(data=request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            messages.success(request, 'Usuário atualizado com sucesso!')
            return redirect('perfil:login')

    context = {
        'form': form,
    }

    return render(
        request,
        'perfil/update_perfil.html',
        context,
    )

@login_required(login_url='perfil:login')
def logOut_view(request):
    auth.logout(request)
    return redirect('perfil:login')