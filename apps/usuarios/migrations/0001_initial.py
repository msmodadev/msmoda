# Generated by Django 4.1.3 on 2022-11-26 23:57

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('celular', models.CharField(max_length=100, verbose_name='Celular o telefono')),
                ('tipo_identificacion', models.CharField(choices=[('CC', 'Cédula de ciudadania'), ('CE', 'Cédula de extranjería'), ('PEP', 'Permiso especial de permanencia'), ('RC', 'Registro Civil'), ('TI', 'Tarjeta de Identidad'), ('V', 'Visa'), ('PP', 'Pasaporte')], max_length=4, verbose_name='Tipo de identificación')),
                ('numero_de_identificacion', models.CharField(max_length=150, verbose_name='Número de identificación')),
                ('nombres', models.CharField(max_length=100, verbose_name='Nombre(S)')),
                ('apellidos', models.CharField(max_length=100, verbose_name='Apellido(s)')),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Fecha de cración')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
            ],
            options={
                'verbose_name': 'Usuarios | Cliente',
                'verbose_name_plural': 'Usuarios | Clientes',
                'db_table': 'apps_clientes_model',
            },
        ),
        migrations.CreateModel(
            name='UsuariosModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('celular', models.CharField(max_length=100, verbose_name='Celular o telefono')),
                ('tipo_identificacion', models.CharField(choices=[('CC', 'Cédula de ciudadania'), ('CE', 'Cédula de extranjería'), ('PEP', 'Permiso especial de permanencia'), ('RC', 'Registro Civil'), ('TI', 'Tarjeta de Identidad'), ('V', 'Visa'), ('PP', 'Pasaporte')], max_length=4, verbose_name='Tipo de identificación')),
                ('numero_de_identificacion', models.CharField(max_length=150, verbose_name='Número de identificación')),
                ('email', models.EmailField(blank=True, max_length=254, unique=True, verbose_name='Correo')),
                ('foto', models.URLField(blank=True, null=True, verbose_name='Foto de perfil')),
                ('order', models.PositiveIntegerField(default=1, verbose_name='Orden')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Usuarios | Usuarios',
                'verbose_name_plural': 'Usuarios | Usuarios',
                'db_table': 'apps_usuarios_model',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
