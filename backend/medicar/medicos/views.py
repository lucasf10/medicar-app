from rest_framework import mixins, viewsets
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from .models import Medico
from .serializers import MedicoSerializer
from .filters import MedicosFilter


class MedicosViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ['nome']
    filter_backends = [SearchFilter, DjangoFilterBackend]
    filter_class = MedicosFilter
