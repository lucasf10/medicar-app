from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from .models import Usuario
from .serializers import UsuarioSerializer


class UsuarioCreate(CreateAPIView):
    model = Usuario
    permission_classes = [AllowAny]
    serializer_class = UsuarioSerializer
    queryset = Usuario.objects.all()

    def create(self, request, *args, **kwargs):
        email = request.data.get('email', None)
        nome = request.data.get('nome', None)
        password = request.data.get('password', None)

        if not email or not nome or not password:
            return Response(
                {'mensagem': 'Existem dados não informados.'},
                status=status.HTTP_400_BAD_REQUEST
            )
        elif not Usuario.objects.filter(email=email).exists():
            usuario_serializado = UsuarioSerializer(data=request.data)
            
            if usuario_serializado.is_valid():
                usuario = Usuario.objects.create_user(
                    nome=nome,
                    email=email,
                    password=password
                )

                token = Token.objects.create(user=usuario)

                return Response(
                    {
                        'mensagem': 'Usuário cadastrado.',
                        'usuario': usuario_serializado.data,
                        'token': token.key
                    },
                    status=status.HTTP_201_CREATED
                )
            else:
                return Response(
                    {'mensagem': usuario_serializado.errors},
                    status=status.HTTP_400_BAD_REQUEST
                )
        else:
            return Response(
                {'mensagem': 'Este e-mail já está sendo utilizado.'},
                status=status.HTTP_400_BAD_REQUEST
            )


class UsuarioLogin(CreateAPIView):
    model = Usuario
    permission_classes = [AllowAny]
    serializer_class = UsuarioSerializer
    queryset = Usuario.objects.all()

    def create(self, request, *args, **kwargs):
        email = request.data.get('email', None)
        password = request.data.get('password', None)

        if not email or not password:
            return Response(
                {'mensagem': 'Existem dados não informados.'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        usuario = authenticate(email=email, password=password)

        if not usuario:
            return Response(
                {'mensagem': 'Dados inválidos. Tenta novamente.'},
                status=status.HTTP_400_BAD_REQUEST
            )
        else:
            usuario_serializado = UsuarioSerializer(usuario)
            token, _ = Token.objects.get_or_create(user=usuario)

            return Response(
                {
                    'usuario': usuario_serializado.data,
                    'token': token.key
                },
                status=status.HTTP_200_OK
            )
