from rest_framework.serializers import ModelSerializer, ReadOnlyField

from .models import Usuario


class UsuarioSerializer(ModelSerializer):

    class Meta:
        model = Usuario
        fields = ('nome', 'email', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }
