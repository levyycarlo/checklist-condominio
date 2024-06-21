# Generated by Django 5.0.6 on 2024-06-08 18:07

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checklist', '0002_imagem_remove_checklist_foto_checklist_uploads_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='checklist',
            old_name='descricao',
            new_name='descricao_problema',
        ),
        migrations.RenameField(
            model_name='imagem',
            old_name='imagem',
            new_name='uploads',
        ),
        migrations.RemoveField(
            model_name='checklist',
            name='fotos',
        ),
        migrations.RemoveField(
            model_name='checklist',
            name='local',
        ),
        migrations.RemoveField(
            model_name='checklist',
            name='uploads',
        ),
        migrations.AddField(
            model_name='checklist',
            name='andar',
            field=models.CharField(blank=True, choices=[('andar1', 'Andar 1'), ('andar2', 'Andar 2'), ('andar3', 'Andar 3')], default=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='checklist',
            name='apartamento',
            field=models.CharField(blank=True, choices=[('apartamento1', 'Apartamento n° 1'), ('apartamento2', 'Apartamento n° 2'), ('apartamento3', 'Apartamento n° 3')], default=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='checklist',
            name='areas_comuns',
            field=models.CharField(blank=True, choices=[('corredorPrincipal', 'Corredor Principal'), ('escadas', 'Escadas'), ('elevadores', 'Elevadores'), ('garagem', 'Garagem'), ('salaoFestas', 'Salão de Festas'), ('academia', 'Academia'), ('piscina', 'Piscina'), ('playground', 'Playground'), ('quadraEsportiva', 'Quadra Esportiva'), ('churrasqueira', 'Churrasqueira'), ('salaReunioes', 'Sala de Reuniões'), ('salaJogos', 'Sala de Jogos')], default=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='checklist',
            name='areas_externas',
            field=models.CharField(blank=True, choices=[('estacionamento', 'Estacionamento'), ('jardim', 'Jardim'), ('quadraTennis', 'Quadra de Tênis'), ('quadraFutebol', 'Quadra de Futebol'), ('patio', 'Pátio'), ('ciclovia', 'Ciclovia')], default=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='checklist',
            name='data_criacao',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='checklist',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
        migrations.AddField(
            model_name='checklist',
            name='outros',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='checklist',
            name='torre',
            field=models.CharField(blank=True, choices=[('TorreA', 'Torre A'), ('TorreB', 'Torre B'), ('TorreC', 'Torre C')], default=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='checklist',
            name='categoria',
            field=models.CharField(blank=True, choices=[('estrutural', 'Estrutural'), ('administrativo', 'Administrativo'), ('seguranca', 'Segurança'), ('emergencia', 'Emergência'), ('sinistro', 'Sinistro'), ('recursosHumanos', 'Recursos Humanos'), ('manutencaoRecorrente', 'Manutenção Recorrente'), ('limpeza', 'Limpeza'), ('jardinagem', 'Jardinagem'), ('insetosPragas', 'Insetos/Pragas'), ('barulho', 'Barulho'), ('vizinhos', 'Relações com Vizinhos')], default=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='checklist',
            name='condominio',
            field=models.CharField(blank=True, choices=[('CondomínioA', 'Condomínio A'), ('CondomínioB', 'Condomínio B'), ('CondomínioC', 'Condomínio C')], default=True, max_length=100, null=True),
        ),
    ]