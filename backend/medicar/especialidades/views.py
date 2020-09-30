from rest_framework import mixins, viewsets, filters
from rest_framework.permissions import IsAuthenticated

from .models import Especialidade
from .serializers import EspecialidadeSerializer


class EspecialidadesViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Especialidade.objects.all()
    serializer_class = EspecialidadeSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ['nome']
    filter_backends = (filters.SearchFilter,)
