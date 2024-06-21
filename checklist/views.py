from django.shortcuts import render, redirect
from .forms import ChecklistForm
from django.contrib import messages

def auth_checklist(request):
    if request.method == 'POST':
        form = ChecklistForm(request.POST, request.FILES)
        if form.is_valid():
            # Processar os dados do formulário, se necessário
            # Aqui você pode adicionar lógica adicional, como salvar os dados no banco de dados
            form.save()
            # Adiciona uma mensagem de sucesso
            messages.success(request, 'Checklist registrado com sucesso!')
            # Redireciona para a página do dashboard
            return redirect('home_dashboard')
        else:
            # Adiciona uma mensagem de erro caso o formulário não seja válido
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = ChecklistForm()

    return render(request, 'register_checklist.html', {'form': form})

# As funções register_checklist e home_dashboard permanecem iguais
def register_checklist(request):
    form = ChecklistForm()
    return render(request, 'register_checklist.html', {'form': form})

def home_dashboard(request):

    return render(request, 'dashboard.html')
