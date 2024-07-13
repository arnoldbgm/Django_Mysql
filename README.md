# Proyecto Django con Django REST Framework y MySQL

Este documento proporciona una guía paso a paso sobre cómo configurar un proyecto Django con Django REST Framework y una base de datos MySQL.

## Paso 1: Crear y activar un entorno virtual

Primero, crea un entorno virtual utilizando el comando `venv` de Python:

```sh
python -m venv venv
```

Luego, activa el entorno virtual. El comando para activar el entorno varía según tu sistema operativo:

- En Windows:

  ```sh
  venv\Scripts\activate
  ```

- En macOS y Linux:

  ```sh
  source venv/bin/activate
  ```

## Paso 2: Instalar Django, Django REST Framework y MySQL Client

Con el entorno virtual activado, instala Django, Django REST Framework y MySQL Client utilizando `pip`:

```sh
pip install django djangorestframework mysqlclient
```

## Paso 3: Configurar las aplicaciones instaladas

Agrega `rest_framework` a la lista de aplicaciones instaladas en tu archivo `settings.py`:

```python
INSTALLED_APPS = [
    ...
    'rest_framework',
    ...
]
```

## Paso 4: Configurar la base de datos

Configura tu base de datos MySQL en el archivo `settings.py` utilizando la siguiente configuración:

```python
# 🔥🦾 Aqui vas a configurar tu base de datos
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "mydatabase",
        "USER": "mydatabaseuser",
        "PASSWORD": "mypassword",
        "HOST": "127.0.0.1",
        "PORT": "3306",
    }
}
```

Asegúrate de reemplazar `"mydatabase"`, `"mydatabaseuser"`, `"mypassword"` y otros valores con la información correspondiente a tu base de datos.

## Paso 5: Crear una aplicación llamada `restaurante`

Crea una nueva aplicación dentro de tu proyecto Django llamada `restaurante`:

```sh
python manage.py startapp restaurante
```

Luego, agrega la aplicación `restaurante` a la lista de aplicaciones instaladas en tu archivo `settings.py`:

```python
INSTALLED_APPS = [
    ...
    'rest_framework',
    'restaurante',
    ...
]
```

## Paso 6: Crear los modelos de base de datos

Crea los siguientes modelos dentro del archivo `models.py` de tu aplicación `restaurante`:

```python
from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.FloatField()
    categoriaId = models.ForeignKey(Categoria, related_name='productos', on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
```

## IMPORTANTE

Siempre que instales un nuevo paquete o modifiques tus dependencias, asegúrate de actualizar el archivo `requirements.txt` ejecutando:

```sh
pip freeze > requirements.txt
```

Para instalar todas las dependencias listadas en `requirements.txt`, utiliza:

```sh
pip install -r requirements.txt
```

Con estos pasos, habrás configurado tu entorno de desarrollo Django con Django REST Framework y MySQL, además de crear los modelos necesarios para tu aplicación `restaurante` y manejar adecuadamente las dependencias del proyecto.