from datetime import datetime, timedelta, date
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from django.urls import reverse

from .models import Agenda
from usuarios.models import Usuario
from especialidades.models import Especialidade
from medicos.models import Medico

class TestAgendasAPI(APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.client = APIClient()
        cls.usuario_existente_data = {
            'email': 'teste_existente@mail.com',
            'password': '88888888',
            'nome': 'Teste'
        }
        cls.usuario_existente = Usuario.objects.create_user(**cls.usuario_existente_data)
        cls.url = reverse('agenda-list')
        cls.criar_agendas()

    @classmethod
    def criar_agendas(cls):
        esp1 = Especialidade.objects.create(nome='Pediatria')
        esp2 = Especialidade.objects.create(nome='Cardiologia')

        med1 = Medico.objects.create(nome='Medico 1', crm='3333', especialidade=esp1)
        med2 = Medico.objects.create(nome='Medico 2', crm='4444', especialidade=esp2)

        agenda_1 = Agenda.objects.create(
            medico=med1,
            dia=date.today() + timedelta(days=1),
            horarios=['14:00', '15:00', '16:00']
        )
        agenda_2 = Agenda.objects.create(
            medico=med2,
            dia=date.today() + timedelta(days=2),
            horarios=['12:00', '16:00', '18:00']
        )

        cls.id_pediatria = esp1.id
        cls.id_cardiologia = esp2.id

        cls.id_medico_1 = med1.id
        cls.id_medico_2 = med2.id

        cls.id_agenda_1 = agenda_1.id
        cls.id_agenda_2 = agenda_2.id

    def test_nao_autorizado(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def get_dados_esperados_completo(self):

        return [
            {
                'id': self.id_agenda_1,
                'medico':{'id': self.id_medico_1, 'crm': '3333', 'nome': 'Medico 1', 'especialidade': {'id': self.id_pediatria, 'nome': 'Pediatria'}},
                'dia': str(date.today() + timedelta(days=1)),
                'horarios': ['14:00', '15:00', '16:00']
            },
            {
                'id': self.id_agenda_2,
                'medico':{'id': self.id_medico_2, 'crm': '4444', 'nome': 'Medico 2', 'especialidade': {'id': self.id_cardiologia, 'nome': 'Cardiologia'}},
                'dia': str(date.today() + timedelta(days=2)),
                'horarios': ['12:00', '16:00', '18:00']
            }
        ]

    def get_dados_esperados_minimo(self):
        return [
            {
                'id': self.id_agenda_1,
                'medico':{'id': self.id_medico_1, 'crm': '3333', 'nome': 'Medico 1', 'especialidade': {'id': self.id_pediatria, 'nome': 'Pediatria'}},
                'dia': str(date.today() + timedelta(days=1)),
                'horarios': ['14:00', '15:00', '16:00']
            },
        ]

    def test_listar_agendas(self):
        dados_esperados = self.get_dados_esperados_completo()

        self.client.login(email='teste_existente@mail.com', password='88888888')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, dados_esperados)

    def test_listar_agendas_filtro_medico(self):
        dados_esperados_completo = self.get_dados_esperados_completo()
        dados_esperados_minimo = self.get_dados_esperados_minimo()

        self.client.login(email='teste_existente@mail.com', password='88888888')
        
        response = self.client.get(self.url+'?medico='+str(self.id_medico_1))
        self.assertEqual(response.data, dados_esperados_minimo)

        response = self.client.get(self.url+'?medico='+str(self.id_medico_2)+'&medico='+str(self.id_medico_1))
        self.assertEqual(response.data, dados_esperados_completo)

        response = self.client.get(self.url+'?medico='+str(self.id_medico_2+1))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_listar_agendas_filtro_especialidade(self):
        dados_esperados_completo = self.get_dados_esperados_completo()
        dados_esperados_minimo = self.get_dados_esperados_minimo()

        self.client.login(email='teste_existente@mail.com', password='88888888')

        response = self.client.get(self.url+'?especialidade='+str(self.id_pediatria))
        self.assertEqual(response.data, dados_esperados_minimo)

        response = self.client.get(self.url+'?especialidade='+str(self.id_pediatria)+'&especialidade='+str(self.id_cardiologia))
        dados_esperados_completo = sorted(dados_esperados_completo, key=lambda dado: dado['id'], reverse=True)
        self.assertEqual(response.data, dados_esperados_completo)

        response = self.client.get(self.url+'?especialidade='+str(self.id_cardiologia+1))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    
    def test_listar_agendas_filtro_data(self):
        dados_esperados_completo = self.get_dados_esperados_completo()
        dados_esperados_minimo = self.get_dados_esperados_minimo()

        self.client.login(email='teste_existente@mail.com', password='88888888')

        response = self.client.get(self.url+'?data_inicio='+str(date.today() + timedelta(days=3)))
        self.assertEqual(response.data, [])

        response = self.client.get(self.url+'?data_inicio='+str(date.today() + timedelta(days=1)))
        self.assertEqual(response.data, dados_esperados_completo)

        response = self.client.get(self.url+'?data_final='+str(date.today()))
        self.assertEqual(response.data, [])

        response = self.client.get(self.url+'?data_final='+str(date.today() + timedelta(days=1)))
        self.assertEqual(response.data, dados_esperados_minimo)

        response = self.client.get(self.url+'?data_final='+str(date.today() + timedelta(days=3)))
        self.assertEqual(response.data, dados_esperados_completo)

        response = self.client.get(
            self.url+'?data_final='+str(date.today() + timedelta(days=1))+'&data_inicio='+str(date.today() + timedelta(days=1))
        )
        self.assertEqual(response.data, dados_esperados_minimo)

        response = self.client.get(
            self.url+'?data_final='+str(date.today() + timedelta(days=3))+'&data_inicio='+str(date.today() + timedelta(days=1))
        )
        self.assertEqual(response.data, dados_esperados_completo)

        response = self.client.get(
            self.url+'?data_final='+str(date.today() + timedelta(days=4))+'&data_inicio='+str(date.today() + timedelta(days=3))
        )
        self.assertEqual(response.data, [])
