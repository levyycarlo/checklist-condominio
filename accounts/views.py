from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CadastroSindicoForm, SindicoLoginForm


def sindico_login(request):
    if request.method == 'POST':
        form = SindicoLoginForm(request.POST, request=request)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login realizado com sucesso!')
                return redirect('home_dashboard')  # Certifique-se de que 'interfaceSindico' está correto
            else:
                messages.error(request, 'Email ou senha incorretos. Por favor, tente novamente.')
        else:
            messages.error(request, 'Email ou senha incorretos. Por favor, tente novamente.')
    else:
        form = SindicoLoginForm(request=request)
    return render(request, 'telaLogin_sindico.html', {'form': form})



def register_sindico(request):
    if request.method == 'POST':
        form = CadastroSindicoForm(request.POST, request=request)
        if form.is_valid():
            user = form.save()
            user = authenticate(request, username=user.email, password=request.POST['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'Cadastro realizado com sucesso!')
                return redirect('home_dashboard')
        messages.error(request, 'Por favor, corrija os erros abaixo.')
    else:
        form = CadastroSindicoForm(request=request)
    return render(request, 'cadastroSindico.html', {'form': form})
