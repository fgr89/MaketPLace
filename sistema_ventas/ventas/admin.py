from django.contrib import admin
from .models import Producto, Venta, DetalleVenta, Category

class DetalleVentaInline(admin.TabularInline):
    model = DetalleVenta
    extra = 1
    raw_id_fields = ('producto',)
    fields = ['producto', 'cantidad', 'precio_unitario']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at', 'updated_at']
    search_fields = ['name', 'description']
    list_filter = ['created_at']

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'precio', 'category', 'stock', 'is_active', 'disponible']
    search_fields = ['nombre', 'description']
    list_filter = ['fecha_creacion', 'fecha_actualizacion', 'category', 'is_active']
    raw_id_fields = ['seller']
    date_hierarchy = 'fecha_creacion'
    list_editable = ['precio', 'stock', 'is_active']
    list_per_page = 20
    fieldsets = (
        ('Información básica', {
            'fields': ('nombre', 'description', 'precio', 'category')
        }),
        ('Inventario', {
            'fields': ('stock', 'is_active')
        }),
        ('Información adicional', {
            'fields': ('seller', 'image'),
            'classes': ('collapse',)
        }),
    )

@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ['id', 'vendedor', 'fecha', 'total', 'estado']
    list_filter = ['fecha', 'estado', 'vendedor']
    search_fields = ['vendedor__username', 'id']
    date_hierarchy = 'fecha'
    inlines = [DetalleVentaInline]
    list_per_page = 20
    readonly_fields = ['fecha', 'total']
    
    def has_delete_permission(self, request, obj=None):
        # Solo permite eliminar ventas pendientes
        if obj is not None and obj.estado != 'pendiente':
            return False
        return super().has_delete_permission(request, obj)

@admin.register(DetalleVenta)
class DetalleVentaAdmin(admin.ModelAdmin):
    list_display = ['venta', 'producto', 'cantidad', 'precio_unitario', 'subtotal']
    search_fields = ['producto__nombre', 'venta__id']
    list_filter = ['venta__fecha']
    raw_id_fields = ('producto', 'venta')
    readonly_fields = ['subtotal']

    def subtotal(self, obj):
        return obj.cantidad * obj.precio_unitario
    subtotal.short_description = 'Subtotal'