from rest_framework import serializers 
from .models import menuList 

class menuserializer(serializers.ModelSerializer):
    class Meta :
        model = menuList
        fields = ["menuname"]

class submenuserializer(serializers.ModelSerializer):
    class Meta : 
        model = MenuList
        fields = ["menuname","submenuname","menulink","MenuType"]