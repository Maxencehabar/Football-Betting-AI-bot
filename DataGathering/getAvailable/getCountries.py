import json


def getCountriesList():
    with open("DataGathering/getAvailable/countriesList.json", "r") as f:
        countries = json.load(f)
    names = []
    for country in countries:
        print(country["name"])
        names.append(country["name"])
    return names


def getLeaguesList(country):
    with open("DataGathering/getAvailable/leaguesList.json", "r") as f:
        leagues = json.load(f)
    names = []
    for league in leagues:
        if league["country"]["name"] == country:
            names.append(league["league"]["name"])
    return names


if __name__ == "__main__":
    getLeaguesList("France")
