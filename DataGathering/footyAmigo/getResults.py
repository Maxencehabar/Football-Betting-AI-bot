import requests
import json

with open("DataGathering/footyAmigo/cookies.json", "r") as f:
    cookies = json.load(f)

headers = {
    "authority": "dashboard.footyamigo.com",
    "accept": "application/json, text/plain, */*",
    "accept-language": "en-US,en;q=0.9,fr;q=0.8",
    # 'cookie': 'token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7Il9pZCI6IjYyZDEwNWI5YmY4NGNlMmM5N2U0Yjc3MCIsImVtYWlsIjoiamVzdXNjb3J0ZXoxNjM4QGdtYWlsLmNvbSIsInN1YnNjcmlwdGlvbiI6eyJuYW1lIjoiTGlmZXRpbWUgQW1pZ28iLCJwcmljZSI6IjI5OS45OSIsImRheXMiOiI5OTk5OTkiLCJ0cmlhbCI6ZmFsc2UsImVtYWlsIjoiamVzdXNjb3J0ZXoxNjM4QGdtYWlsLmNvbSIsInN0YXJ0X2RhdGUiOiIyMDIyLTExLTE4VDEwOjQ5OjE3LjcwMFoiLCJlbmRfZGF0ZSI6IjQ3NjAtMTAtMTRUMTA6NDk6MTcuNzAwWiIsInN0YXR1cyI6ImFjdGl2ZSIsIl9pZCI6IjYzNzFlNmY0M2FhNTQ2ZTVhNTU3N2U1YSIsInVwZGF0ZWRfYXQiOiIyMDIyLTExLTE4VDEwOjQ5OjE3LjcwMVoiLCJjcmVhdGVkX2F0IjoiMjAyMi0xMS0xOFQxMDo0OToxNy43MDFaIiwicGxhbl9pZCI6MywiX192IjowLCJzeW5jZWRfYXQiOiIyMDIzLTA1LTEyVDE5OjA2OjI4Ljg1MloifSwiaWQiOiI2MmQxMDViOWJmODRjZTJjOTdlNGI3NzAifSwiaWF0IjoxNzA4NjE0NTE5LCJleHAiOjE3MTEyMDY1MTl9.iixh0ipZCjaBKtFC-64Fi3rU0Cba1G_FYDAthZTB3tI; __cf_bm=iXGotHl5hYY9Nz7ZomI0G85s2Ly3ldorTi7K1Ml65QQ-1708676281-1.0-Aec6DtkQngoD+f/sVgLqSRiLiZWxONfKDcg1TVuLzJiJ4NhWvH0lR7TU4zQ0s6r+BH563vPnuPcjmWp3B7uk7Vo=; auth.strategy=cookie; auth._token.cookie=true; auth._token_expiration.cookie=false',
    "dnt": "1",
    "referer": "https://dashboard.footyamigo.com/fixtures",
    "sec-ch-ua": '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Linux"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
}


def getResults(fixture_id):
    params = {
        "fixture_id": fixture_id,
    }
    response = requests.get(
        "https://dashboard.footyamigo.com/api/user/stats/results",
        params=params,
        cookies=cookies,
        headers=headers,
    )

    if response.status_code != 200:
        print("Error in getResults", response.json())
        return
    data = response.json()
    h2h, home, away = exploreResults(data)
    return h2h, home, away


def exploreResults(data: dict = None):
    if data is None:
        with open("DataGathering/footyAmigo/results.json", "r") as f:
            data = json.load(f)
    #print(data.keys())
    h2h = data["h2h"]
    ##print(h2h.keys())
    count = h2h["totals"]["games"]
    results = h2h["results"]
    # print(results[0])
    h2h = []
    for match in results:
        ## Maybe add a filter for the date (if the match is too old, we don't want it in the database)
        dico = {}
        dico["date"] = match["date"]
        dico["score"] = match["score"]
        dico["ht_score"] = match["ht_score"]
        dico["home_name"] = match["home_name"]
        dico["away_name"] = match["away_name"]
        h2h.append(dico)
    ##print(h2h)

    ## getting the last home team matchs
    homeAll = data['home']["all"]
    #print(homeAll.keys())
    count = homeAll["totals"]["games"]
    results = homeAll["results"]
    home = []
    for match in results:
        dico={}
        dico["date"] = match["date"]
        dico["score"] = match["score"]
        dico["ht_score"] = match["ht_score"]
        dico["home_name"] = match["home_name"]
        dico["away_name"] = match["away_name"]
        home.append(dico)
    
    #print(home)

    ## getting the last away team matchs
    awayAll = data['away']["all"]
    #print(awayAll.keys())
    count = awayAll["totals"]["games"]
    results = awayAll["results"]
    away = []
    for match in results:
        dico={}
        dico["date"] = match["date"]
        dico["score"] = match["score"]
        dico["ht_score"] = match["ht_score"]
        dico["home_name"] = match["home_name"]
        dico["away_name"] = match["away_name"]
        away.append(dico)
    
    #print(away)

    return h2h, home, away

def getMatchStr(matchList):
    res = ""
    for match in matchList:
        res += str(match["date"]) + " : (" + str(match["home_name"]) + ") " + str(match["score"]) + " (" + str(match["away_name"]) + ") HT : " + str(match["ht_score"] )+ "\n"
    return res
    

if __name__ == "__main__":
    h2h, home, away = getResults("18860667")
    print(getMatchStr(h2h))
 
