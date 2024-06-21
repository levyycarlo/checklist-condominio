from django.shortcuts import render, redirect
from django.http import HttpResponse

# Importar views necessárias da aplicação accounts
from accounts.views import CadastroSindicoForm

def home(request):
    # Renderiza a página inicial

    return render(request, 'home.html')

def sobre(request):
    #Renderiza a página 'Sobre'

    return render(request, 'sobre.html')

def login_sindico(request):
    #Renderiza a página de login do síndico.

    return render(request, 'telaLogin_sindico.html')

def cadastro_sindico(request):
    #Renderiza a página de registro de síndico.

    return render(request, 'cadastroSindico.html')

#def register_sindico(request):
    if request.method == 'POST':
        form = CadastroSindicoForm(request.POST)
        if form.is_valid():
            form.save()  # Isso cria e salva o usuário automaticamente
            return redirect('frontend:login_sindico')  # Redireciona para a página de login no frontend
    else:
        form = CadastroSindicoForm()
    return render(request, 'cadastroSindico.html', {'form': form})

def recover_password(request):
    #Renderiza a página de recuperação de senha.
    
    return render(request, 'alterar.html')
