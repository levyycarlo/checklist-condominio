# Generated by Django 5.0.6 on 2024-06-25 19:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checklist', '0009_checklist_data_resolucao_ocorrencia'),
    ]

    operations = [
        migrations.RenameField(
            model_name='checklist',
            old_name='resolucao_problema',
            new_name='resolucao_ocorrencia',
        ),
    ]
