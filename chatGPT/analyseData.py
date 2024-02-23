from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import os
from dotenv import load_dotenv
load_dotenv()

with open("chatGPT/preprompt.txt", "r") as f:
    preprompt = f.read()

template = (
    preprompt + """ {match} Here are the stats : {stats}. Now analyse the data."""
)

prompt = PromptTemplate(input_variables=["match", "stats"], template=template)

llm = OpenAI(openai_api_key=os.getenv("OPEN_AI_API_KEY"))

llm_chain = LLMChain(
    llm=llm,
    prompt=prompt,
    verbose=True,
)


def Analyse(match, stats):
    res = llm_chain.predict(match=match, stats=stats)
    print(res)
    return res


if __name__ == "__main__":
    Analyse(match="Here are the stats", stats="salut")
