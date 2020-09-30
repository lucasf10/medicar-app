from rest_framework.serializers import ModelSerializer

from .models import Especialidade


class EspecialidadeSerializer(ModelSerializer):

    class Meta:
        model = Especialidade
        fields = ('id', 'nome')
