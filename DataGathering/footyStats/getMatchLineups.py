import requests
from bs4 import BeautifulSoup
import logging
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
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "en-US,en;q=0.9,fr;q=0.8",
    # 'cookie': 'country=FR; PHPSESSID=8ulc205k5lrp3e74krt0f9csqc; __cflb=0H28vfqVTQfGYScnseHmmBNxbXR2bUiBaUGHJoG8ufq; tz=Europe/Berlin; cartalyst_sentinel=%22C5KdHp9PhQzU4c2IMXp7yEjA1NvRzBYQ%22',
    "dnt": "1",
    "referer": "https://footystats.org/azerbaijan/energetik-fk-vs-fk-difai-agsu-h2h-stats",
    "sec-ch-ua": '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Linux"',
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
}


div = """
<div class="rw100 fr rmt2e" style="width:48%;">
 <div class="row cf">
  <a class="semi-bold" href="/clubs/dijon-fco-446">
   <img alt="Dijon FCO Logo" class="club-image-border-circular-no-border club-image-size-tiny mr03 fa-adjust-l2" src="https://cdn.footystats.org/img/teams/france-dijon-fco_thumb.png" style="width:18px;"/>
   <span class="fa-adjust-h2">
    Dijon
   </span>
  </a>
 </div>
 <div class="w100 fl mt10 rw100 m0Auto cf club-blue-highlight br4 bbox" style="font-size:8.5pt;">
  <p class="col-lg-1 semi-bold lh14e">
   #
  </p>
  <p class="col-lg-11 semi-bold lh14e">
   Starting 11
  </p>
 </div>
 <div class="w100 fl rw100 m0Auto bbox">
  <div class="row cf bbox">
   <p class="col-lg-4 fs08e semi-bold" style="height:28px;line-height:28px;">
    Forwards
   </p>
   <div class="col-lg-8 pr" height="38px;">
    <div class="w100 pa" style="top:13px;height:1px;background:#ddd;">
    </div>
   </div>
  </div>
  <div class="row cf m0Auto" style="font-size:10pt;line-height:1.6em;">
   <p class="col-lg-1 fs08e semi-bold dark-gray al">
    8
   </p>
   <p class="col-lg-7 ellipses">
    <a class="semi-bold fs09e" href="/players/france/kevin-schur">
     <span class="mr05 flag o8 flag-1 flag-fr-12">
     </span>
     Kevin Schur
    </a>
   </p>
   <p class="col-lg-2 ac fs08e semi-bold">
    LW
   </p>
   <p class="col-lg-2 ac" style="">
    <span class="dBlock ac gray small" style="width:30px;">
     -
    </span>
   </p>
  </div>
  <div class="row cf m0Auto" style="font-size:10pt;line-height:1.6em;">
   <p class="col-lg-1 fs08e semi-bold dark-gray al">
    21
   </p>
   <p class="col-lg-7 ellipses">
    <a class="semi-bold fs09e" href="/players/tunisia/mohamed-ben-fredj">
     <span class="mr05 flag o8 flag-1 flag-tn-12">
     </span>
     Mohamed Ben Fredj
    </a>
   </p>
   <p class="col-lg-2 ac fs08e semi-bold">
    -
   </p>
   <p class="col-lg-2 ac" style="">
    <span class="dBlock ac gray small" style="width:30px;">
     -
    </span>
   </p>
  </div>
  <div class="row cf bbox">
   <p class="col-lg-4 fs08e semi-bold" style="height:28px;line-height:28px;">
    Midfielders
   </p>
   <div class="col-lg-8 pr" height="38px;">
    <div class="w100 pa" style="top:12px;height:1px;background:#ddd;">
    </div>
   </div>
  </div>
  <div class="row cf m0Auto" style="font-size:10pt;line-height:1.6em;">
   <p class="col-lg-1 fs08e semi-bold dark-gray al">
    34
   </p>
   <p class="col-lg-7 ellipses">
    <span class="semi-bold fs09e">
     <span class="mr05 flag o8 flag-1 flag-fr-12">
     </span>
     Zakaria Ariss
    </span>
   </p>
   <p class="col-lg-2 ac fs08e semi-bold">
    -
   </p>
   <p class="col-lg-2 ac" style="">
    <span class="dBlock ac gray small" style="width:30px;">
     -
    </span>
   </p>
  </div>
  <div class="row cf m0Auto" style="font-size:10pt;line-height:1.6em;">
   <p class="col-lg-1 fs08e semi-bold dark-gray al">
    14
   </p>
   <p class="col-lg-7 ellipses">
    <a class="semi-bold fs09e" href="/players/france/jordan-marie">
     <span class="mr05 flag o8 flag-1 flag-fr-12">
     </span>
     Jordan Marié
    </a>
   </p>
   <p class="col-lg-2 ac fs08e semi-bold">
    CM
   </p>
   <p class="col-lg-2 ac" style="">
    <span class="dBlock ac gray small" style="width:30px;">
     -
    </span>
   </p>
  </div>
  <div class="row cf m0Auto" style="font-size:10pt;line-height:1.6em;">
   <p class="col-lg-1 fs08e semi-bold dark-gray al">
    6
   </p>
   <p class="col-lg-7 ellipses">
    <a class="semi-bold fs09e" href="/players/france/rayan-souici">
     <span class="mr05 flag o8 flag-1 flag-fr-12">
     </span>
     Rayan Souici
    </a>
   </p>
   <p class="col-lg-2 ac fs08e semi-bold">
    -
   </p>
   <p class="col-lg-2 ac" style="">
    <span class="dBlock ac gray small" style="width:30px;">
     -
    </span>
   </p>
  </div>
  <div class="row cf m0Auto" style="font-size:10pt;line-height:1.6em;">
   <p class="col-lg-1 fs08e semi-bold dark-gray al">
    20
   </p>
   <p class="col-lg-7 ellipses">
    <a class="semi-bold fs09e" href="/players/france/zakaria-fdaouch">
     <span class="mr05 flag o8 flag-1 flag-fr-12">
     </span>
     Zakaria Fdaouch
    </a>
   </p>
   <p class="col-lg-2 ac fs08e semi-bold">
    -
   </p>
   <p class="col-lg-2 ac" style="">
    <span class="dBlock ac gray small" style="width:30px;">
     -
    </span>
   </p>
  </div>
  <div class="row cf m0Auto" style="font-size:10pt;line-height:1.6em;">
   <p class="col-lg-1 fs08e semi-bold dark-gray al">
    17
   </p>
   <p class="col-lg-7 ellipses">
    <span class="semi-bold fs09e">
     <span class="mr05 flag o8 flag-1 flag-fr-12">
     </span>
     Yanis Chahid
    </span>
   </p>
   <p class="col-lg-2 ac fs08e semi-bold">
    -
   </p>
   <p class="col-lg-2 ac" style="">
    <span class="dBlock ac gray small" style="width:30px;">
     -
    </span>
   </p>
  </div>
  <div class="row cf bbox">
   <p class="col-lg-4 fs08e semi-bold" style="height:28px;line-height:28px;">
    Defenders
   </p>
   <div class="col-lg-8 pr" height="38px;">
    <div class="w100 pa" style="top:12px;height:1px;background:#ddd;">
    </div>
   </div>
  </div>
  <div class="row cf m0Auto" style="font-size:10pt;line-height:1.6em;">
   <p class="col-lg-1 fs08e semi-bold dark-gray al">
    23
   </p>
   <p class="col-lg-7 ellipses">
    <a class="semi-bold fs09e" href="/players/france/cedric-makutungu">
     <span class="mr05 flag o8 flag-1 flag-fr-12">
     </span>
     Cedric Makutungu
    </a>
   </p>
   <p class="col-lg-2 ac fs08e semi-bold">
    -
   </p>
   <p class="col-lg-2 ac" style="">
    <span class="dBlock ac gray small" style="width:30px;">
     -
    </span>
   </p>
  </div>
  <div class="row cf m0Auto" style="font-size:10pt;line-height:1.6em;">
   <p class="col-lg-1 fs08e semi-bold dark-gray al">
    5
   </p>
   <p class="col-lg-7 ellipses">
    <a class="semi-bold fs09e" href="/players/france/arnold-temanfo">
     <span class="mr05 flag o8 flag-1 flag-fr-12">
     </span>
     Arnold Temanfo
    </a>
   </p>
   <p class="col-lg-2 ac fs08e semi-bold">
    RB
   </p>
   <p class="col-lg-2 ac" style="">
    <span class="dBlock ac gray small" style="width:30px;">
     -
    </span>
   </p>
  </div>
  <div class="row cf m0Auto" style="font-size:10pt;line-height:1.6em;">
   <p class="col-lg-1 fs08e semi-bold dark-gray al">
    13
   </p>
   <p class="col-lg-7 ellipses">
    <span class="semi-bold fs09e">
     <span class="mr05 flag o8 flag-1 flag-fr-12">
     </span>
     Souleymane Cissé
    </span>
   </p>
   <p class="col-lg-2 ac fs08e semi-bold">
    -
   </p>
   <p class="col-lg-2 ac" style="">
    <span class="dBlock ac gray small" style="width:30px;">
     -
    </span>
   </p>
  </div>
  <div class="row cf bbox">
   <p class="col-lg-4 fs08e semi-bold" style="height:28px;line-height:28px;">
    Goalkeeper
   </p>
   <div class="col-lg-8 pr" height="38px;">
    <div class="w100 pa" style="top:12px;height:1px;background:#ddd;">
    </div>
   </div>
  </div>
  <div class="row cf m0Auto" style="font-size:10pt;line-height:1.6em;">
   <p class="col-lg-1 fs08e semi-bold dark-gray al">
    40
   </p>
   <p class="col-lg-7 ellipses">
    <span class="semi-bold fs09e">
     <span class="mr05 flag o8 flag-1 flag-fr-12">
     </span>
     Robin Risser
    </span>
   </p>
   <p class="col-lg-2 ac fs08e semi-bold">
    -
   </p>
   <p class="col-lg-2 ac" style="">
    <span class="dBlock ac gray small" style="width:30px;">
     -
    </span>
   </p>
  </div>
 </div>
 <div class="w100 fl mt15e rw100 m0Auto cf club-blue-highlight br4 bbox" style="font-size:8.5pt;">
  <p class="col-lg-1 semi-bold lh14e">
   #
  </p>
  <p class="col-lg-11 semi-bold lh14e">
   Substitutes
  </p>
 </div>
 <div class="w100 fl rw100 m0Auto bbox">
  <div class="row cf bbox">
   <p class="col-lg-4 fs08e semi-bold" style="height:28px;line-height:28px;">
    Forwards
   </p>
   <div class="col-lg-8 pr" height="38px;">
    <div class="w100 pa" style="top:13px;height:1px;background:#ddd;">
    </div>
   </div>
  </div>
  <div class="row cf m0Auto" style="font-size:10pt;line-height:1.6em;">
   <p class="col-lg-1 fs08e semi-bold dark-gray al">
    19
   </p>
   <p class="col-lg-7 ellipses">
    <a class="semi-bold fs09e" href="/players/france/joseph-mendes">
     <span class="mr05 flag o8 flag-1 flag-fr-12">
     </span>
     Joseph Mendes
    </a>
    <span class="dark-gray ml03 bold">
     ↑
    </span>
   </p>
   <p class="col-lg-2 ac fs08e semi-bold">
    CF
   </p>
   <p class="col-lg-2 ac" style="">
    <span class="dBlock ac gray small" style="width:30px;">
     -
    </span>
   </p>
  </div>
  <div class="row cf bbox">
   <p class="col-lg-4 fs08e semi-bold" style="height:28px;line-height:28px;">
    Midfielders
   </p>
   <div class="col-lg-8 pr" height="38px;">
    <div class="w100 pa" style="top:12px;height:1px;background:#ddd;">
    </div>
   </div>
  </div>
  <div class="row cf m0Auto" style="font-size:10pt;line-height:1.6em;">
   <p class="col-lg-1 fs08e semi-bold dark-gray al">
    25
   </p>
   <p class="col-lg-7 ellipses">
    <span class="semi-bold fs09e">
     <span class="mr05 flag o8 flag-1 flag-gp-12">
     </span>
     Zoran Christophe Moco
    </span>
    <span class="dark-gray ml03 bold">
     ↑
    </span>
   </p>
   <p class="col-lg-2 ac fs08e semi-bold">
    -
   </p>
   <p class="col-lg-2 ac" style="">
    <span class="dBlock ac gray small" style="width:30px;">
     -
    </span>
   </p>
  </div>
  <div class="row cf m0Auto" style="font-size:10pt;line-height:1.6em;">
   <p class="col-lg-1 fs08e semi-bold dark-gray al">
    29
   </p>
   <p class="col-lg-7 ellipses">
    <a class="semi-bold fs09e" href="/players/cameroon/cyrille-loic-onana-etoga">
     <span class="mr05 flag o8 flag-1 flag-cm-12">
     </span>
     Cyrille Loic Onana Etoga
    </a>
    <span class="dark-gray ml03 bold">
     ↑
    </span>
   </p>
   <p class="col-lg-2 ac fs08e semi-bold">
    -
   </p>
   <p class="col-lg-2 ac" style="">
    <span class="dBlock ac gray small" style="width:30px;">
     -
    </span>
   </p>
  </div>
  <div class="row cf m0Auto" style="font-size:10pt;line-height:1.6em;">
   <p class="col-lg-1 fs08e semi-bold dark-gray al">
    28
   </p>
   <p class="col-lg-7 ellipses">
    <a class="semi-bold fs09e" href="/players/france/bryan-soumare">
     <span class="mr05 flag o8 flag-1 flag-fr-12">
     </span>
     Bryan Soumaré
    </a>
    <span class="dark-gray ml03 bold">
     ↑
    </span>
   </p>
   <p class="col-lg-2 ac fs08e semi-bold">
    CAM
   </p>
   <p class="col-lg-2 ac" style="">
    <span class="dBlock ac gray small" style="width:30px;">
     -
    </span>
   </p>
  </div>
  <div class="row cf bbox">
   <p class="col-lg-4 fs08e semi-bold" style="height:28px;line-height:28px;">
    Defenders
   </p>
   <div class="col-lg-8 pr" height="38px;">
    <div class="w100 pa" style="top:12px;height:1px;background:#ddd;">
    </div>
   </div>
  </div>
  <div class="row cf m0Auto" style="font-size:10pt;line-height:1.6em;">
   <p class="col-lg-1 fs08e semi-bold dark-gray al">
    2
   </p>
   <p class="col-lg-7 ellipses">
    <a class="semi-bold fs09e" href="/players/ivory-coast/adama-fofana">
     <span class="mr05 flag o8 flag-1 flag-ci-12">
     </span>
     Adama Fofana
    </a>
    <span class="dark-gray ml03 bold">
     ↑
    </span>
   </p>
   <p class="col-lg-2 ac fs08e semi-bold">
    LB
   </p>
   <p class="col-lg-2 ac" style="">
    <span class="dBlock ac gray small" style="width:30px;">
     -
    </span>
   </p>
  </div>
  <div class="row cf bbox">
   <p class="col-lg-4 fs08e semi-bold" style="height:28px;line-height:28px;">
    Goalkeeper
   </p>
   <div class="col-lg-8 pr" height="38px;">
    <div class="w100 pa" style="top:12px;height:1px;background:#ddd;">
    </div>
   </div>
  </div>
 </div>
</div>"""


