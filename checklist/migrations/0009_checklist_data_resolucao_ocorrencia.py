# Generated by Django 5.0.6 on 2024-06-25 19:41

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checklist', '0008_checklist_resolucao_problema'),
    ]

    operations = [
        migrations.AddField(
            model_name='checklist',
            name='data_resolucao_ocorrencia',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]