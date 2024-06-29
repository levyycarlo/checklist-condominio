from django.urls import path
from maintenance.views import request_totais, manage_solicit
from checklist.views import register_checklist, auth_update_checklist
from frontend.views import home


urlpatterns = [
    # URL para tela de dashboard
    path('', home, name= 'home'),

    # URL para tela de solicitações totais
    path('solicitacoes/totais/', request_totais, name='solicitacoes_totais'),

    # URL para tela de registro de checklist
    path('register/checklist/', register_checklist, name='register_checklist'),

    # URL para tela edição com as informações do checklist
    path('manage/solicit/<int:checklist_id>', manage_solicit, name='manage_solicit'),

    # URL para autenticação update de checklist
    path('auth/update/checklist/<int:checklist_id>/', auth_update_checklist, name='auth_update_checklist')

]