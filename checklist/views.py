from django.shortcuts import render, redirect, get_object_or_404
from .forms import ChecklistForm
from .models import Checklist
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
    # Contagem de status pendente
    pendente_cont = Checklist.objects.filter(status='pendente').count()

    # Contagem de status concluído
    concluido_cont = Checklist.objects.filter(status='concluido').count()

    contagem_total = Checklist.objects.count()
    return render(request, 'dashboard.html', {
        'pendente': pendente_cont,
        'concluido': concluido_cont,
        'contagem_total':contagem_total
    })


def auth_update_checklist(request, checklist_id):
    checklist = get_object_or_404(Checklist, id=checklist_id)
    
    if request.method == 'POST':
        status = request.POST.get('status')
        resolucao_ocorrencia = request.POST.get('resolucao_ocorrencia')

        if status and resolucao_ocorrencia:
            # Atualiza os campos do checklist
            checklist.status = status
            checklist.resolucao_ocorrencia = resolucao_ocorrencia
            checklist.save()

            messages.success(request, 'Checklist atualizado com sucesso.')
            return redirect('solicitacoes_totais')  # Redireciona para a lista de solicitações totais
        else:
            if not status:
                messages.warning(request, 'É obrigatório mudar o status.')
            if not resolucao_ocorrencia:
                messages.warning(request, 'É obrigatório responder a resolução do problema.')
    else:
        # Caso não seja uma requisição POST, apenas renderiza o template com os dados do checklist
        return render(request, 'manage_solicitacoes.html', {'checklist': checklist})

    # Se houver algum erro de validação ou não for um POST válido, retorna para o template com as mensagens de erro
    return render(request, 'manage_solicitacoes.html', {'checklist': checklist})