from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework.routers import DefaultRouter
from django.utils.timezone import make_aware

from usuarios.views import UsuarioCreate, UsuarioLogin
from especialidades.views import EspecialidadesViewSet
from medicos.views import MedicosViewSet
from agendas.views import AgendasViewSet
from consultas.views import ConsultasViewSet


router = DefaultRouter()
router.register(r'especialidades', EspecialidadesViewSet)
router.register(r'medicos', MedicosViewSet)
router.register(r'agendas', AgendasViewSet)
router.register(r'consultas', ConsultasViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuario/criar/', UsuarioCreate.as_view(), name='criar_usuario'),
    path('login/', UsuarioLogin.as_view(), name='autenticar_usuario'),
    path('', include(router.urls)),
]
