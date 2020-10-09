# Medicar - Desafio Intmed

Desafio para a vaga de desenvolvedor Fullstack da Intmed.

## Como Rodar a API (Backend)
  0. Tenha certeza de que o python 3 está instalado na máquina.
  1. Clone o repositório: `git clone https://github.com/LucasGabrielSI/desafio-medicar-intmed.git`
  2. Navegue até a raiz de onde o repositório foi clonado e entre na pasta backend: `cd backend`
  3. Crie um ambiente virtual: `python3 -m venv <nome_venv>`
  4. Ative um ambiente virtual: `. <nome_venv>/bin/activate` ou `source <nome_venv>/bin/activate`
  5. Instale as dependências: `pip3 install -r requirements.txt`
  6. Crie um banco de dados no postgresql e insira as informações no settings.py, ou sete as variáveis globais no sistema:
    - DB_NAME: Nome do Banco de Dados
    - DB_USER: Nome do Usuário do Banco de Dados
    - DB_PASSWORD: Senha do Usuário do Banco de Dados
    - DB_HOST: Endereço de onde está hospedado (se for local, deixar localhost)
    - DB_PORT: Porta do endereço onde está hospedado (se for a padrão, deixar vazia)
```
# settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('DB_NAME', ''),
        'USER': os.environ.get('DB_USER', ''),
        'PASSWORD': os.environ.get('DB_PASSWORD', ''),
        'HOST': os.environ.get('DB_HOST', ''),
        'PORT': os.environ.get('DB_PORT', ''),
    }
}
```
  7. Rode as migrações: `./manage.py migrate`
  8. Inicie o servidos: `./manage.py runserver`
  9. Para criar um super usuário, e conseguir acessar o painel administrativo (http://localhost:8000/admin/): `./manage.py createsuperuser`

## Como Rodar o Client (Frontend):
  0. Tenha certeza que o node e o npm estão instalados em sua máquina.
  1. Supondo que o repositório já tenha sido clonado para rodar a API, volte até a raiz, e navegue até a pasta frontend: `cd frontend`
  2. Instale o projeto: `npm install`
  3. Rode o projeto: `npm run`
  4. Acesse: `https://localhost:4200`
