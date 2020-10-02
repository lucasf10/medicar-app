from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from .models import Agenda
from .serializers import AgendaSerializer
from .filters import AgendasFilter


class AgendasViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Agenda.objects.all()
    serializer_class = AgendaSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filter_class = AgendasFilter
