from django.contrib import admin

from .models import Especialidade


class EspecialidadeAdmin(admin.ModelAdmin):
    model = Especialidade
    list_display = ('id', 'nome')
    # search_fields = ('nome', )
    # ordering = ('nome', )

admin.site.register(Especialidade, EspecialidadeAdmin)
