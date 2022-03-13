from django.contrib import admin
from .models import Producto,CategoriaProd

# Register your models here.
class CategoriaProdAdmin(admin.ModelAdmin):
    readonly_fields=("create", "updated")

class ProductoAdmin(admin.ModelAdmin):
    readonly_fields=("create", "updated")


admin.site.register(CategoriaProd,CategoriaProdAdmin)

admin.site.register(Producto, ProductoAdmin)
