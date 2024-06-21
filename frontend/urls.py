from django.urls import path
from frontend.views import home, sobre, login_sindico, cadastro_sindico 
from accounts.views import register_sindico, sindico_login

urlpatterns = [
    # URL para a tela home do site
    path('', home, name='home'),

    # URL para a tela sobre do site
    path('sobre/', sobre, name='sobre'),

    # URL para a tela de login do síndico
    path('login/sindico/', login_sindico, name='login_sindico'),

    # URL para a tela de cadastro do síndico
    path('cadastrar/sindico/', cadastro_sindico, name='cadastrar_sindico'),

    # URL para autenticação de cadastro de síndico
    path('register/add_sindico/', register_sindico, name='register_sindico'),

    # URL para a autenticação do síndico
    path('login/auth_sindico/', sindico_login, name='sindico_login')
]
