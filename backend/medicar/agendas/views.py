from rest_framework import mixins, viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from datetime import datetime, date

from .models import Agenda
from .serializers import AgendaSerializer
from .filters import AgendasFilter
from consultas.models import Consulta


class AgendasViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Agenda.objects.filter(dia__gte=date.today()).order_by('dia')
    serializer_class = AgendaSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filter_class = AgendasFilter

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)

        lista_agendas = []
        for agenda in serializer.data:
            horarios_filtrados = []
            for hora in agenda['horarios']:
                dia_horario = datetime.strptime('{}T{}'.format(agenda['dia'], hora), '%Y-%m-%dT%H:%M')
                consulta_marcada = Consulta.objects.filter(dia_horario=dia_horario).exists()
                if dia_horario > datetime.now() and not consulta_marcada:
                    horarios_filtrados.append(hora)
            agenda['horarios'] = horarios_filtrados

            if len(agenda['horarios']) > 0:
                lista_agendas.append(agenda)

        return Response(lista_agendas)
