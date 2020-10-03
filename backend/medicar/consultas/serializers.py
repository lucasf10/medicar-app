from rest_framework.serializers import ModelSerializer, DateTimeField

from .models import Consulta
from medicos.serializers import MedicoSerializer


class ConsultaSerializer(ModelSerializer):
    medico = MedicoSerializer(read_only=True)
    dia = DateTimeField(source='dia_horario', format='%Y-%m-%d')
    horario = DateTimeField(source='dia_horario', format='%H:%M')

    class Meta:
        model = Consulta
        fields = ('id', 'dia', 'horario', 'data_agendamento', 'medico')
