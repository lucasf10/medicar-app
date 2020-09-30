from django.contrib import admin

from .models import Medico


class MedicoAdmin(admin.ModelAdmin):
    model = Medico
    list_display = ('id', 'nome', 'crm', 'email', 'telefone', 'especialidade')
    search_fields = ('nome', 'crm', 'especialidade', 'email')
    ordering = ('nome', 'especialidade', 'crm')

admin.site.register(Medico, MedicoAdmin)
