from rest_framework import serializers
from .models import programmer


class Modelo_1_Serializer(serializers.ModelSerializer):
 class Meta:
    model = programmer
# fields = ('fullname','languaje','is_active’) acá

fields = '__all__'
# con la opción '__all__' traemos todos los

