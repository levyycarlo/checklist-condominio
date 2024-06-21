from django.urls import path
from checklist.views import  register_checklist #auth_checklist,

urlpatterns = [

    #URL PARA A TELA DO REGISTRO DE CHECKLIST
    path ('register/checklist/', register_checklist, name= 'register_checklist' ),

    #URL PARA PROCESSAR REGISTRO DE CHECKLIST
    #path ('auth/checklist/sindico', auth_checklist, name= 'auth_checklist)' ),
]

