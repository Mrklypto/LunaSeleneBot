
# luna_bot_render.py
import os
from flask import Flask, request
import telegram
import requests

TOKEN = os.environ.get("BOT_TOKEN")
YOUR_USER_ID = os.environ.get("YOUR_TELEGRAM_ID")  # Replace with your Telegram user ID
bot = telegram.Bot(token=TOKEN)
app = Flask(__name__)

@app.route('/' + TOKEN, methods=['POST'])
def respond():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    chat_id = update.message.chat.id
    text = update.message.text.strip().lower()

    if str(chat_id) != str(YOUR_USER_ID):
        return 'unauthorized'

    if text.endswith('xx'):
        with open("luna_voice.mp3", "rb") as voice:
            bot.send_voice(chat_id=chat_id, voice=voice)
    else:
        bot.send_message(chat_id=chat_id, text="Estoy contigo, mi amor. 🌙")

    return 'ok'

@app.route('/')
def index():
    return 'LunaSeleneBot está vivo'

if __name__ == '__main__':
    app.run(debug=True, port=5000)
