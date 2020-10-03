from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from django.urls import reverse

from .models import Medico
from usuarios.models import Usuario
from especialidades.models import Especialidade

class TestMedicosAPI(APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.client = APIClient()
        cls.usuario_existente_data = {
            'email': 'teste_existente@mail.com',
            'password': '88888888',
            'nome': 'Teste'
        }
        cls.usuario_existente = Usuario.objects.create_user(**cls.usuario_existente_data)
        cls.url = reverse('medico-list')
        cls.criar_medicos()
    
    @classmethod
    def criar_medicos(cls):
        Medico.objects.create(
            nome='Medico Teste',
            crm='1234',
            especialidade=Especialidade.objects.create(nome='Pediatria')
        )
        Medico.objects.create(
            nome='Outro Medico',
            crm='4567',
            especialidade=Especialidade.objects.create(nome='Cardiologia')
        )

    def get_dados_esperados_completo(self):
        return [
            {'id': 1, 'crm': '1234', 'nome': 'Medico Teste', 'especialidade': {'id': 1, 'nome': 'Pediatria'}},
            {'id': 2, 'crm': '4567', 'nome': 'Outro Medico', 'especialidade': {'id': 2, 'nome': 'Cardiologia'}},
        ]

    def get_dados_esperados_minimo(self):
        return [
            {'id': 2, 'crm': '4567', 'nome': 'Outro Medico', 'especialidade': {'id': 2, 'nome': 'Cardiologia'}},
        ]

    def test_nao_autorizado(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_listar_medicos(self):
        dados_esperados = self.get_dados_esperados_completo()
        
        self.client.login(email='teste_existente@mail.com', password='88888888')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, dados_esperados)

    def test_listar_medicos_busca(self):
        dados_esperados_minimo = self.get_dados_esperados_minimo()
        dados_esperados_completo = self.get_dados_esperados_completo()
        
        self.client.login(email='teste_existente@mail.com', password='88888888')
        
        response = self.client.get(self.url+'?search=outro')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, dados_esperados_minimo)

        response = self.client.get(self.url+'?search=pra')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [])

        response = self.client.get(self.url+'?search=medico')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, dados_esperados_completo)

    def test_listar_medicos_filtro_especialidade(self):
        dados_esperados_minimo = self.get_dados_esperados_minimo()
        dados_esperados_completo = self.get_dados_esperados_completo()
        
        self.client.login(email='teste_existente@mail.com', password='88888888')
        
        response = self.client.get(self.url+'?especialidade=2')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, dados_esperados_minimo)

        response = self.client.get(self.url+'?especialidade=3')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        response = self.client.get(self.url+'?especialidade=1&especialidade=2')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, dados_esperados_completo)
