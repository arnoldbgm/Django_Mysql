from rest_framework import serializers
from .models import CategoriaModel, ProductoModel

class CategoriaSerializer(serializers.ModelSerializer):
   class Meta:
      model =  CategoriaModel  #El nombre de mi modelo
      fields = '__all__'   #Aqui se coloca los campos
      # 1. Esto hace el serializer por detras
      # {
      #    "id": "15",
      #    "nombre": "Linea Blanca"
      # }
      # 2. Tambien hace las validaciones
      # 3. Tambien crear y actualizar.

class ProductosSerializer(serializers.ModelSerializer):
   categoriaId = CategoriaSerializer()
   
   class Meta:
      model = ProductoModel
      # PAra ordenar la respuesta se usa el fields
      # fields = '__all__'
      fields = ['id', 'nombre', 'precio', 'descripcion', 'categoriaId']
      # {
      #    "id",
      #    "nombre"
      #    "descripcion",
      #    "double",
      #    "categoriaId":{
      #        id: 1    
      #        nombre : "..."
      #     }
      # }