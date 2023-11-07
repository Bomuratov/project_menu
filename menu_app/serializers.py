from rest_framework.serializers import ModelSerializer
from .models import *


class RestaurantSerializers(ModelSerializer):
    class Meta:
        model = Restaurant
        fields = "__all__"


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class MenuSerializer(ModelSerializer):
    class Meta:
        model = Menu
        fields = "__all__"