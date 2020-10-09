from django.db import models
from django.contrib.postgres.fields import ArrayField

from medicos.models import Medico
from usuarios.models import Usuario


class Consulta(models.Model):

    data_agendamento = models.DateTimeField(auto_now_add=True)
    dia_horario = models.DateTimeField(null=False, blank=False)
    medico = models.ForeignKey(
        Medico,
        on_delete=models.CASCADE,
        related_name='consultas',
        null=False,
        blank=False
    )
    paciente = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        related_name='consultas',
        null=False,
        blank=False
    )

    def __str__(self):
        return 'Consulta de {} com {} ({}T{})'.format(
            self.paciente,
            self.medico.nome,
            self.dia_horario.date,
            self.dia_horario.time
        )
