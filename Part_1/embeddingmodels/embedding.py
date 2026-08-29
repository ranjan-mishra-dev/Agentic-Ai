from dotenv import load_dotenv
load_dotenv()

from langchain_openai import OpenAIEmbeddings
from langchain_google_genai import GoogleGenerativeAIEmbeddings

embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-2")
# u can use Qwen3-Embedding-0.6B model locally its size is 1.3GB if gemini hits its limit or sentence transformer

texts = ["hi i am ranjan", "i am a software engineer", "today day is sunny"]
# vector = embeddings.embed_query("Hi my name is ranjan")

vector = embeddings.embed_documents(texts)
print(f"Dimension: {len(vector[0])}")
print(vector)