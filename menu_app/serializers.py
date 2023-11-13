from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import *


class BasemodelSerializer(ModelSerializer):
    class Meta:
        model = Basemodel
        fields = "__all__"

class RestaurantSerializers(ModelSerializer):
    class Meta:
        model = Restaurant
        fields = "__all__"


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class MenuSerializer(ModelSerializer):
    category = serializers.CharField(source='category.name', read_only=True)
    restaurant = serializers.CharField(source='restaurant.name', read_only=True)
        
    class Meta:
        model = Menu
        fields = ['name', 'description', 'price', 'photo', 'discount', 'category', 'restaurant']


class AdressTableSerializer(ModelSerializer):
    class Meta:
        model = Adress_table
        fields = ["user", 'name']


class TableSerializer(ModelSerializer):
    restaurant = serializers.CharField(source='restaurant.name', read_only=True)
    adress_table_name = serializers.CharField(source='adress_table.name', read_only=True)
    class Meta:
        model = Table
        fields = ["number", 'type', 'restaurant', 'adress_table_name', 'percent', 'id']
