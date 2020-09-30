from rest_framework import mixins, viewsets, filters
from rest_framework.permissions import IsAuthenticated

from especialidades.models import Especialidade
from especialidades.serializers import EspecialidadeSerializer


class EspecialidadesViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Especialidade.objects.all()
    serializer_class = EspecialidadeSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ['nome']
    filter_backends = (filters.SearchFilter,)
