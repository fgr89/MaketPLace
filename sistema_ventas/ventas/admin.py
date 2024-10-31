from django.contrib import admin
from .models import Producto, Venta, DetalleVenta

class DetalleVentaInline(admin.TabularInline):
    model = DetalleVenta
    extra = 1

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'precio', 'stock', 'disponible']
    search_fields = ['nombre', 'descripcion']
    list_filter = ['fecha_creacion', 'fecha_actualizacion']

@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ['id', 'vendedor', 'fecha', 'total', 'estado']
    list_filter = ['fecha', 'estado', 'vendedor']
    inlines = [DetalleVentaInline]
