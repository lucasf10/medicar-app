from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from django.urls import reverse

from .models import Usuario

class TestUsuariosAPI(APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.client = APIClient()
        cls.usuario_existente_data = {
            'email': 'teste_existente@mail.com',
            'password': '88888888',
            'nome': 'Teste'
        }
        cls.usuario_existente = Usuario.objects.create_user(**cls.usuario_existente_data)

    def test_criar_usuario(self):
        data = {
            'email': 'teste@email.com',
            'nome': 'Teste',
            'password': '9999999'
        }
        url = reverse('criar_usuario')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIsNotNone(response.data.get('token', None))
        
        usuario_criado_data = response.data.get('usuario', None)
        self.assertIsNotNone(usuario_criado_data)
        self.assertEqual(usuario_criado_data.get('email'), data.get('email'))
        self.assertEqual(usuario_criado_data.get('nome'), data.get('nome'))

        self.assertTrue(
            Usuario.objects.filter(email=data.get('email'), nome=data.get('nome')).exists(),
        )

    def test_criar_usuario_existente(self):
        url = reverse('criar_usuario')
        response = self.client.post(url, self.usuario_existente_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_login(self):
        url = reverse('autenticar_usuario')
        response = self.client.post(url, self.usuario_existente_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsNotNone(response.data.get('token', None))
        self.assertIsNotNone(response.data.get('usuario', None))

    def test_login_senha_errada(self):
        url = reverse('autenticar_usuario')
        self.usuario_existente_data.update({'password': '11111111'})
        response = self.client.post(url, self.usuario_existente_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
