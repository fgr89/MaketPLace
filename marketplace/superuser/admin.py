from django.contrib import admin
from .models import Category, Product
from django.utils.html import format_html

admin.site.register(Category)
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock', 'image_preview']  # Mostrar estos campos en la lista
    
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" />', obj.image.url)
        return "Sin imagen"
    
    image_preview.short_description = 'Vista previa'