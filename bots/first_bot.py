import telebot
from telebot.types import Message
import json

bot_client = telebot.TeleBot(token="5917024566:AAGQV3ncboZxFjnI92BZ489aoqiBS6lwaPc")
ADMIN_CHAT_ID = 340771847

@bot_client.message_handler(commands=["start"])
def echo(message: Message):
    with open("users.json", "w") as f_o:
        data_from_json = json.load(f_o)
    bot_client.reply_to(message=message, text=str(message.chat.id))



bot_client.polling()
