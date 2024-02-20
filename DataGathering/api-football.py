import requests
import os
from dotenv import load_dotenv
import logging
import json

logging.basicConfig(level=logging.INFO)

api_key = os.getenv("RAPID_API_KEY")

## For instance, here is the input we get : Guadalajara Chivas at Necaxa (SOCCER, Mexico Primera Division)
## To get the H2H history, we need the two team ids


def getH2H(team1: str, team2: str):
    res = requests.get(
        "https://api-football-v1.p.rapidapi.com/v3/fixtures/headtohead?h2h="
        + team1
        + "-"
        + team2,
        headers={"x-rapidapi-key": api_key},
    )
    data = res.json()["response"]
    print(data)
    with open("h2h.json", "w") as f:
        json.dump(data, f)


def exploreData():
    with open("h2h.json", "r") as f:
        data = json.load(f)
    print(len(data))
    for match in data:
        ##print(match.keys())
        date = match["fixture"]["date"]
        ## getting only day
        date = date.split("T")[0]
        team1 = match["teams"]["home"]["name"]
        team2 = match["teams"]["away"]["name"]
        score = str(match["goals"]["home"]) + " - " + str(match["goals"]["away"])
        print(date, ":", team1, score, team2)


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


def getData(input):

    res = requests.get(
        "https://api-football-v1.p.rapidapi.com/v3/countries",
        headers={"x-rapidapi-key": api_key},
    )
    print(res.json())


if __name__ == "__main__":
    """id1 = getTeamId("Guadalajara Chivas")
    id2 = getTeamId("Necaxa")
    print(id1, id2)"""
    id1 = 2278
    id2 = 2288
    ##getH2H(str(id1), str(id2))
    exploreData()
