# Generated by Django 5.0.6 on 2024-06-29 02:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checklist', '0010_rename_resolucao_problema_checklist_resolucao_ocorrencia'),
    ]

    operations = [
        migrations.RenameField(
            model_name='checklist',
            old_name='imagem',
            new_name='upload',
        ),
        migrations.RenameField(
            model_name='imagem',
            old_name='uploads',
            new_name='upload',
        ),
    ]