import telebot
import os
import sys
from dotenv import load_dotenv
sys.path.append("chatGPT/")
import analyseData as chatGPT
sys.path.append("DataGathering/footyAmigo/")
import getMatchData as getMatchData
import searchForMatchs as searchForMatchs



import logging
logging.basicConfig(level=logging.INFO)


load_dotenv()
#BOT_TOKEN = os.getenv("TESTING_TELEGRAM_BOT")
BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)



@bot.message_handler(commands=["game"])
def game(message):
    text = message.text.replace("/game ", "")
    print(text)
    words = text.split("-")
    print(words)
    id = searchForMatchs.searchForMatchs(words, bot, message)
    if id == None:
        bot.send_message(message.chat.id, "No match found.")
        return
    data = getMatchData.getMatchData(id)
    result = getMatchData.extractData(data)

    bot.send_message(message.chat.id, str(result))

    

@bot.message_handler()
def sendHelp(message):
    helpMessage = """Welcome to the AI Analysis Bot. Here are the available commands:
    /game : Get the probability of a match result.
    please provide the teams and the league like so : /game team1-team2"""
    bot.send_message(message.chat.id, helpMessage)



if __name__ == "__main__":
    logging.info("Starting the bot...")
    bot.infinity_polling()
