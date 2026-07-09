import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

llm = ChatOpenAI(
    model=os.getenv("TOKENLAB_MODEL", "gpt-5.4"),
    api_key=os.environ["TOKENLAB_API_KEY"],
    base_url="https://api.tokenlab.sh/v1",
)

response = llm.invoke("Explain TokenLab in one sentence.")
print(response.content)
