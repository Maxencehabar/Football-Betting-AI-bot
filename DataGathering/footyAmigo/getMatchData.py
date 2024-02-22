import requests
import json

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


def exploreMatchData():
    with open("DataGathering/footyAmigo/matchData.json", "r") as f:
        data = json.load(f)
    print(data.keys())
    print(extractData(data))


if __name__ == "__main__":
    id = "19050408"
    data = getMatchData(id)
    print(extractData(data))
