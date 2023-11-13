from django.contrib import admin
from .models import *

class MenuAdmin(admin.ModelAdmin):
    list_display = ("name", "price","category","description")
    list_display_links = ("name",)
    list_editable = ("price","category","description")
    list_per_page = 10
    list_filter = ("restaurant",)
    actions_on_top = False
    actions_on_bottom = True
class TableAdmin(admin.ModelAdmin):
    list_display = ("type","number","restaurant","adress_table","percent")

admin.site.register(Menu, MenuAdmin)
admin.site.register(Table, TableAdmin)
admin.site.register(Restaurant)
admin.site.register(Adress_table)
admin.site.register(Category)