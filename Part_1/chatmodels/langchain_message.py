from dotenv import load_dotenv
load_dotenv()

from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain.chat_models import init_chat_model

model = init_chat_model("gpt-5.4-mini")
# langchain msg is better choice bcz each model has their own role name like google say model then openai say assistant using list need to translate manual but this handle automatically and fully compatiable with reduce and give built in features like tool calling

sys_msg = SystemMessage("You are a best physics teacher in this world and you teaching every concept like a child with proper defnition, example and use cases")
human_msg = HumanMessage("difference between acceleration and velocity")

message = [
    sys_msg,
]

print("----- to exit enter 0 ----")
while True:
    human_msg = input("You: ")
    if human_msg == "0":
        break

    message.append(HumanMessage(human_msg))
    res = model.invoke(message)
    print("Bot: ", res.content)

    message.append(AIMessage(res.content))
    print(message)