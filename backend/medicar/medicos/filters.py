from django_filters.rest_framework import FilterSet, ModelMultipleChoiceFilter

from .models import Medico
from especialidades.models import Especialidade


class MedicosFilter(FilterSet):
    especialidade = ModelMultipleChoiceFilter(queryset=Especialidade.objects.all())

    class Meta:
        model = Medico
        fields = ['especialidade']
