# 🌡️ Alerta_Bot – Monitoramento de Temperatura com Django + Telegram

Este projeto foi desenvolvido como parte de um desafio técnico com o objetivo de:

- Consultar a temperatura atual de uma localidade via API pública.
- Armazenar esses dados em um banco de dados (SQLite).
- Verificar se a temperatura ultrapassa um limite configurável.
- Registrar um alerta em caso de excesso de temperatura.
- Enviar uma notificação via Telegram.

---

## 🚀 Tecnologias Utilizadas

- Python 3.10+
- Django 4.x
- SQLite (banco padrão do Django)
- API pública de Clima 
- Bot do Telegram

---

## 📁 Estrutura do Projeto

Alerta_Bot/
├── alertas/ # App Django para alertas e clima
│ ├── models.py # Modelos: Clima, Alerta
│ ├── bot.py # Código do bot Telegram
│ ├── utils.py # Funções auxiliares (chamada API, etc)
├── clima_alerta/ # Configuração principal Django
├── db.sqlite3
├── manage.py

yaml
Copiar
Editar

---

## ⚙️ Como Rodar o Projeto

### 1. Clone o repositório

```bash
git clone https://github.com/Amadeus-22/Alerta_Bot.git
cd Alerta_Bot
2. Crie um ambiente virtual e ative-o
bash
Copiar
Editar
python -m venv venv
venv\Scripts\activate       # No Windows
# ou
source venv/bin/activate   # No Linux/Mac
3. Instale as dependências
bash
Copiar
Editar
pip install -r requirements.txt
4. Rode as migrações do banco de dados
bash
Copiar
Editar
python manage.py migrate
5. (Opcional) Crie um superusuário para o Django Admin
bash
Copiar
Editar
python manage.py createsuperuser
🌡️ Como Configurar o Alerta de Temperatura
No arquivo alertas/bot.py, altere o valor do limite de temperatura se quiser mudar o padrão (ex: 30°C):

python
Copiar
Editar
LIMITE_TEMPERATURA = 30
Você também pode configurar a cidade desejada e o ID do chat do Telegram.

python
Copiar
Editar
LOCALIZACAO = {'latitude': -23.55, 'longitude': -46.63}  # Exemplo: São Paulo
TELEGRAM_CHAT_ID = 'SEU_CHAT_ID'
TELEGRAM_TOKEN = 'SEU_TOKEN_DO_BOT'
🤖 Como Rodar o Bot (Verificação e Notificação)
bash
Copiar
Editar
python alertas/bot.py
Esse script irá:

Consultar a API de clima.

Armazenar a temperatura no banco.

Verificar se ultrapassa o limite.

Se ultrapassado, registrar alerta e enviar notificação no Telegram.

🧪 Como Testar Manualmente (Simular)
Testar no terminal (simular temperatura)
Você pode modificar manualmente a função que pega a temperatura em utils.py para forçar um valor alto e simular o alerta.

Exemplo:

python
Copiar
Editar
def obter_temperatura():
    return 35.0  # Simula alta temperatura
Depois, execute novamente:

bash
Copiar
Editar
python alertas/bot.py
Você deve ver a mensagem enviada no Telegram e um alerta salvo no banco.
