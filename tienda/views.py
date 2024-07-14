from rest_framework.views import APIView
# Me permite generar enpoints de tipo GET, POST, PUT, DELETE
from .models import CategoriaModel, ProductoModel
from .serializers import CategoriaSerializer, ProductosSerializer
from rest_framework.response import Response

# Esta controlador permitira a mi usuario,
# 1. Ver las categorias
# 2. Crear nuevas categorias
class CategoriaListCreate(APIView):
   def get(self, request):
      # Consultas usando la ORM
      # Vamos a practicar el uso de la ORM de DJANGO
      # SELECT * from categorias;
      # Primero el nombre del modelo - objetcs - metodo
      # producto = CategoriaModel.objects.all()
      # SELECT * FROM categorias WHERE id = 1
      # lt => significa lower than  ==> menor que
      #categoria = CategoriaModel.objects.filter(id=1)  # es lo mismo get()
      # Para usar el serializer colocamos
      #print(categoria)
      # El nombre del serializador     (lo que queremos serializar)
      # Debes usar many=True cuando uses .all()   .filter()
      # No debe usarse cuando uses .get()    .first()    
      # INSERT ORM
      
      # INSERT INTO CategorialModel (nombre) VALUES ('Libros');
      # El create es una insercion en la base de datos => chantamos nuestra data 
      # en la bd
      # categoria = CategoriaModel.objects.create(nombre="Muebles")
      
      # UPDATE ORM
      # Amiguito modificame el registro 4 de mi tabla categorias, quiero
      # que se llame Deportes
      # categoria = CategoriaModel.objects.filter(id=4)
      # categoria.nombre = "Deportes"
      # categoria.save()
      # serializer = CategoriaSerializer(categoria)
      categoria = CategoriaModel.objects.all()
      serializer = CategoriaSerializer(categoria, many=True)
      return Response({"msg":serializer.data}) 
   
   def post(self, request):
      # request.data
      # {
      #  "nombre": "Robots"
      # }
      serializer = CategoriaSerializer(data=request.data)
      # Retorna un true o un false, si mi data cumple con lo establecido
      if serializer.is_valid():
         # Para guardar hariamos un model.objects.create(*******)
         # CategoriaModel.objects.create(***lo que envio****)
         serializer.save()
         return Response({"msg": serializer.data})
      else:
         # Muestra un error de que la data no esta valida
         return Response({"msg": "La data no cumple 😢"}) 
      
#Vamos a crear un endpoint que me traiga toda las lista de productos
# con su categoria, de tipo get

class ProductListCreate(APIView):
   def get(self,request):
      # Select * from productos
      productos = ProductoModel.objects.all()
      serializer = ProductosSerializer(productos, many=True)
      return Response(serializer.data)
   

class CategoriaDelete(APIView):
   # pk = primary key => llave primaria = id
   def delete(self,request, pk):
      categoria = CategoriaModel.objects.get(id=pk)
      categoria.delete()
      return Response ({"msg": "Eliminacion exitosa 👍"})