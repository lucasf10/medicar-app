from django.contrib import admin
from django.urls import path
from django.conf.urls import include

from usuarios.views import UsuarioCreate, UsuarioLogin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuario/criar/', UsuarioCreate.as_view(), name='criar_usuario'),
    path('login/', UsuarioLogin.as_view(), name='altenticar_usuario')
]
