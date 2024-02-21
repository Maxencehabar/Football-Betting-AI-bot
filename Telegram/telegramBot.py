import telebot
import os
import sys
from dotenv import load_dotenv
sys.path.append("chatGPT/")
import analyseData as chatGPT

sys.path.append("DataGathering/")
import api_football as api
import logging

logging.basicConfig(level=logging.INFO)

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=["game"])
def send_welcome(message):
    messageContent = message.text
    if "-" not in messageContent:
        bot.send_message(
            message.chat.id,
            "Please provide the teams like so : /game team1-team2-league",
        )
        return
    ## the messageContent is /game team1-team2-league
    ## remove the /game
    messageContent = messageContent.replace("/game ", "")
    try:
        print("Message content: " + messageContent)
        team1 = messageContent.split("-")[0]
        team2 = messageContent.split("-")[1]
        league = messageContent.split("-")[2]
    except Exception as e:
        logging.error(e)

        bot.send_message(
            message.chat.id,
            "Please provide the teams like so : /game team1-team2-league",
        )
        return
    logging.info("Team1: " + team1 + " Team2: " + team2 + " League: " + league)
    ## Data processing and analysis.
    res = api.main(team1, team2,league)
    h2h, tea1Stats, team2Stats = res
    ## Shaping the h2h list : 
    res = ""
    for match in h2h:
        res += match + "\n"
    bot.send_message(message.chat.id, "H2H : \n" + res)
    bot.send_message(message.chat.id, "Team1 Stats : \n" + str(tea1Stats))
    bot.send_message(message.chat.id, "Team2 Stats : \n" + str(team2Stats))
    bot.send_message(message.chat.id, "Data gathered. Sending to chatGPT...")
    ## Send the data to chatGPT
    match = team1 + " vs " + team2 + " in " + league
    res = chatGPT.Analyse(match, "Team1 Stats : " + str(tea1Stats) + " Team2 Stats : " + str(team2Stats) + " H2H : " + res)
    bot.send_message(message.chat.id, "ChatGPT Answer :")
    bot.send_message(message.chat.id, "Analysis : \n" + res)

@bot.message_handler()
def sendHelp(message):
    helpMessage = "Welcome to the Football Bot! Here are the commands you can use:\n/game - Start the analysis for a match.\nPlease provide info like so : /game team1-team2-league"
    bot.send_message(message.chat.id, helpMessage)

if __name__ == "__main__":
    logging.info("Starting the bot...")
    bot.infinity_polling()
