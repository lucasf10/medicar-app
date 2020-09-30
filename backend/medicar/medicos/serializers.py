from rest_framework.serializers import ModelSerializer

from .models import Medico
from especialidades.serializers import EspecialidadeSerializer


class MedicoSerializer(ModelSerializer):
    especialidade = EspecialidadeSerializer(read_only=True)

    class Meta:
        model = Medico
        fields = ('id', 'crm', 'nome', 'especialidade')
