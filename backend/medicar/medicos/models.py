from django.db import models

from especialidades.models import Especialidade


class Medico(models.Model):

    nome = models.CharField(max_length=100, null=False, blank=False)
    crm = models.CharField(unique=True, max_length=20, null=False, blank=False)
    email = models.EmailField(unique=True, null=True, blank=True)
    telefone = models.CharField(max_length=12, null=True, blank=True)
    especialidade = models.ForeignKey(
        Especialidade,
        on_delete=models.SET_NULL,
        related_name='medicos',
        null=True,
        blank=True
    )

    def __str__(self):
        return '{} ({})'.format(self.nome, self.crm)
