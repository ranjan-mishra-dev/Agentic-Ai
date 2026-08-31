from dotenv import load_dotenv
load_dotenv()

from langchain.chat_models import init_chat_model
from langchain_openai import ChatOpenAI

from langchain_mistralai import ChatMistralAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

from langchain_groq import ChatGroq

llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-R1-0528",
    task="text-generation",
)

# model = ChatHuggingFace(llm=llm)


# model = init_chat_model("gpt-5.4-mini");
# model = ChatOpenAI(model='gpt-5.4-mini')

# model = ChatGoogleGenerativeAI(model='gemini-3.1-flash-image')
# model = ChatGoogleGenerativeAI(model='gemini-3.1-flash-image')

# model = ChatGoogleGenerativeAI(model = "mistral-medium-latest", max_retries=2)
# model = ChatGoogleGenerativeAI(model='gemini-3.7-flash', temperature=2.0, max_tokens=100)

model = ChatGroq(model="qwen/qwen3.6-27b")

res = model.invoke('mumbai vs new york')
print(res.content)

print(model)
# res = model.invoke("dubai vs mumbai")
