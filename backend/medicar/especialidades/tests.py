from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from django.urls import reverse

from .models import Especialidade
from usuarios.models import Usuario

class TestEspecialidadesAPI(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.usuario_existente_data = {
            'email': 'teste_existente@mail.com',
            'password': '88888888',
            'nome': 'Teste'
        }
        self.usuario_existente = Usuario.objects.create_user(**self.usuario_existente_data)
        self.url = reverse('especialidade-list')
        self.criar_especialidades()

    def criar_especialidades(self):
        Especialidade.objects.create(nome='Pediatria')
        Especialidade.objects.create(nome='Cardiologia')

    def test_nao_autorizado(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_listar_especialidades(self):
        dados_esperados = [
            {'id': 1, 'nome':'Pediatria'},
            {'id': 2, 'nome':'Cardiologia'}
        ]
        
        self.client.login(email='teste_existente@mail.com', password='88888888')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, dados_esperados)
