from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone

from .managers import UsuarioManager

class Usuario(AbstractBaseUser, PermissionsMixin):

    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    data_criacao = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome']
    
    objects = UsuarioManager()

    def __str__(self):
        return '{} ({})'.format(self.nome, self.email)