def getLineups(url):
    
    finalURL = "https://footystats.org" + url
    logging.info("Getting lineups for match: " + finalURL)
    response = requests.get(finalURL, cookies=cookies, headers=headers)
    ##print(response.text)
    if response.status_code != 200:
        logging.error("Error in getLineups", str(response.json()))
        return
    soup = BeautifulSoup(response.text, "html.parser")
    team1 = soup.find("div", class_="rw100 fl")
    if (team1 == None):
        logging.error("Error in getInfos", "team1 is None. No lineups found")
        return False
    res1 = getTeamInfos(team1)
    team2 = soup.find("div", class_="rw100 fr rmt2e")
    if (team2 == None):
        logging.error("Error in getInfos", "team2 is None. No lineups found")
        return False
    res2 = getTeamInfos(team2)
    return res1, res2


def getTeamInfos(div):
    res = dict()
    data = div.text
    name, starting, substitutes = data.split("#")
    print("Name:", name)
    res["name"] = name
    ##print("Starting:", starting)
    ##print("Substitutes:", substitutes)
    forward, rest = starting.split("Midfielders")
    midfield, rest = rest.split("Defenders")
    defenders, goalkeeper = rest.split("Goalkeeper")

    forward = forward.replace("Starting 11", "")
    forward = forward.replace("Forwards", "")

    starting = dict()
    starting["forward"] = forward
    starting["midfield"] = midfield
    starting["defenders"] = defenders
    starting["goalkeeper"] = goalkeeper

    forward, rest = substitutes.split("Midfielders")
    midfield, rest = rest.split("Defenders")
    defenders, goalkeeper = rest.split("Goalkeeper")

    forward = forward.replace("Substitutes", "")
    forward = forward.replace("Forwards", "")

    substitutes = dict()
    substitutes["forward"] = forward
    substitutes["midfield"] = midfield
    substitutes["defenders"] = defenders
    substitutes["goalkeeper"] = goalkeeper

    print("Starting:", starting)
    print("Substitutes:", substitutes)

    res["starting"] = starting
    res["substitutes"] = substitutes
    return res


def exploreData():
    with open("DataGathering/footyStats/response.txt", "r") as f:
        data = f.read()
    soup = BeautifulSoup(data, "html.parser")
    lineups = soup.find("div", class_="row cf mt1e r-m0")
    ##print(lineups)
    team1 = soup.find("div", class_="rw100 fl")
    res = getTeamInfos(team1)
    team2 = soup.find("div", class_="rw100 fr rmt2e")
    res = getTeamInfos(team2)



if __name__ == "__main__":
    getLineups(
        "france/as-saint-etienne-vs-paris-fc-h2h-stats#"
    )
