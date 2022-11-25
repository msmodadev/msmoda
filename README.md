# Crear un proyecto desplegado en pythonanywhere (host gratuito para aplicaciones python):
1. Crear usuario en pythonanywhere.com
2. Crear nuevo repositorio en github.com
3. Dentro de github Usuario >  Settings > Developer Settings > Personal access tokens > Fine-grained personal access tokens > Generate token > name the token > permissions > colocar todos los permisos en read and write si es posible > generate token

#Crear un proyecto con Django:
1. Crear un entorno virtual
```console
python -m venv nombre_del_entorno
```

2. Activar el entorno virtual
```console
En la ruta del entorno:
nombre_del_entorno\Scripts\activate
```
Resultado:
(nombre_del_entorno) c:\path_proyecto

3. Instalar la versión de Django requerida | con el entorno activo
```console
pip install django==4.0.1
```
