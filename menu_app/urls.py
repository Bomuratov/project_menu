from django.urls import include, path
from .views import *
from .routes import *




urlpatterns = [
    path("api/", include(router.urls)),
    # path("api/menu/", Menu_view.as_view({"get": "list"}), name="menu"),
    path("api/table/<str:name_restaurant>/", Table_view.as_view({"get": "list"}), name="table"),
    path("api/menu/<str:name_restaurant>/", Menu_view.as_view({"get": "list"}), name="menu"),
]
