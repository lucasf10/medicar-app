from rest_framework.serializers import ModelSerializer, ListField, TimeField

from .models import Agenda
from medicos.serializers import MedicoSerializer


class AgendaSerializer(ModelSerializer):
    medico = MedicoSerializer(read_only=True)
    horarios = ListField(child=TimeField(format='%H:%M'))

    class Meta:
        model = Agenda
        fields = ('id', 'medico', 'dia', 'horarios')
