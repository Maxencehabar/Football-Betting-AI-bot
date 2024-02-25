import os
import requests
import logging

logging.basicConfig(level=logging.INFO)

headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + os.getenv("OPEN_AI_API_KEY"),
}

with open("chatGPT/preprompt.txt", "r") as f:
    preprompt = f.read()


def Analyse(match, stats):
    json_data = {
        "model": "gpt-4",
        "messages": [
            {
                "role": "system",
                "content": preprompt,
            },
            {
                "role": "user",
                "content": f"{match} Here are the stats : {stats}. Now analyse the data.",
            },
        ],
    }

    response = requests.post(
        "https://api.openai.com/v1/chat/completions", headers=headers, json=json_data
    )

    # print(response.json())
    logging.info(response.status_code)

    if response.status_code == 429:
        logging.error("Rate limit exceeded")
        return "Rate limit exceeded"

    if response.status_code != 200:
        logging.error(response.json())

        return "Server error : status code " + str(response.status_code)
    try:
        res = response.json()["choices"][0]["message"]["content"]
        print(res)
        return res
    except Exception as e:
        logging.error(response.json())
        logging.error("Can't access response")
        return e


if __name__ == "__main__":
    Analyse(match="Here are the stats", stats="salut")
