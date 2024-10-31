

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Producto, Venta, DetalleVenta

@login_required
def dashboard(request):
    return render(request, 'ventas/dashboard.html')

@login_required
def disponibilidad_producto(request):
    productos = Producto.objects.all()
    return render(request, 'ventas/disponibilidad.html', {'productos': productos})

@login_required
def detalle_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    return render(request, 'ventas/detalle_producto.html', {'producto': producto})

@login_required
def nuevo_producto(request):
    if request.method == 'POST':
        # Agregar lógica para crear nuevo producto
        pass
    return render(request, 'ventas/form_producto.html')

@login_required
def editar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        # Agregar lógica para editar producto
        pass
    return render(request, 'ventas/form_producto.html', {'producto': producto})

@login_required
def inventario(request):
    productos = Producto.objects.all()
    return render(request, 'ventas/inventario.html', {'productos': productos})

@login_required
def actualizar_inventario(request):
    if request.method == 'POST':
        # Agregar lógica para actualizar inventario
        pass
    return redirect('ventas:inventario')

@login_required
def resumen_ventas(request):
    ventas = Venta.objects.filter(vendedor=request.user)
    return render(request, 'ventas/resumen_ventas.html', {'ventas': ventas})

@login_required
def nueva_venta(request):
    if request.method == 'POST':
        # Agregar lógica para crear nueva venta
        pass
    productos = Producto.objects.all()
    return render(request, 'ventas/form_venta.html', {'productos': productos})

@login_required
def detalle_venta(request, venta_id):
    venta = get_object_or_404(Venta, id=venta_id)
    return render(request, 'ventas/detalle_venta.html', {'venta': venta})

@login_required
def check_stock(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    return JsonResponse({
        'stock': producto.stock,
        'disponible': producto.stock > 0
    })