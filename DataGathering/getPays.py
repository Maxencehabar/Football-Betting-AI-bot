from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import os
from dotenv import load_dotenv

load_dotenv()

preprompt = """Here is the list of football leagues with official names : {leagues}. Give me the official name of {league} from the list only. If the league isn't in the list, just answer None.
Else, answer only with the official name of the league from the list I gave you. Give the corresponding league's official name."""

template = preprompt

prompt = PromptTemplate(input_variables=["leagues", "league"], template=template)

llm = OpenAI(openai_api_key=os.getenv("OPEN_AI_API_KEY"))

llm_chain = LLMChain(
    llm=llm,
    prompt=prompt,
    verbose=True,
)


def cleanAnswer(answer):
    print(answer[0])
    while answer[0] == "\n" or answer[0] == " ":
        answer = answer[1:]
    print("Answer[0] : ", answer[0])
    return answer


def getLeague(leagues, league):
    res = llm_chain.predict(leagues=leagues, league=league)
    print("Answer : ", res)
    res = cleanAnswer(res)
    print("Answer : ", res)
    return res


if __name__ == "__main__":
    getLeague(
        leagues="Premier League, La Liga, Serie A, Ligue 1, Bundesliga",
        league="Ligue 1",
    )
