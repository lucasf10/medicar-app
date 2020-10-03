import json
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from django.urls import reverse

from .models import Medico
from usuarios.models import Usuario
from especialidades.models import Especialidade

class TestMedicosAPI(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.usuario_existente_data = {
            'email': 'teste_existente@mail.com',
            'password': '88888888',
            'nome': 'Teste'
        }
        self.usuario_existente = Usuario.objects.create_user(**self.usuario_existente_data)
        self.url = reverse('medico-list')
        self.criar_medicos()
    
    def criar_medicos(self):
        esp1 = Especialidade.objects.create(nome='Pediatria')
        esp2 = Especialidade.objects.create(nome='Cardiologia')

        Medico.objects.create(
            nome='Medico 1',
            crm='1234',
            especialidade=esp1
        )
        Medico.objects.create(
            nome='Medico 2',
            crm='4567',
            especialidade=esp2
        )

    def test_nao_autorizado(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_listar_medicos(self):
        dados_esperados = [
            {'id': 1, 'crm': '1234', 'nome':'Medico 1', 'especialidade': {'id': 1, 'nome': 'Pediatria'}},
            {'id': 2, 'crm': '4567', 'nome':'Medico 2', 'especialidade': {'id': 2, 'nome': 'Cardiologia'}},
        ]
        
        self.client.login(email='teste_existente@mail.com', password='88888888')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, dados_esperados)
