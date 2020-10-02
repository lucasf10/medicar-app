from rest_framework.serializers import ModelSerializer, DateField, TimeField

from .models import Consulta
from medicos.serializers import MedicoSerializer


class ConsultaSerializer(ModelSerializer):
    medico = MedicoSerializer(read_only=True)
    dia = DateField(source='dia_horario')
    horario = TimeField(source='dia_horario')

    class Meta:
        model = Consulta
        fields = ('id', 'dia', 'horario', 'data_agendamento', 'medico')
