from django.urls import path, include
from rest_framework import routers 
from Biblioteca import views 

router = routers.DefaultRouter() 

router.register(r'Nacionalidad', views.Nacionalidad_ViewSet) 
router.register(r'Autor', views.Autor_ViewSet) 
router.register(r'Comuna', views.Comuna_ViewSet) 
router.register(r'Direccion', views.Direccion_ViewSet) 
router.register(r'Biblioteca', views.Biblioteca_ViewSet) 
router.register(r'Lector', views.Lector_ViewSet) 
router.register(r'Libro', views.Libro_ViewSet) 
router.register(r'Genero', views.Genero_ViewSet) 
router.register(r'Prestamo', views.Prestamo_ViewSet) 

urlpatterns = [ 
 path('', include(router.urls)) 

] 