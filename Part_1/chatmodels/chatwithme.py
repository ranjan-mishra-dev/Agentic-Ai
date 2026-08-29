from dotenv import load_dotenv
load_dotenv()

from langchain.chat_models import init_chat_model
from langchain_groq import ChatGroq

model = ChatGroq(model="qwen/qwen3.6-27b")

# types of achieve this memory: using LIST(where we keeping & feeding prev chat), messages 
# dis of using list is it can reach a limit approx to ur left ram size and it is not a sustainable way, that's why we have messages in langchain

message_history = []
print("---to exit enter 0 ---")
while True:
    msg = input('You: ')
    message_history.append({"User": msg})
    if msg == "0":
        break

    res = model.invoke(message_history)
    message_history.append({"Bot": res.content})
    print("Bot: ", res.content)
    print(message_history)

# currently problem facing is this bot doesn't have memory means what we talk in prev chat he doesn't remember
