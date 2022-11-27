from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from apps.usuarios.models import UsuariosModel


@admin.register(UsuariosModel)
class UsuariosAdmin(UserAdmin):
    list_display = (
        "id",
        "email",
        "username",
        "get_full_name",
        "is_staff",
        "is_active",
        "date_joined"
    )

    list_display_links = (
        "id",
        "email",
        "username"
    )

    list_filter = (
        "tipo_identificacion",
        "is_staff",
        "is_superuser",
        "is_active",
        "groups"
    )

    fieldsets = (
        (
            "Datos de usuario",
            {
                "fields":
                (
                    "username",
                    "email",
                    "password"
                )
            }
        ),
        (
            "Información personal",
            {
                "fields":
                (
                    "first_name",
                    "last_name",
                )
            }
        ),
        (
            "Permissions",
            {
                "fields":
                (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (
            "Fechas",
            {
                "fields":
                (
                    "last_login",
                    "date_joined"
                )
            }
        ),
        (
            "Otros campos",
            {
                "fields":
                (
                    "order",
                )
            }
        )
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "password1", "password2"),
            },
        ),
    )

    filter_horizontal = (
        "groups",
        "user_permissions",
    )

    ordering = (
        "username",
        "id",
        "email"
    )

    search_fields = (
        "username",
        "first_name",
        "last_name",
        "email"
    )

    readonly_fields = (
        "date_joined",
        "last_login"
    )
