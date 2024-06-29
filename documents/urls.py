from django.urls import path
from checklist.views import home_dashboard
from documents.views import logs



urlpatterns = [
    # URL para tela de logs

    path('home/dashboard/', home_dashboard, name='home_dashboard'),

    path('logs/',logs, name='logs')

]