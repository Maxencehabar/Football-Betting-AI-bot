import requests
import os
from dotenv import load_dotenv
import logging
import sys

sys.path.append("../chatGPT/")
import getPays as getPays
import json

logging.basicConfig(level=logging.INFO)

load_dotenv()
api_key = os.getenv("RAPID_API_KEY")


def getCountries():
    res = requests.get(
        "https://api-football-v1.p.rapidapi.com/v3/countries",
        headers={"x-rapidapi-key": api_key},
    )
    data = res.json()["response"]
    print(data)
    with open("countriesList.json", "w") as f:
        json.dump(data, f)
    for country in data:
        print(country["name"])
    return data


def getLeagues(pays=None):
    res = requests.get(
        "https://api-football-v1.p.rapidapi.com/v3/leagues",
        headers={"x-rapidapi-key": api_key},
        params={"country": pays},
    )
    data = res.json()["response"]
    with open("leaguesList.json", "w") as f:
        json.dump(data, f)
    for league in data:
        print(league["league"])
    return data


def getTeams(leagueName, season, bot=None, message=None):
    leagueId = getLeagueId(leagueName)
    if leagueId is None:
        bot.send_message(message.chat.id, "League not found.")
    res = requests.get(
        "https://api-football-v1.p.rapidapi.com/v3/teams",
        headers={"x-rapidapi-key": api_key},
        params={"league": leagueId, "season": season},
    )
    print(res.json())
    if res.json()["results"] == 0:
        bot.send_message(message.chat.id, "No teams found.")
        return
    data = res.json()["response"]
    teamsName = []
    for team in data:
        teamsName.append(team["team"]["name"])
    return teamsName


def getH2H(team1Id: str, team2Id: str):
    res = requests.get(
        "https://api-football-v1.p.rapidapi.com/v3/fixtures/headtohead?h2h="
        + team1Id
        + "-"
        + team2Id,
        headers={"x-rapidapi-key": api_key},
    )
    data = res.json()["response"]
    matchs = []
    for match in data:
        ##print(match.keys())
        date = match["fixture"]["date"]
        ## getting only day
        date = date.split("T")[0]
        team1 = match["teams"]["home"]["name"]
        team2 = match["teams"]["away"]["name"]
        score = str(match["goals"]["home"]) + " - " + str(match["goals"]["away"])
        res = date + " : " + team1 + " " + score + " " + team2
        matchs.append(res)
    return matchs


def getFixtureStats(fixtureId):
    res = requests.get(
        "https://api-football-v1.p.rapidapi.com/v3/fixtures/statistics?fixture="
        + fixtureId,
        headers={"x-rapidapi-key": api_key},
    )
    data = res.json()["response"]
    print(data)


def getTeamId(teamName):
    logging.info("Getting team id for " + teamName)
    params = {"name": teamName}
    res = requests.get(
        "https://api-football-v1.p.rapidapi.com/v3/teams",
        headers={"x-rapidapi-key": api_key},
        params=params,
    )
    if res.status_code != 200:
        logging.error("GetTeamId : Status code != 200", str(res.json()))
        return

    ##print(res.json())
    if res.json()["results"] == 0:
        logging.error("GetTeamId : No team found.")
        return None
    data = res.json()["response"]
    team = data[0]
    teamId = team["team"]["id"]
    return teamId


def getLeagueId(leagueName):
    params = {"name": leagueName}
    res = requests.get(
        "https://api-football-v1.p.rapidapi.com/v3/leagues",
        headers={"x-rapidapi-key": api_key},
        params=params,
    )
    if res.status_code != 200:
        logging.error("Error in getLeagueId", str(res.json()))
        return
    ##print(res.json())
    if res.json()["results"] == 0:
        logging.error("No league found.")
        return None
    data = res.json()["response"]
    league = data[0]
    leagueId = league["league"]["id"]
    return leagueId


def getTeamStats(teamId, leagueId, season):
    res = requests.get(
        "https://api-football-v1.p.rapidapi.com/v3/teams/statistics?season="
        + season
        + "&team="
        + teamId
        + "&league="
        + leagueId,
        headers={"x-rapidapi-key": api_key},
    )
    if res.status_code != 200:
        logging.error("Error in getTeamStats", str(res.json()))
        return
    res = res.json()["response"]
    ##print(res)
    data = dict()
    """for key in res.keys():
        print(key)
        print(res[key])
    """

    data["form"] = res["form"]
    data["matchs"] = res["fixtures"]
    data["goals"] = res["goals"]
    return data


def exploreTeamStats():
    with open("teamStats.json", "r") as f:
        data = json.load(f)


def main(team1Name, team2Name, leagueName, bot, message):
    team1Id = getTeamId(team1Name)
    if team1Id is None:
        bot.send_message(message.chat.id, "Team1 not found.")
        return
    team2Id = getTeamId(team2Name)
    if team2Id is None:
        bot.send_message(message.chat.id, "Team2 not found.")
        return
    leagueId = getLeagueId(leagueName)
    if leagueId is None:
        bot.send_message(message.chat.id, "League not found.")
        return
    try:
        h2h = getH2H(str(team1Id), str(team2Id))
    except Exception as e:
        logging.error(e)
        bot.send_message(message.chat.id, "Error in getting h2h.")
        return
    team1Stats = getTeamStats(str(team1Id), str(leagueId), "2021")
    team2Stats = getTeamStats(str(team2Id), str(leagueId), "2021")
    return h2h, team1Stats, team2Stats


def prettyPrintStats(stats):
    res = ""
    res += "Matchs History : " + stats["form"] + "\n"
    print(stats.keys())
    ## Match part :
    print(stats["matchs"])
    for match in stats["matchs"].keys():
        print(stats["matchs"][match])
    print(res)


def getLineups(fixtureId):
    res = requests.get(
        "https://api-football-v1.p.rapidapi.com/v3/fixtures/lineups?fixture="
        + fixtureId,
        headers={"x-rapidapi-key": api_key},
    )
    data = res.json()["response"]
    print(data)
    return data


def getLeagueSeason(leagueId):
    pass


def getFixtureId(leagueId, season, date):
    res = requests.get(
        "https://api-football-v1.p.rapidapi.com/v3/fixtures",
        headers={"x-rapidapi-key": api_key},
        params={"league": leagueId, "season": season, "date": "2023-03-01"},
    )
    if res.status_code != 200:
        print("Error in getFixtureId", res.json())
    print(res.json())
    data = res.json()["response"]
    if len(data) == 0:
        print("No match found.")
        return  
    print(data)
    print(data[0])
    return data


def getLineups():
    ## get fixture id from league name, team name
    ##18893355 Cholet Dijon National France 2024-03-01 19:30:00
    res = getLeagues("France")

    leagues = []
    leaguesNames = []
    for league in res:
        actualSeason = ""
        print(league["seasons"])
        for season in league["seasons"]:
            if season["current"] == True:
                actualSeason = season["year"]
        leagues.append((league["league"]["name"], actualSeason))
        leaguesNames.append(league["league"]["name"])

    leagueId = getLeagueId("National")
    if leagueId is None:
        print("League not found. Asking chatGPT")
        res = getPays.getLeague(leaguesNames, "National")
        if "None" in res:
            print("League not found")
        else:
            leagueId = getLeagueId(res)
            print("League found : ", leagueId)
            fixtureId = getFixtureId(leagueId, "2023", "2024-03-01")
            print("Fixture id : ", fixtureId)
    print(leagueId)


if __name__ == "__main__":
    ##res = getLeagues("France")

    getFixtureId("63", "2023", "2024-03-01")
