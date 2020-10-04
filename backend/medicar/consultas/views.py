from rest_framework import mixins, viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from datetime import datetime
from django.utils.timezone import make_aware, now

from .models import Consulta
from .serializers import ConsultaSerializer
from agendas.models import Agenda


class ConsultasViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = Consulta.objects.filter(dia_horario__gt=now()).order_by('dia_horario')
    serializer_class = ConsultaSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        agenda_id = request.data.get('agenda_id')
        horario = request.data.get('horario')
        agenda = Agenda.objects.filter(id=agenda_id).first()

        if not agenda_id or not horario or not agenda:
            return Response(
                {'mensagem': 'Verifique os campos.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        dia_horario = datetime.strptime('{}T{}'.format(agenda.dia, horario), '%Y-%m-%dT%H:%M')
        horario = dia_horario.time()

        if horario not in agenda.horarios or make_aware(dia_horario) < now():
            return Response(
                {'mensagem': 'Horário não disponível.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        consulta, criado = Consulta.objects.get_or_create(
            dia_horario=make_aware(dia_horario),
            medico=agenda.medico,
            defaults={'paciente': request.user}
        )

        if not criado:
            return Response(
                {'mensagem': 'Horário não disponível.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        return Response(ConsultaSerializer(consulta).data, status=status.HTTP_201_CREATED)

    def get_queryset(self):
        return self.queryset.filter(paciente=self.request.user)
