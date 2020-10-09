from django.db import models
from django.contrib.postgres.fields import ArrayField

from medicos.models import Medico
from .validators import validador_dia


class Agenda(models.Model):

    dia = models.DateField(
        validators=[validador_dia],
        null=False,
        blank=False
    )
    medico = models.ForeignKey(
        Medico,
        on_delete=models.CASCADE,
        related_name='agendas',
        null=False,
        blank=False
    )
    horarios = ArrayField(
        models.TimeField(),
        null=False,
        blank=False,
        help_text="Ex: 14:00,15:00,16:00"
    )

    def __str__(self):
        return '{} ({})'.format(self.medico.nome, self.dia)
