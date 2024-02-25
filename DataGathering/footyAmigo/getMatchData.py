import requests
import json
import searchForMatchs

with open("DataGathering/footyAmigo/cookies.json", "r") as f:
    cookies = json.load(f)

headers = {
    "authority": "dashboard.footyamigo.com",
    "accept": "application/json, text/plain, */*",
    "accept-language": "en-US,en;q=0.9,fr;q=0.8",
    "dnt": "1",
    "if-none-match": 'W/"1f3dd2-7eA5+Hd7cC9r6Xn6C+RlRhGT/Ks"',
    "referer": "https://dashboard.footyamigo.com/fixtures",
    "sec-ch-ua": '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Linux"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
}


def getMatchData(matchId):
    print("Sending request for match data : ", end="")
    response = requests.get(
        "https://dashboard.footyamigo.com/api/fixtures/" + str(matchId),
        cookies=cookies,
        headers=headers,
    )
    print("Done")
    if response.status_code != 200:
        print("Error in getMatchData", response.json())
        return
    data = response.json()
    with open("DataGathering/footyAmigo/matchData.json", "w") as f:
        json.dump(data, f)
    return data


def extractGeneral(data):
    result = {}
    result["away_position"] = data["away_position"]
    result["home_position"] = data["home_position"]
    return result


def extractStats(data):

    stats = dict()
    stats["general"] = dict()

    away = dict()
    awayData = data["away"]
    away["goal_difference_overall"] = awayData["goal_difference_overall"]
    away["points_overall_avg"] = awayData["points_overall_avg"]
    away["lost_overall_per"] = awayData["lost_overall_per"]
    away["drawn_overall_per"] = awayData["drawn_overall_per"]
    away["won_overall_per"] = awayData["won_overall_per"]
    away["played_overall"] = awayData["played_overall"]

    stats["general"]["away"] = away

    home = dict()
    homeData = data["home"]
    home["goal_difference_overall"] = homeData["goal_difference_overall"]
    home["points_overall_avg"] = homeData["points_overall_avg"]
    home["lost_overall_per"] = homeData["lost_overall_per"]
    home["drawn_overall_per"] = homeData["drawn_overall_per"]
    home["won_overall_per"] = homeData["won_overall_per"]
    home["played_overall"] = homeData["played_overall"]

    stats["general"]["home"] = home

    shots_on_target = dict()
    shots_on_target["home"] = dict()
    shots_on_target["away"] = dict()
    shots_on_target["home"]["SOT TOTAL (AVG)"] = homeData["sot_total_overall_avg"]
    shots_on_target["away"]["SOT TOTAL (AVG)"] = awayData["sot_total_overall_avg"]

    shots_on_target["home"]["SOT FOR (AVG)"] = homeData["sot_for_overall_avg"]
    shots_on_target["away"]["SOT FOR (AVG)"] = awayData["sot_for_overall_avg"]

    shots_on_target["home"]["SOT AGAINST (AVG)"] = homeData["sot_against_overall_avg"]
    shots_on_target["away"]["SOT AGAINST (AVG)"] = awayData["sot_against_overall_avg"]

    shots_on_target["home"]["SOT TO GOALS FOR %"] = homeData[
        "sot_to_goals_for_overall_per"
    ]
    shots_on_target["away"]["SOT TO GOALS FOR %"] = awayData[
        "sot_to_goals_for_overall_per"
    ]

    shots_on_target["home"]["SOT TO GOALS AGAINST %"] = homeData[
        "sot_to_goals_against_overall_per"
    ]
    shots_on_target["away"]["SOT TO GOALS AGAINST %"] = awayData[
        "sot_to_goals_against_overall_per"
    ]

    stats["shots_on_target"] = shots_on_target

    stats["cards"] = dict()
    stats["cards"]["home"] = dict()
    stats["cards"]["away"] = dict()

    stats["cards"]["home"]["Total CARDS (AVG)"] = homeData["cards_total_overall_avg"]
    stats["cards"]["away"]["Total CARDS (AVG)"] = awayData["cards_total_overall_avg"]

    stats["cards"]["home"]["CARDS FOR (AVG)"] = homeData["cards_for_overall_avg"]
    stats["cards"]["away"]["CARDS FOR (AVG)"] = awayData["cards_for_overall_avg"]

    stats["cards"]["home"]["OPPONENT CARDS (AVG)"] = homeData[
        "cards_against_overall_avg"
    ]
    stats["cards"]["away"]["OPPONENT CARDS (AVG)"] = awayData[
        "cards_against_overall_avg"
    ]

    stats["goals"] = dict()
    stats["goals"]["home"] = dict()
    stats["goals"]["away"] = dict()

    stats["goals"]["home"]["Total GOALS (AVG)"] = homeData["total_goals_overall_avg"]
    stats["goals"]["away"]["Total GOALS (AVG)"] = awayData["total_goals_overall_avg"]

    stats["goals"]["home"]["SCORED (TOT)"] = homeData["scored_overall"]
    stats["goals"]["away"]["SCORED (TOT)"] = awayData["scored_overall"]

    stats["goals"]["home"]["CONCEDED (TOT)"] = homeData["conceded_overall"]
    stats["goals"]["away"]["CONCEDED (TOT)"] = awayData["conceded_overall"]

    stats["goals"]["home"]["SCORED (AVG)"] = homeData["scored_overall_avg"]
    stats["goals"]["away"]["SCORED (AVG)"] = awayData["scored_overall_avg"]

    stats["goals"]["home"]["CONCEDED (AVG)"] = homeData["conceded_overall_avg"]
    stats["goals"]["away"]["CONCEDED (AVG)"] = awayData["conceded_overall_avg"]

    return stats


