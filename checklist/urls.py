from django.urls import path
from checklist.views import register_checklist,home_dashboard, auth_checklist

from frontend.views import home


urlpatterns = [
    # URL para tela de dashboard
    path('', home, name='home'),

    # URL para autenticar o registro de checklist
    path('auth/checklist/', auth_checklist, name='auth_checklist'),

    # URL para tela de dashboard
    path('home/dashboard/', home_dashboard, name='home_dashboard'),

    # URL para tela de registro de checklist
    path('register/checklist/', register_checklist, name='register_checklist')
]