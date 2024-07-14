from django.urls import path
from .views import CategoriaListCreate, ProductListCreate, CategoriaDelete

urlpatterns = [
   path("categorias/", CategoriaListCreate.as_view()),
   path("productos/", ProductListCreate.as_view()),
   path("categorias/<int:pk>/", CategoriaDelete.as_view())
]