import requests
import logging
from bs4 import BeautifulSoup

logging.basicConfig(level=logging.INFO)

cookies = {
    "country": "FR",
    "PHPSESSID": "8ulc205k5lrp3e74krt0f9csqc",
    "__cflb": "0H28vfqVTQfGYScnseHmmBNxbXR2bUiBaUGHJoG8ufq",
    "tz": "Europe/Berlin",
    "cartalyst_sentinel": "%22C5KdHp9PhQzU4c2IMXp7yEjA1NvRzBYQ%22",
}

headers = {
    "authority": "footystats.org",
    "accept": "*/*",
    "accept-language": "en-US,en;q=0.9,fr;q=0.8",
    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
    # 'cookie': 'country=FR; PHPSESSID=8ulc205k5lrp3e74krt0f9csqc; __cflb=0H28vfqVTQfGYScnseHmmBNxbXR2bUiBaUGHJoG8ufq; tz=Europe/Berlin; cartalyst_sentinel=%22C5KdHp9PhQzU4c2IMXp7yEjA1NvRzBYQ%22',
    "dnt": "1",
    "origin": "https://footystats.org",
    "referer": "https://footystats.org/france/dijon-fco-vs-so-choletais-h2h-stats",
    "sec-ch-ua": '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Linux"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "x-requested-with": "XMLHttpRequest",
}


def searchForMatchs(searchString):
    """
    The search string needs to be one word (so the team1 name)
    """
    data = {
        "searchString": searchString,
    }

    response = requests.post(
        "https://footystats.org/search.php", cookies=cookies, headers=headers, data=data
    )
    if response.status_code != 200:
        logging.error("Error in searchForMatchs", str(response.json()))
        return
    soup = BeautifulSoup(response.text, "html.parser")
    ##print(soup.prettify())
    li_elements = soup.find_all("li")

    # Loop through each 'li' element and extract information
    matchs = []
    for li in li_elements:
        team_name = li.find("div", class_="name").text.strip()
        fixture_url = li.find("a")["href"]
        if "vs" in team_name:
            print("Match name:", team_name)
            print("Fixture URL:", fixture_url)
            matchs.append((team_name, fixture_url))
    
    return matchs



if __name__ == "__main__":
    searchForMatchs("madrid")
