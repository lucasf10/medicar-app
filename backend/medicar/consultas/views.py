from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from datetime import datetime

from .models import Consulta
from .serializers import ConsultaSerializer

# Lista todas as consultas marcadas do usuário logado - OK!
# A listagem não deve exibir consultas para dia e horário passados
# Os itens da listagem devem vir ordenados por ordem crescente do dia e horário da consulta - OK!
class ConsultasViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = Consulta.objects.order_by('dia_horario')
    serializer_class = ConsultaSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user, dia_horario__gt=datetime.now())
