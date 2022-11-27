# Documentación para crear y sincronizar un proyecto en deploy con pythonanywhere (django bakend), separando backend y frontend

## Backend
### Crear un proyecto desplegado en pythonanywhere (host gratuito para aplicaciones python):
1. Crear usuario en pythonanywhere.com
2. Crear nuevo repositorio en github.com
3. Dentro de github Usuario >  Settings > Developer Settings > Personal access tokens > Fine-grained personal access tokens > Generate token > name the token > permissions > colocar todos los permisos en read and write si es posible > generate token
4. En pythonanywhere > crear app > django
5. ingresar a la aplicación principal
6. Darle a "Open Bash Console Here"
7. Inicializar git
```console
git init
git config --global user.email "corre@ejemplo.com"
git config --global user.name "usuario"
git commit -m "Primer commit"
git remote add origin https://url_del_proyecto/nombre.git
```
Acá deben de aparecer algo como "ingrese usuario y contraseña"
En la contraseña ingresar el token previamente generado en el paso 3 o configurar la ssh public key
```console
git push -u origin main  
```


### Sincronizar el proyecto del servidor con nuestro local:
1. Crear un entorno virtual
```console
python -m venv nombre_del_entorno
```

2. Activar el entorno virtual:
```console
En la ruta del entorno:
nombre_del_entorno\Scripts\activate
```
Resultado:
(nombre_del_entorno) c:\path_proyecto

3. Instalar los requerimientos | con el entorno activo:
```console
pip install -r requeriments.txt
```

4. Ir a la carpeta donde va a quedar el proyecto y descargar el proyecto en nuestro local:
```git
git clone https://url_del_proyecto/nombre.git
```

5. Realizar las respectivas configuraciones del settings.py
- ALLOWERD_HOSTS
- DEBUG
- Aplicaciones de terceros
- Aplicaciones creadas por uno
- Si se va a manejar o no el sistema de templates de django
- La base de datos
- Lenguage
- Zona horaria
- Y carpetas: Static y Media

## Cómo crear apps en django:
1. a la altura del manage.py crear una carpeta llamada applications o apps (esto por convención, pero puede tener cualquier nombre)
2. ir a la carpeta
```console
cd apps
```
3. Crear la aplicación utilizando django-admin
```console
django-admin startapp nombre_de_la_app
```
4. Cambiar el archivo apps.py autogenerado
ejemplo:
class NombreDeLaApp(AppConfig):
    name = 'path.nombre_de_la_app'

5. Agregar el mismo nombre a las apps del settings

## Cómo crear tablas en Django (todo)
1. dentro de la aplicación en el archivo models.py
2. ver un tutorial, ya me mame de copiar


### Frontend
1. Instalar node.js
2. Crear la app de react
```console
npx create-react-app nombre_de_la_app
```
3. Iniciar la app
```console
cd nombre_de_la_app
npm start
```
