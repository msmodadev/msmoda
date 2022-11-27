from django.db import models
from django.utils import timezone

from django.contrib.auth.models import AbstractUser

# Create your models here.


class PersonasModel(models.Model):
    CEDULA_DE_CIUDANIA = 'CC'
    CEDULA_DE_EXTRANJERIA = 'CE'
    PERMISO_ESPECIAL_DE_PERMANENCIA = 'PEP'
    REGISTRO_CIVIL = 'RC'
    TARJETA_DE_IDENTIDAD = 'TI'
    VISA = 'V'
    PASAPORTE = 'PP'

    TIPO_DE_DOCUMENTO = [
        ("Selecciona una opción", ""),
        (CEDULA_DE_CIUDANIA, 'Cédula de ciudadania'),
        (CEDULA_DE_EXTRANJERIA, 'Cédula de extranjería'),
        (PERMISO_ESPECIAL_DE_PERMANENCIA, 'Permiso especial de permanencia'),
        (REGISTRO_CIVIL, 'Registro Civil'),
        (TARJETA_DE_IDENTIDAD, 'Tarjeta de Identidad'),
        (VISA, 'Visa'),
        (PASAPORTE, 'Pasaporte'),
    ]

    celular = models.CharField(
        "Celular o telefono",
        max_length=100
    )

    tipo_identificacion = models.CharField(
        "Tipo de identificación",
        choices=TIPO_DE_DOCUMENTO,
        max_length=4
    )

    numero_de_identificacion = models.CharField(
        "Número de identificación",
        max_length=150
    )

    class Meta:
        abstract = True


class ClientesModel(PersonasModel):
    nombres = models.CharField(
        "Nombre(S)",
        max_length=100
    )

    apellidos = models.CharField(
        "Apellido(s)",
        max_length=100
    )

    estado = models.BooleanField(
        'Estado',
        default=True
    )

    created = models.DateTimeField(
        'Fecha de cración',
        default=timezone.now,
    )

    updated = models.DateTimeField(
        'Fecha de edición',
        auto_now=True,
    )

    class Meta:
        db_table = "apps_clientes_model"
        verbose_name = "Usuarios | Cliente"
        verbose_name_plural = "Usuarios | Clientes"


class UsuariosModel(PersonasModel, AbstractUser):   
    email = models.EmailField(
        "Correo",
        blank=True,
        unique=True
    )

    foto = models.URLField(
        "Foto de perfil",
        null=True,
        blank=True
    )

    order = models.PositiveIntegerField(
        'Orden',
        default=1,
    )

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['tipo_identificacion',
                       'numero_de_identificacion', 'username']

    class Meta:
        db_table = "apps_usuarios_model"
        verbose_name = "Usuarios | Usuarios"
        verbose_name_plural = "Usuarios | Usuarios"
