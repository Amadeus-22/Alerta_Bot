# Alerta_Bot
# 🌤️ Clima Alerta com Django + Telegram

Este projeto monitora a temperatura de uma localidade, registra em banco de dados e envia alertas via Telegram quando os limites são ultrapassados.

---

## 📌 Funcionalidades

- Consulta periódica da API [open-meteo.com](https://open-meteo.com/)
- Armazenamento de dados em banco SQLite
- Geração de alertas com limites de temperatura
- Notificações em tempo real via bot do Telegram
- Logs detalhados dos alertas
- Testes automatizados com pytest
- Painel django automatizado

---


---

## 🚀 Como rodar o projeto

```bash
# Acesse a pasta do projeto
cd clima_alerta

# Ative o ambiente virtual
.\venv\Scripts\activate

# Instale as dependências
pip install -r requirements.txt

# Rode o serviço de verificação + bot
python alertas/servico_alerta.py
