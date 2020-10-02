from django.core.exceptions import ValidationError

from datetime import date


def validador_dia(dia):
    if dia < date.today():
        raise ValidationError("Data passada não permitida")
