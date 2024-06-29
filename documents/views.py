from django.shortcuts import render, redirect
from checklist.models import Checklist
import os
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def logs(request):
    log_file = 'admin_actions.log'
    logs_content = []

    # Verifica se o arquivo de log existe
    if os.path.exists(log_file):
        with open(log_file, 'r') as f:
            logs_content = f.readlines()

    # Paginação dos registros de log
   # Lê o arquivo de log e inverte a ordem das linhas
    with open(log_file, 'r')   as log_file:
        logs_content = log_file.readlines()[::-1]  # Inverte a ordem das linhas
        
     # Preparando os registros formatados para exibição
    logs_formatted = []
    for index, line in enumerate(logs_content):
        parts = line.split(' - ')
        if len(parts) >= 2:
            log_id = index + 1
            timestamp = parts[0]
            action = parts[1].strip()
            logs_formatted.append({
                'id': log_id,
                'timestamp': timestamp,
                'action': action,
            })

    paginator = Paginator(logs_content, 20)  # 20 registros por página
    page_number = request.GET.get('page')
    try:
        logs_page = paginator.page(page_number)
    except PageNotAnInteger:
        logs_page = paginator.page(1)
    except EmptyPage:
        logs_page = paginator.page(paginator.num_pages)

    return render(request, 'logs.html', {'logs_page': logs_page})