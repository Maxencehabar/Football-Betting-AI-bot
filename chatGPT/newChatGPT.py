import os
import requests

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + os.getenv('OPEN_AI_API_KEY'),
}

with open("chatGPT/preprompt.txt", "r") as f:
    preprompt = f.read()

def Analyse(match, stats):
    json_data = {
        'model': 'gpt-3.5-turbo',
        'messages': [
            {
                'role': 'system',
                'content': preprompt,
            },
            {
                'role': 'user',
                'content': f"{match} Here are the stats : {stats}. Now analyse the data.",
            },
        ],
    }

    response = requests.post('https://api.openai.com/v1/chat/completions', headers=headers, json=json_data)

    #print(response.json())
    res = response.json()["choices"][0]["message"]["content"]
    print(res)
    return res

if __name__ == "__main__":
    Analyse(match="Here are the stats", stats="salut")