from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework.routers import DefaultRouter

from usuarios.views import UsuarioCreate, UsuarioLogin
from especialidades.views import EspecialidadesViewSet
from medicos.views import MedicosViewSet


router = DefaultRouter()
router.register(r'especialidades', EspecialidadesViewSet)
router.register(r'medicos', MedicosViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuario/criar/', UsuarioCreate.as_view(), name='criar_usuario'),
    path('login/', UsuarioLogin.as_view(), name='altenticar_usuario'),
    path('', include(router.urls)),
]
