# Generated by Django 5.0.6 on 2024-06-25 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_remove_cadastrosindico_is_superuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='cadastrosindico',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='cadastrosindico',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]