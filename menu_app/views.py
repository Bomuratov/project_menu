from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.decorators import action
from .serializers import *
from .models import *


class Restaurant_view(ModelViewSet):
    queryset = Restaurant.objects.all()
    parser_classes = [MultiPartParser, FormParser]
    serializer_class = RestaurantSerializers


class Category_view(ModelViewSet):
    queryset = Category.objects.all()
    parser_classes = [MultiPartParser, FormParser]
    serializer_class = CategorySerializer


class Menu_view(ModelViewSet):
    queryset = Menu.objects.all()
    parser_classes = [MultiPartParser, FormParser]
    serializer_class = MenuSerializer

    def get_queryset(self):
        restaurant_name = self.kwargs['name_restaurant']
        restaurant = get_object_or_404(Restaurant, name=restaurant_name)
        return Menu.objects.filter(restaurant=restaurant)


class Table_view(ModelViewSet):
    queryset = Table.objects.all()
    parser_classes = [MultiPartParser, FormParser]
    serializer_class = TableSerializer

    def get_queryset(self):
        restaurant_name = self.kwargs['name_restaurant']
        restaurant = get_object_or_404(Restaurant, name=restaurant_name)
        return Table.objects.filter(restaurant=restaurant)





