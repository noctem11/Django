from django.urls import path, include
from rest_framework import routers
from api import views

router = routers.DefaultRouter() # este elemento

router.register(r'programmers',
views.ProgrammerViewSet)
# la r permite que no se interprete como un salto de


# 'programmers' es un ENDPOINT
urlpatterns = [

]