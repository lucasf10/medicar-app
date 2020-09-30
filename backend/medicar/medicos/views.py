from rest_framework import mixins, viewsets, filters
from rest_framework.permissions import IsAuthenticated

from .models import Medico
from .serializers import MedicoSerializer


class MedicosViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ['nome']
    filter_backends = (filters.SearchFilter,)
