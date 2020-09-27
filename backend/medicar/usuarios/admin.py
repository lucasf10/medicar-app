from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from usuarios.models import Usuario


class UsuarioAdmin (UserAdmin):
    model = Usuario
    list_display = ('nome', 'email', 'is_staff')
    search_fields = ('nome', 'email')
    ordering = ('nome', 'email',)
    filter_horizontal = ()
    list_filter = ('is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('nome', 'email', 'password')}),
        ('Permissões', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff')}
        ),
    )


admin.site.register(Usuario, UsuarioAdmin)
admin.site.unregister(Group)