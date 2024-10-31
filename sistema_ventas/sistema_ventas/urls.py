from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView


urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),
    
    # Autenticación
    path('login/', auth_views.LoginView.as_view(
        template_name='ventas/login.html',
        redirect_authenticated_user=True
    ), name='login'),
    
    path('logout/', auth_views.LogoutView.as_view(
        next_page='login'
    ), name='logout'),
    
    # Redirigir la raíz a la aplicación ventas
    path('', RedirectView.as_view(url='/ventas/', permanent=False)),
    
    # Incluir las URLs de la aplicación ventas
    path('ventas/', include('ventas.urls')),
]