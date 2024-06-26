# Generated by Django 5.0.6 on 2024-06-06 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_rename_cadastro_sindico_cadastrosindico'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cadastrosindico',
            options={},
        ),
        migrations.AlterModelManagers(
            name='cadastrosindico',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='cadastrosindico',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='cadastrosindico',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='cadastrosindico',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='cadastrosindico',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='cadastrosindico',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='cadastrosindico',
            name='username',
        ),
        migrations.AlterField(
            model_name='cadastrosindico',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='cadastrosindico',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups'),
        ),
        migrations.AlterField(
            model_name='cadastrosindico',
            name='password',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='cadastrosindico',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions'),
        ),
    ]
