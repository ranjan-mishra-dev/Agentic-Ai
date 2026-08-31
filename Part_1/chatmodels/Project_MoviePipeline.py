# problem statement: Build a movie information processing system that converts raw movie descriptions into structured JSON containing key details and a clean summary, and stores the result in a database.
import os

from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel
from pymongo import MongoClient


from typing import List, Optional
from langchain_core.output_parsers import PydanticOutputParser


client = MongoClient(os.getenv("MONGODB_URI"))

db = client["movie_database_agenticai"]
collection = db["movies"]

model = ChatGroq(model="groq/compound-mini")

class MovieModel(BaseModel):
    title: str
    director: str
    cast: List[str]
    release_year: Optional[int]
    genre: List[str]
    rating: Optional[float]
    summary: str


parser = PydanticOutputParser(pydantic_object=MovieModel)


# here u don't required to give ai-message bcz AI message is useful when you want to give the model an example of how an assistant previously responded
prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """ You are an AI assistant specialized in extracting structured information from movie descriptions.
Your task is to analyze the user's raw movie paragraph and extract these define information {format_instruction} """
    ),
    (
        "human", """ {movie_text} """
    )
])





movie_summary = input("Enter your movie summary: ")
# print("format instruction: ", parser.get_format_instructions())

msg = prompt.invoke({"movie_text": movie_summary, "format_instruction": parser.get_format_instructions()})
# print("prompt look like: ", msg)

res = model.invoke(msg)
# print("ai: ", res.content)

movie = parser.parse(res.content)
movie_data = movie.model_dump()

result = collection.insert_one(movie_data)

print("\nMovie saved successfully!")
print("MongoDB document ID:", result.inserted_id)


#  Use pydantic when you need reliable structured data(for Validating + Structure)