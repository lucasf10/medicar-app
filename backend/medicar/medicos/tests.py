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
        esp1 = Especialidade.objects.create(nome='Pediatria')
        esp2 = Especialidade.objects.create(nome='Cardiologia')

        med1 = Medico.objects.create(
            nome='Medico Teste',
            crm='1111',
            especialidade=esp1
        )
        med2 = Medico.objects.create(
            nome='Outro Medico',
            crm='2222',
            especialidade=esp2
        )

        cls.id_pediatria = esp1.id
        cls.id_cardiologia = esp2.id
        cls.id_med1 = med1.id
        cls.id_med2 = med2.id

    def get_dados_esperados_completo(self):

        return [
            {'id': self.id_med1, 'crm': '1111', 'nome': 'Medico Teste', 'especialidade': {'id': self.id_pediatria, 'nome': 'Pediatria'}},
            {'id': self.id_med2, 'crm': '2222', 'nome': 'Outro Medico', 'especialidade': {'id': self.id_cardiologia, 'nome': 'Cardiologia'}},
        ]

    def get_dados_esperados_minimo(self):

        return [
            {'id': self.id_med2, 'crm': '2222', 'nome': 'Outro Medico', 'especialidade': {'id': self.id_cardiologia, 'nome': 'Cardiologia'}},
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
        
        response = self.client.get(self.url+'?especialidade='+str(self.id_cardiologia))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, dados_esperados_minimo)

        response = self.client.get(self.url+'?especialidade='+str(self.id_cardiologia+1))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        response = self.client.get(self.url+'?especialidade='+str(self.id_cardiologia)+'&especialidade='+str(self.id_pediatria))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, dados_esperados_completo)
