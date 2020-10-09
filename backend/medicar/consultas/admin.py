from django.contrib import admin

from .models import Consulta


class ConsultaAdmin(admin.ModelAdmin):
    model = Consulta
    list_display = ('id', 'paciente', 'medico', 'dia_horario')

admin.site.register(Consulta, ConsultaAdmin)
