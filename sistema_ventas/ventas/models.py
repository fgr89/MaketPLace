from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Categories"

class Producto(models.Model):
    nombre = models.CharField(max_length=200)  # Cambiado de name a nombre
    description = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)  # Cambiado de price a precio
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')
    stock = models.IntegerField(default=0)
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    is_active = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)  # Cambiado de created_at
    fecha_actualizacion = models.DateTimeField(auto_now=True)  # Cambiado de updated_at
    
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        
    def __str__(self):
        return self.nombre
    
    def disponible(self):
        return self.stock > 0

class Venta(models.Model):
    vendedor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ventas')
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('completada', 'Completada'),
        ('cancelada', 'Cancelada'),
    ]
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='pendiente')
    
    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'
        ordering = ['-fecha']
    
    def __str__(self):
        return f"Venta {self.id} - {self.fecha.strftime('%d/%m/%Y %H:%M')}"
    
    def calcular_total(self):
        return sum(detalle.subtotal() for detalle in self.detalles.all())

class DetalleVenta(models.Model):
    venta = models.ForeignKey(Venta, related_name='detalles', on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    
    class Meta:
        verbose_name = 'Detalle de venta'
        verbose_name_plural = 'Detalles de venta'
    
    def __str__(self):
        return f"{self.producto.nombre} - {self.cantidad} unidades"
    
    def subtotal(self):
        return self.cantidad * self.precio_unitario