# problem statement: Build a movie information processing system that converts raw movie descriptions into structured JSON containing key details and a clean summary, and stores the result in a database.
from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

model = ChatGroq(model="groq/compound-mini")

# here u don't required to give ai-message bcz AI message is useful when you want to give the model an example of how an assistant previously responded
prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
You are an AI assistant specialized in extracting
structured information from movie descriptions.

Your task is to analyze the user's raw movie paragraph and extract
exactly these 7 important fields:

1. title
2. director
3. cast
4. release_year
5. genre
6. rating
7. summary

Follow these rules:
- Use only information explicitly mentioned in the paragraph.
- Never invent or assume information.
- If information is missing, return null.
- cast must be a list of names.
- genre must be a list of genres.
- rating should be a numerical value if mentioned.
- release_year should be a number if mentioned.
- summary should be a concise 2-3 sentence summary.
- Return ONLY valid JSON.
- Do not include markdown or explanations.

Return the following structure:

{{
    "title": "...",
    "director": "...",
    "cast": ["..."],
    "release_year": 0,
    "genre": ["..."],
    "rating": 0.0,
    "summary": "..."
}}
"""
    ),
    (
        "human",
        """
Extract the movie information from this paragraph:

{movie_text}
"""
    )
])



movie_summary = input("Enter your movie summary: ")

msg = prompt.invoke({"movie_text": movie_summary})
print("msg: ", msg)

res = model.invoke(msg)
print("ai: ", res.content)

