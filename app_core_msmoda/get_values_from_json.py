import json
from django.core.exceptions import ImproperlyConfigured

with open("configuracion.json") as f:
    valor = json.loads(f.read())

def get_value(titulo, valores=valor):
    try:
        return valores[titulo]
    except:
        raise ImproperlyConfigured(f"El nombre {titulo} no existe o no ha sido declarado")
    