from django.urls import path
from accounts.views import register_sindico, sindico_login
from checklist.views import home_dashboard


urlpatterns = [
    # URL para processar o login do síndico
    path('login/sindico/', sindico_login, name='login_sindico'),

    # URL para processar o registro do síndico
    path('register/sindico/', register_sindico, name='register_sindico'),

    #URL para a tela de sindico
    path('home/dashboard/', home_dashboard, name ='home_dashboard')
]
