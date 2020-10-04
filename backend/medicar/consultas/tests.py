from datetime import datetime, timedelta, date
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from django.urls import reverse
from django.utils.timezone import make_aware, now

from .models import Consulta
from usuarios.models import Usuario
from especialidades.models import Especialidade
from medicos.models import Medico
from agendas.models import Agenda

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
        cls.url_list = reverse('consulta-list')
        cls.criar_consultas()

    @classmethod
    def criar_consultas(cls):
        cls.outro_usuario_data = {
            'email': 'outro_user@mail.com',
            'password': '999999',
            'nome': 'Teste 2'
        }
        cls.outro_usuario = Usuario.objects.create_user(**cls.outro_usuario_data)

        esp = Especialidade.objects.create(nome='Pediatria')
        med = Medico.objects.create(nome='Medico 1', crm='1010', especialidade=esp)

        agenda = Agenda.objects.create(
            medico=med,
            dia=date.today() + timedelta(days=1),
            horarios=['14:00', '15:00', '16:00']
        )

        data_hora_0 = datetime.strptime('{}T14:00'.format(date.today() - timedelta(days=2)), '%Y-%m-%dT%H:%M')
        data_hora_1 = datetime.strptime('{}T14:00'.format(date.today() + timedelta(days=1)), '%Y-%m-%dT%H:%M')
        data_hora_2 = datetime.strptime('{}T16:00'.format(date.today() + timedelta(days=1)), '%Y-%m-%dT%H:%M')

        consulta_1 = Consulta.objects.create(
            medico=med,
            paciente=cls.usuario_existente,
            dia_horario=make_aware(data_hora_0),
        )
        consulta_2 = Consulta.objects.create(
            medico=med,
            paciente=cls.usuario_existente,
            dia_horario=make_aware(data_hora_1),
        )
        consulta_3 = Consulta.objects.create(
            medico=med,
            paciente=cls.outro_usuario,
            dia_horario=make_aware(data_hora_2),
        )

        cls.id_pediatria = esp.id
        cls.id_medico = med.id
        cls.id_agenda = agenda.id
        cls.id_consulta_1 = consulta_1.id
        cls.id_consulta_2 = consulta_2.id
        cls.id_consulta_3 = consulta_3.id

    def test_nao_autorizado(self):
        response = self.client.get(self.url_list)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        response = self.client.delete(reverse('consulta-detail', kwargs={'pk': self.id_consulta_1}))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_criar_consulta(self):
        dados_esperados = {
            'id': self.id_consulta_3 + 1,
            'dia': str(date.today() + timedelta(days=1)),
            'horario': '15:00',
            'medico': {
                'id': self.id_medico,
                'crm': '1010',
                'nome': 'Medico 1', 
                'especialidade': {
                    'id': self.id_pediatria,
                    'nome': 'Pediatria'
                }
            }
        }
        self.client.login(email='teste_existente@mail.com', password='88888888')

        response = self.client.post(self.url_list, data={'agenda_id': self.id_agenda, 'horario': '15:00'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response.data.pop('data_agendamento')
        self.assertEqual(response.data, dados_esperados)

        response = self.client.post(self.url_list, data={'agenda_id': self.id_agenda, 'horario': '15:00'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_consulta(self):
        self.client.login(email='teste_existente@mail.com', password='88888888')

        response = self.client.delete(reverse('consulta-detail', kwargs={'pk': 999}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        response = self.client.delete(reverse('consulta-detail', kwargs={'pk': self.id_consulta_3}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        response = self.client.delete(reverse('consulta-detail', kwargs={'pk': self.id_consulta_1}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        horario_4 = datetime.strptime('{}T16:00'.format(date.today() + timedelta(days=2)), '%Y-%m-%dT%H:%M')
        consulta_4 = Consulta.objects.create(
            medico_id=self.id_medico,
            paciente=self.usuario_existente,
            dia_horario=make_aware(horario_4)
        )
        response = self.client.delete(reverse('consulta-detail', kwargs={'pk': consulta_4.id}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_list_consulta(self):
        self.client.login(email='teste_existente@mail.com', password='88888888')
        dados_esperados = [{
            'id': self.id_consulta_2,
            'dia': str(date.today() + timedelta(days=1)),
            'horario': '14:00',
            'medico': {
                'id': self.id_medico,
                'crm': '1010',
                'nome': 'Medico 1', 
                'especialidade': {
                    'id': self.id_pediatria,
                    'nome': 'Pediatria'
                }
            }
        }]
        response = self.client.get(self.url_list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response.data[0].pop('data_agendamento')
        self.assertEqual(response.data, dados_esperados)
