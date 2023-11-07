from django.urls import path
from .views import *

urlpatterns = [
    path("api/restaurant", restaurant.as_view({"post": "create"}), name="restaurant"),
    path("api/restaurant_get", restaurant.as_view({"get": "list"}), name="restaurant"),
    path("api/category", category.as_view({"post": "create"}), name="category"),
    path("api/category_get", category.as_view({"get": "list"}), name="category"),
    path("api/menu", menu.as_view({"post": "create"}), name="menu"),
    path("api/menu_get", menu.as_view({"get": "list"}), name="menu"),
]
