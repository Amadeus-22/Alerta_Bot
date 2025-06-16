import os
import sys
import django
import time
import requests
import threading
import asyncio
from telegram import Bot, Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from datetime import datetime

# Configuração do Django (ajuste conforme seu projeto)
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # raiz do projeto
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'clima_alerta.settings')
django.setup()

from alertas.models import Temperatura, Alerta, LogAlerta

# Configurações do projeto
API_URL = "https://api.open-meteo.com/v1/forecast?latitude=-23.55&longitude=-46.63&daily=temperature_2m_max,temperature_2m_min&timezone=auto"
TEMPERATURA_MAXIMA_LIMITE = 30.0
TEMPERATURA_MINIMA_LIMITE = 10.0
INTERVALO_MINUTOS = 30
TELEGRAM_TOKEN = "7985056340:AAH2i9UgsJZjnwuMicozNN2HNZb0EQtKBbA"
CHAT_ID = "7985056340"

bot = Bot(token=TELEGRAM_TOKEN)

def consultar_temperaturas():
    try:
        resp = requests.get(API_URL)
        dados = resp.json()
        temp_max = dados['daily']['temperature_2m_max'][0]
        temp_min = dados['daily']['temperature_2m_min'][0]
        return temp_max, temp_min
    except Exception as e:
        print("Erro na consulta da API:", e)
        return None, None

def enviar_alerta(msg):
    try:
        bot.send_message(chat_id=CHAT_ID, text=msg)
        print("✅ Alerta enviado.")
    except Exception as e:
        print("❌ Erro ao enviar alerta:", e)

# Comandos do Telegram
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🌤️ Olá! Estou monitorando a temperatura.")

async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    temp_max, temp_min = consultar_temperaturas()
    if temp_max is not None and temp_min is not None:
        msg = f"🌡️ Temperaturas previstas para hoje:\nMáxima: {temp_max}°C\nMínima: {temp_min}°C"
    else:
        msg = "❌ Não consegui obter os dados do clima agora."
    await update.message.reply_text(msg)

def registrar_log(tipo, temperatura, mensagem):
    LogAlerta.objects.create(tipo=tipo, temperatura=temperatura, mensagem=mensagem)

def verificar_e_registrar_alertas():
    while True:
        temp_max, temp_min = consultar_temperaturas()
        if temp_max is not None and temp_min is not None:
            # Salva as temperaturas no banco (aparecerá no admin)
            Temperatura.objects.create(valor=temp_max)
            Temperatura.objects.create(valor=temp_min)
            print(f"🌡️ Temperaturas registradas no banco: Máx {temp_max}°C, Mín {temp_min}°C")

            # Verifica limites máximos e mínimos para gerar alertas
            if temp_max > TEMPERATURA_MAXIMA_LIMITE:
                msg = f"🔥 Alerta! Temperatura MÁXIMA prevista: {temp_max}°C em {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}"
                Alerta.objects.create(temperatura=temp_max, mensagem=msg)
                registrar_log("Máxima", temp_max, msg)
                enviar_alerta(msg)

            if temp_min < TEMPERATURA_MINIMA_LIMITE:
                msg = f"❄️ Alerta! Temperatura MÍNIMA prevista: {temp_min}°C em {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}"
                Alerta.objects.create(temperatura=temp_min, mensagem=msg)
                registrar_log("Mínima", temp_min, msg)
                enviar_alerta(msg)
        else:
            print("Não foi possível consultar a API.")

        time.sleep(INTERVALO_MINUTOS * 60)

async def iniciar_bot_telegram():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("status", status))
    print("🤖 Bot ouvindo comandos no Telegram...")
    await app.initialize()
    await app.start()
    await app.updater.start_polling()
    await asyncio.Event().wait()

if __name__ == "__main__":
    # Executa a verificação de alertas em thread separada
    threading.Thread(target=verificar_e_registrar_alertas, daemon=True).start()

    # Executa o bot Telegram no loop principal de asyncio
    loop = asyncio.get_event_loop()
    loop.create_task(iniciar_bot_telegram())
    loop.run_forever()
