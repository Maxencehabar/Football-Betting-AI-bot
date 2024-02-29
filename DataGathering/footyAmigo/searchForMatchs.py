import requests
from datetime import datetime

headers = {
    "authority": "f3uplov8kxj76ynmp-1.a1.typesense.net",
    "accept": "application/json, text/plain, */*",
    "accept-language": "en-US,en;q=0.9,fr;q=0.8",
    "dnt": "1",
    "origin": "https://dashboard.footyamigo.com",
    "referer": "https://dashboard.footyamigo.com/",
    "sec-ch-ua": '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Linux"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "x-typesense-api-key": "Z24wUsr9k9D8x4i2s38i98xsv5zjQLfu",
}


def searchForMatchs(words, bot=None, message=None):
    """
    This function takes a list of words and returns the id of the first match found.
    """
    query = ""
    for word in words:
        query += word + " "
    response = requests.get(
        "https://f3uplov8kxj76ynmp-1.a1.typesense.net/collections/fixtures/documents/search?q="
        + query
        + "&query_by=home_name,away_name,league_name,country_name&filter_by=timestamp:%3E1708604340+%26%26+status:[LIVE,+HT,+PEN_LIVE,+BREAK,+ET,+NS]&sort_by=timestamp:asc&per_page=30&highlight_fields=none",
        headers=headers,
    )

    if response.status_code != 200:
        print("Error in searchForMatchs", response.json())
        return
    if response.json()["found"] == 0:
        print("No match found.")
        return
    ##print(response.json())
    data = response.json()["hits"]
    for match in data:
        id = match["document"]["id"]
        status = match["document"]["status"]
        timestamp = match["document"]["timestamp"]
        pays = match["document"]["country_name"]
        print(pays)
        ## convert the timestamp to a human readable format.
        ## timestamp is 1708610400
        date = datetime.fromtimestamp(timestamp)
        print(date)
        if status == "NS":
            if bot and message:
                bot.send_message(
                    message.chat.id,
                    "Found the match : "
                    + match["document"]["home_name"]
                    + " vs "
                    + match["document"]["away_name"]
                    + " in "
                    + match["document"]["league_name"],
                )
                bot.send_message(message.chat.id, "Happenning at : " + str(date))
            print("Found the match : ", id)
            return (id, match["document"]["home_name"], match["document"]["away_name"], match["document"]["league_name"], date)


if __name__ == "__main__":
    searchForMatchs(["Zacapa Tellioz"])
