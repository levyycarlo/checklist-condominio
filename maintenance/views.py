from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
#from django.http import JsonResponse
from django.views.decorators.http import require_POST
from checklist.models import Checklist

def request_totais(request):
    # Renderiza a página de solicitacoes totais
    status = request.GET.get('status')
    # Obter todos os checklists ordenados pela data
    checklist = Checklist.objects.all().order_by('-data_checklist')

    # Filtrar checklists pelo status, se fornecido
    if status and status != 'todos':
         checklist = checklist.filter(status=status)

    # Paginação dos checklists
    paginator = Paginator(checklist, 9)  # 9 checklists por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
    }

    return render(request, 'solicitacoes_totais.html', context)

def manage_solicit(request, checklist_id):
    # Buscar o checklist pelo ID
    checklist = get_object_or_404(Checklist, id=checklist_id)

    # Renderizar a página de edição com as informações do checklist
    return render(request, 'manage_solicitacoes.html', {'checklist': checklist})