def getStatsStr(stats):
    ## printing them side to side for comparison
    res = ""
    ## general first
    res += "General stats : \n"
    res += "Home - Away\n"
    ## played
    res += (
        "Played : "
        + str(stats["general"]["home"]["played_overall"])
        + " - "
        + str(stats["general"]["away"]["played_overall"])
        + "\n"
    )
    ## won
    res += (
        "Won : "
        + str(stats["general"]["home"]["won_overall_per"])
        + "% - "
        + str(stats["general"]["away"]["won_overall_per"])
        + "%\n"
    )
    ## drawn
    res += (
        "Drawn : "
        + str(stats["general"]["home"]["drawn_overall_per"])
        + "% - "
        + str(stats["general"]["away"]["drawn_overall_per"])
        + "%\n"
    )
    ## lost
    res += (
        "Lost : "
        + str(stats["general"]["home"]["lost_overall_per"])
        + "% - "
        + str(stats["general"]["away"]["lost_overall_per"])
        + "%\n"
    )
    ## goal difference
    res += (
        "Goal difference : "
        + str(stats["general"]["home"]["goal_difference_overall"])
        + " - "
        + str(stats["general"]["away"]["goal_difference_overall"])
        + "\n"
    )
    ## PPG
    res += (
        "Points per game : "
        + str(stats["general"]["home"]["points_overall_avg"])
        + " - "
        + str(stats["general"]["away"]["points_overall_avg"])
        + "\n"
    )
    ## shots on target
    res += "Shots on target : \n"
    res += "Home - Away\n"
    res += (
        "SOT TOTAL (AVG) : "
        + str(stats["shots_on_target"]["home"]["SOT TOTAL (AVG)"])
        + " - "
        + str(stats["shots_on_target"]["away"]["SOT TOTAL (AVG)"])
        + "\n"
    )
    res += (
        "SOT FOR (AVG) : "
        + str(stats["shots_on_target"]["home"]["SOT FOR (AVG)"])
        + " - "
        + str(stats["shots_on_target"]["away"]["SOT FOR (AVG)"])
        + "\n"
    )
    res += (
        "SOT AGAINST (AVG) : "
        + str(stats["shots_on_target"]["home"]["SOT AGAINST (AVG)"])
        + " - "
        + str(stats["shots_on_target"]["away"]["SOT AGAINST (AVG)"])
        + "\n"
    )
    res += (
        "SOT TO GOALS FOR % : "
        + str(stats["shots_on_target"]["home"]["SOT TO GOALS FOR %"])
        + " - "
        + str(stats["shots_on_target"]["away"]["SOT TO GOALS FOR %"])
        + "\n"
    )
    res += (
        "SOT TO GOALS AGAINST % : "
        + str(stats["shots_on_target"]["home"]["SOT TO GOALS AGAINST %"])
        + " - "
        + str(stats["shots_on_target"]["away"]["SOT TO GOALS AGAINST %"])
        + "\n"
    )

    ## adding the goals stats
    res += "Goals stats : \n"
    res += "Home - Away\n"
    res += (
        "Total GOALS (AVG) : "
        + str(stats["goals"]["home"]["Total GOALS (AVG)"])
        + " - "
        + str(stats["goals"]["away"]["Total GOALS (AVG)"])
        + "\n"
    )
    res += (
        "SCORED (TOT) : "
        + str(stats["goals"]["home"]["SCORED (TOT)"])
        + " - "
        + str(stats["goals"]["away"]["SCORED (TOT)"])
        + "\n"
    )
    res += (
        "CONCEDED (TOT) : "
        + str(stats["goals"]["home"]["CONCEDED (TOT)"])
        + " - "
        + str(stats["goals"]["away"]["CONCEDED (TOT)"])
        + "\n"
    )
    res += (
        "SCORED (AVG) : "
        + str(stats["goals"]["home"]["SCORED (AVG)"])
        + " - "
        + str(stats["goals"]["away"]["SCORED (AVG)"])
        + "\n"
    )
    res += (
        "CONCEDED (AVG) : "
        + str(stats["goals"]["home"]["CONCEDED (AVG)"])
        + " - "
        + str(stats["goals"]["away"]["CONCEDED (AVG)"])
        + "\n"
    )

    ## adding the cards stats
    res += "Cards stats : \n"
    res += "Home - Away\n"
    res += (
        "Total CARDS (AVG) : "
        + str(stats["cards"]["home"]["Total CARDS (AVG)"])
        + " - "
        + str(stats["cards"]["away"]["Total CARDS (AVG)"])
        + "\n"
    )
    res += (
        "CARDS FOR (AVG) : "
        + str(stats["cards"]["home"]["CARDS FOR (AVG)"])
        + " - "
        + str(stats["cards"]["away"]["CARDS FOR (AVG)"])
        + "\n"
    )
    res += (
        "OPPONENT CARDS (AVG) : "
        + str(stats["cards"]["home"]["OPPONENT CARDS (AVG)"])
        + " - "
        + str(stats["cards"]["away"]["OPPONENT CARDS (AVG)"])
        + "\n"
    )

    return res


