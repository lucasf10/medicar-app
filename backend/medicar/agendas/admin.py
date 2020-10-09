from django.contrib import admin

from .models import Agenda


class AgendaAdmin(admin.ModelAdmin):
    model = Agenda
    list_display = ('id', 'medico', 'dia', 'horarios')
    search_fields = ('medico__nome', 'dia')
    ordering = ('medico', 'dia')

admin.site.register(Agenda, AgendaAdmin)
