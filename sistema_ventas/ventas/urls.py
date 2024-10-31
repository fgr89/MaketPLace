from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from django.urls import path

app_name = 'ventas'

urlpatterns = [
    # Dashboard
    path('', views.dashboard, name='dashboard'),
    
    # Productos y disponibilidad
    path('disponibilidad/', views.disponibilidad_producto, name='disponibilidad'),
    path('producto/<int:producto_id>/', views.detalle_producto, name='detalle_producto'),
    path('producto/nuevo/', views.nuevo_producto, name='nuevo_producto'),
    path('producto/<int:producto_id>/editar/', views.editar_producto, name='editar_producto'),
    
    # Inventario
    path('inventario/', views.inventario, name='inventario'),
    path('inventario/actualizar/', views.actualizar_inventario, name='actualizar_inventario'),
    
    # Ventas
    path('resumen/', views.resumen_ventas, name='resumen'),
    path('venta/nueva/', views.nueva_venta, name='nueva_venta'),
    path('venta/<int:venta_id>/', views.detalle_venta, name='detalle_venta'),
    
    # API para actualizaciones dinámicas (opcional)
    path('api/check-stock/<int:producto_id>/', views.check_stock, name='check_stock'),

    # Otras rutas de la aplicación ventas
    path('logout/', LogoutView.as_view(), name='logout'),
]
