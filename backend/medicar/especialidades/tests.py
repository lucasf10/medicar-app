from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from django.urls import reverse

from .models import Especialidade
from usuarios.models import Usuario

class TestEspecialidadesAPI(APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.client = APIClient()
        cls.usuario_existente_data = {
            'email': 'teste_existente@mail.com',
            'password': '88888888',
            'nome': 'Teste'
        }
        cls.usuario_existente = Usuario.objects.create_user(**cls.usuario_existente_data)
        cls.url = reverse('especialidade-list')
        cls.criar_especialidades()

    @classmethod
    def criar_especialidades(cls):
        esp1 = Especialidade.objects.create(nome='Pediatria')
        esp2 = Especialidade.objects.create(nome='Cardiologia')

        cls.id_pediatria = esp1.id
        cls.id_cardiologia = esp2.id

    def test_nao_autorizado(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_listar_especialidades(self):
        dados_esperados = [
            {'id': self.id_pediatria, 'nome':'Pediatria'},
            {'id': self.id_cardiologia, 'nome':'Cardiologia'}
        ]
        
        self.client.login(email='teste_existente@mail.com', password='88888888')
        
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, dados_esperados)

    def test_listar_especialidades_busca(self):
        dados_esperados = [
            {'id': self.id_pediatria, 'nome':'Pediatria'},
        ]
        
        self.client.login(email='teste_existente@mail.com', password='88888888')
        
        response = self.client.get(self.url+'?search=ped')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, dados_esperados)

        response = self.client.get(self.url+'?search=pra')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [])
