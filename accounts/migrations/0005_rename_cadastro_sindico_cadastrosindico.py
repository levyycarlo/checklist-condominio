# Generated by Django 5.0.6 on 2024-06-05 21:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_rename_cadastrosindico_cadastro_sindico'),
        ('admin', '0003_logentry_add_action_flag_choices'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cadastro_Sindico',
            new_name='CadastroSindico',
        ),
    ]
