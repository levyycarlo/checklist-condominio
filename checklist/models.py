from django.db import models
from django.utils import timezone


class Imagem(models.Model):
    uploads = models.ImageField(upload_to='uploads/')

class Checklist(models.Model):
    CONDOMINIOS_CHOICES = [
        ('CondomínioA', 'Condomínio A'),
        ('CondomínioB', 'Condomínio B'),
        ('CondomínioC', 'Condomínio C'),
        # Adicione mais opções conforme necessário
    ]

    PRIORIDADE_CHOICES = [
        ('baixa', 'Baixa'),
        ('média', 'Média'),
        ('alta', 'Alta'),
        ('urgente', 'Urgente'),
    ]

    CATEGORIA_CHOICES = [
        ('estrutural', 'Estrutural'),
        ('administrativo', 'Administrativo'),
        ('seguranca', 'Segurança'),
        ('emergencia', 'Emergência'),
        ('sinistro', 'Sinistro'),
        ('recursosHumanos', 'Recursos Humanos'),
        ('manutencaoRecorrente', 'Manutenção Recorrente'),
        ('limpeza', 'Limpeza'),
        ('jardinagem', 'Jardinagem'),
        ('insetosPragas', 'Insetos/Pragas'),
        ('barulho', 'Barulho'),
        ('vizinhos', 'Relações com Vizinhos'),
        # Adicione mais opções conforme necessário
    ]

    TORRE_CHOICES = [
        ('TorreA', 'Torre A'),
        ('TorreB', 'Torre B'),
        ('TorreC', 'Torre C'),
        # Adicione mais opções conforme necessário
    ]

    ANDAR_CHOICES = [
        ('andar1', 'Andar 1'),
        ('andar2', 'Andar 2'),
        ('andar3', 'Andar 3'),
        # Adicione mais opções conforme necessário
    ]

    APARTAMENTO_CHOICES = [
        ('apartamento1', 'Apartamento n° 1'),
        ('apartamento2', 'Apartamento n° 2'),
        ('apartamento3', 'Apartamento n° 3'),
        # Adicione mais opções conforme necessário
    ]

    AREAS_COMUNS_CHOICES = [
        ('corredorPrincipal', 'Corredor Principal'),
        ('escadas', 'Escadas'),
        ('elevadores', 'Elevadores'),
        ('garagem', 'Garagem'),
        ('salaoFestas', 'Salão de Festas'),
        ('academia', 'Academia'),
        ('piscina', 'Piscina'),
        ('playground', 'Playground'),
        ('quadraEsportiva', 'Quadra Esportiva'),
        ('churrasqueira', 'Churrasqueira'),
        ('salaReunioes', 'Sala de Reuniões'),
        ('salaJogos', 'Sala de Jogos'),
        # Adicione mais opções conforme necessário
    ]

    AREAS_EXTERNAS_CHOICES = [
        ('estacionamento', 'Estacionamento'),
        ('jardim', 'Jardim'),
        ('quadraTennis', 'Quadra de Tênis'),
        ('quadraFutebol', 'Quadra de Futebol'),
        ('patio', 'Pátio'),
        ('ciclovia', 'Ciclovia'),
        # Adicione mais opções conforme necessário
    ]
    
    
    condominio = models.CharField(max_length=100, choices=CONDOMINIOS_CHOICES, null= True, blank= True, default=True)
    torre = models.CharField(max_length=100, choices=TORRE_CHOICES, null= True, blank= True, default=True)
    andar = models.CharField(max_length=100, choices=ANDAR_CHOICES, null= True, blank= True, default=True)
    apartamento = models.CharField(max_length=100, choices=APARTAMENTO_CHOICES,null= True, blank= True, default=True)
    areas_comuns = models.CharField(max_length=100, choices=AREAS_COMUNS_CHOICES, null= True, blank= True, default=True)
    areas_externas = models.CharField(max_length=100, choices=AREAS_EXTERNAS_CHOICES, null= True, blank= True, default=True)
    outros = models.TextField(blank=True)
    prioridade = models.CharField(max_length=100, choices=PRIORIDADE_CHOICES)
    categoria = models.CharField(max_length=100, choices=CATEGORIA_CHOICES, null= True, blank= True, default=True)
    descricao_problema = models.TextField()
    imagem = models.ImageField(upload_to='uploads/', blank=True, null=True)
    autor_tipo = models.CharField(max_length=100)
    nome_autor = models.CharField(max_length=100)
    cpf_autor = models.CharField(max_length=14)
    data_upload = models.DateTimeField(default=timezone.now)
    data_checklist = models.DateTimeField(default=timezone.now, blank=True, null=True)


    def __str__(self):
        return f'Checklist #{self.pk} - {self.condominio}'
