# Generated by Django 5.0.6 on 2024-06-09 19:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checklist', '0004_rename_data_criacao_checklist_data_criacao_ocorrencia_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='checklist',
            old_name='data_criacao_ocorrencia',
            new_name='data_criacao_checklist',
        ),
    ]
