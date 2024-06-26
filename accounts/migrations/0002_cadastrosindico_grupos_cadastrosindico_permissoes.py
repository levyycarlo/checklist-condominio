# Generated by Django 5.0.6 on 2024-06-05 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.AddField(
            model_name='cadastrosindico',
            name='grupos',
            field=models.ManyToManyField(related_name='cadastro_sindico_grupos', to='auth.group'),
        ),
        migrations.AddField(
            model_name='cadastrosindico',
            name='permissoes',
            field=models.ManyToManyField(related_name='cadastro_sindico_permissoes', to='auth.permission'),
        ),
    ]
