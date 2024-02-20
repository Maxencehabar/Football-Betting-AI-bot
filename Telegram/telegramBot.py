import telebot
import os
from dotenv import load_dotenv

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler()
def send_welcome(message):
    res = "The bot is getting built! Be patient!"
    bot.send_message(message.chat.id, res)

bot.infinity_polling()