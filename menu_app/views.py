from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.parsers import MultiPartParser, FormParser
from .serializers import *
from .models import *


class restaurant(ModelViewSet):
    queryset = Restaurant
    parser_classes = [MultiPartParser, FormParser]
    serializer_class = RestaurantSerializers


class category(ModelViewSet):
    queryset = Category
    parser_classes = [MultiPartParser, FormParser]
    serializer_class = CategorySerializer


class menu(ModelViewSet):
    queryset = Menu
    parser_classes = [MultiPartParser, FormParser]
    serializer_class = MenuSerializer