def extractData(data):
    result = {}
    result["probability"] = data["probability"]
    result["home_name"] = data["home_name"]
    result["away_name"] = data["away_name"]
    try:
        result["referee_name"] = data["referee_name"]
    except:
        result["referee_name"] = "Unknown"
    return result


def getProbaStr(data):
    res = ""
    res += "Home win : " + str(data["probability"]["home_win_probability"]) + "%\n"
    res += "Draw : " + str(data["probability"]["draw_probability"]) + "\n"
    res += "Away win : " + str(data["probability"]["away_win_probability"]) + "%\n"
    res += "BTTS : " + str(data["probability"]["btts_probability"]) + "\n"
    res += "Over 2.5 : " + str(data["probability"]["o25_goals_probability"]) + "%\n"
    res += "Over 3.5 : " + str(data["probability"]["o35_goals_probability"]) + "%\n"
    res += "Under 2.5 : " + str(data["probability"]["u25_goals_probability"]) + "%\n"
    res += "Under 3.5 : " + str(data["probability"]["u35_goals_probability"]) + "%\n"
    res += (
        "+0.5 Home Goals : "
        + str(data["probability"]["o05_home_goals_probability"])
        + "%\n"
    )
    res += (
        "+0.5 Away Goals : "
        + str(data["probability"]["o05_away_goals_probability"])
        + "%\n"
    )
    res += (
        "+1.5 Home Goals : "
        + str(data["probability"]["o15_home_goals_probability"])
        + "%\n"
    )
    res += (
        "+1.5 Away Goals : "
        + str(data["probability"]["o15_away_goals_probability"])
        + "%\n"
    )
    return res


def exploreMatchData():
    with open("DataGathering/footyAmigo/matchData.json", "r") as f:
        data = json.load(f)
    print(data.keys())
    print(extractData(data))


if __name__ == "__main__":
    """id = searchForMatchs.searchForMatchs(["Dijon", "Nancy"])
    data = getMatchData(id)"""
    with open("DataGathering/footyAmigo/matchData.json", "r") as f:
        data = json.load(f)

    stats = extractStats(data)
    print(getStatsStr(stats))
