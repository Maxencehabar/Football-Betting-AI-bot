import requests
import os
from dotenv import load_dotenv
import logging
import json

logging.basicConfig(level=logging.INFO)

load_dotenv()
api_key = os.getenv("RAPID_API_KEY")

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


def getLeague(leagueName):
    res = requests.get(
        "https://api-football-v1.p.rapidapi.com/v3/leagues",
        headers={"x-rapidapi-key": api_key},
    )
    data = res.json()["response"]
    print(type(data))


def getTeamId(teamName):
    logging.info("Getting team id for " + teamName)
    params = {"name": teamName}
    res = requests.get(
        "https://api-football-v1.p.rapidapi.com/v3/teams",
        headers={"x-rapidapi-key": api_key},
        params=params,
    )
    if res.status_code != 200:
        logging.error("Error in getTeamId", str(res.json()))
        return

    try:
        data = res.json()["response"]
        team = data[0]
        teamId = team["team"]["id"]
        return teamId
    except:
        logging.error("Error in getTeamId", str(res.json()))
        return


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
    with open("league.json", "w") as f:
        json.dump(res.json(), f)
    try:
        data = res.json()["response"]
        league = data[0]
        leagueId = league["league"]["id"]
        return leagueId
    except:
        logging.error("Error in getLeagueId", str(res.json()))
        return


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


def main(team1Name, team2Name, leagueName):
    team1Id = getTeamId(team1Name)
    team2Id = getTeamId(team2Name)
    leagueId = getLeagueId(leagueName)
    h2h = getH2H(str(team1Id), str(team2Id))
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


if __name__ == "__main__":
    main("Auxerre", "Marseille", "Ligue 1")
