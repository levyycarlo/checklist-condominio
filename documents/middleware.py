# ARQUIVO DE LOG !!#

import logging
from django.utils.deprecation import MiddlewareMixin
from accounts.models import CadastroSindico  # Importe seu modelo CadastroSindico aqui

logger = logging.getLogger(__name__)
handler = logging.FileHandler('admin_actions.log')
formatter = logging.Formatter('%(asctime)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)

class AdminActionsLoggingMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.user.is_authenticated:
            user_email = request.user.email
            if request.user.is_superuser:
                try:
                    cadastro_sindico = CadastroSindico.objects.get(email=request.user.email)
                    user_email = cadastro_sindico.email
                except CadastroSindico.DoesNotExist:
                    pass  # Fallback to request.user.email

            action = f"User {user_email} accessed {request.path}"
            logger.info(action)
