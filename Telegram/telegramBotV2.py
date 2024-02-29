import telebot
import os
import sys
import time
from dotenv import load_dotenv

sys.path.append("chatGPT/")


# import analyseData as chatGPT
import newChatGPT as chatGPT

sys.path.append("DataGathering/footyAmigo/")
import getMatchData as getMatchData
import getResults as getResults
import searchForMatchs as searchForMatchs

sys.path.append("DataGathering/footyStats/")
import getMatchLineups as getMatchLineups
import searchFootyStats as searchFootyStats

import logging

logging.basicConfig(level=logging.INFO)


load_dotenv()
BOT_TOKEN = os.getenv("TESTING_TELEGRAM_BOT")
#BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=["game"])
def game(message):
    text = message.text.replace("/game ", "")
    words = text.split("-")
    if words == None or words == []:
        bot.send_message(
            message.chat.id,
            "Please provide the teams and the league like so : /game team1-team2",
        )
        return
    (id, home_name, away_name, leagueName, date) = searchForMatchs.searchForMatchs(words, bot, message)
    print(id, home_name, away_name, leagueName,  date)
    if id == None:
        bot.send_message(message.chat.id, "No match found.")
        return
    stringToChatGPT = ""
    data = getMatchData.getMatchData(id)
    probaStr = getMatchData.getProbaStr(data)
    stringToChatGPT += "Probabilities : \n"
    stringToChatGPT += probaStr
    bot.send_message(message.chat.id, "Probabilities :")
    time.sleep(0.5)
    bot.send_message(message.chat.id, str(probaStr))

    stringToChatGPT += "\nMatch history : \n"
    h2h, home, away = getResults.getResults(id)
    stringToChatGPT += "Head to Head : \n"
    stringMatch = getResults.getMatchStr(h2h)
    stringToChatGPT += stringMatch
    bot.send_message(message.chat.id, "Head to Head :")
    time.sleep(0.5)
    bot.send_message(message.chat.id, stringMatch)

    stringToChatGPT += "Home team last matches : \n"
    stringMatch = getResults.getMatchStr(home)
    stringToChatGPT += stringMatch
    bot.send_message(message.chat.id, "Home team last matches :")
    time.sleep(0.5)
    bot.send_message(message.chat.id, stringMatch)

    stringToChatGPT += "Away team last matches : \n"
    stringMatch = getResults.getMatchStr(away)
    stringToChatGPT += stringMatch
    bot.send_message(message.chat.id, "Away team last matches :")
    time.sleep(0.5)
    bot.send_message(message.chat.id, stringMatch)

    ## getting the stats

    stats = getMatchData.extractStats(data)
    stringToChatGPT += "Stats : \n"
    stringStats = getMatchData.getStatsStr(stats)
    stringToChatGPT += stringStats
    bot.send_message(message.chat.id, "Stats :")
    time.sleep(0.5)
    bot.send_message(message.chat.id, stringStats)

    ## getting the lineups
    results = searchFootyStats.searchForMatchs(home_name)
    
    if len(results) == 0:
        bot.send_message(message.chat.id, "Couldn't get lineups.")
    else:
        res = results[0]
        print(res)
        url = res[1]
        lineups = getMatchLineups.getLineups(url)
        if lineups == False:
            bot.send_message(message.chat.id, "Couldn't get lineups.")
        else:
            stringToChatGPT += "Lineups : \n"
            stringToChatGPT += str(lineups)
            bot.send_message(message.chat.id, "Lineups :")
            time.sleep(0.5)
            for team in lineups:
                bot.send_message(message.chat.id, str(team))
                time.sleep(0.5)
    
    match = data["home_name"] + " vs " + data["away_name"]
    bot.send_message(message.chat.id, "ChatGPT Analysis :")
    ##res = chatGPT.Analyse(match=match, stats=stringToChatGPT)
    ##bot.send_message(message.chat.id, res)


@bot.message_handler()
def sendHelp(message):
    helpMessage = """Welcome to the AI Analysis Bot. Here are the available commands:
    /game : Get the probability of a match result.
    please provide the teams and the league like so : /game team1-team2"""
    bot.send_message(message.chat.id, helpMessage)


if __name__ == "__main__":
    logging.info("Starting the bot...")
    bot.infinity_polling()
