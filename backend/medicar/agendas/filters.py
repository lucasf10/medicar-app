from django_filters.rest_framework import FilterSet, ModelMultipleChoiceFilter, DateFilter

from .models import Agenda
from especialidades.models import Especialidade
from medicos.models import Medico


class AgendasFilter(FilterSet):
    especialidade = ModelMultipleChoiceFilter(
        field_name='medico__especialidade',
        label="Especialidade do médico",
        queryset=Especialidade.objects.all()
    )
    medico = ModelMultipleChoiceFilter(queryset=Medico.objects.all())
    data_final = DateFilter(field_name='dia',lookup_expr=('lte'),) 
    data_inicio = DateFilter(field_name='dia',lookup_expr=('gte'))

    class Meta:
        model = Agenda
        fields = ['especialidade', 'medico', 'data_inicio', 'data_final']
