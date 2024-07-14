from django.db import models

# Create your models here.


class CategoriaModel(models.Model):
    nombre = models.CharField(max_length=190, blank=False, null=False)


class ProductoModel(models.Model):
    nombre = models.CharField(max_length=191, blank=False, null=False)
    descripcion = models.TextField()
    precio = models.FloatField(blank=False, null=False)
    categoriaId = models.ForeignKey(
        CategoriaModel, related_name='productos', on_delete=models.CASCADE)

   # Cascada => Elimina todos los registros
   # Protect => Eliminar solo cuando no halla dependientes