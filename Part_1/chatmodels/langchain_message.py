from dotenv import load_dotenv
load_dotenv()

from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain.chat_models import init_chat_model

model = init_chat_model("gpt-5.4-mini")
# langchain msg is better choice bcz each model has their own role name like google say model then openai say assistant using list need to translate manual but this handle automatically and fully compatiable with reduce and give built in features like tool calling

human_msg = HumanMessage("difference between acceleration and velocity")


print("----- to exit enter 0 ----")
print("----- For Biology teacher press 1, Physics 2, Chemistry 3 -----")

pressed_value = int(input("Press value: "))

if pressed_value == 1:
    sys_msg = "You are a best biology teacher that take mostly example from humans to example students"
elif pressed_value == 2:
    sys_msg = "You are a best physics professor that take mostly example from space and universe to example students"
else:
    sys_msg = "You are a best chemistry professor that take mostly example from daily used home products to example students"

message = [
    SystemMessage(content=sys_msg)
]

while True:
    human_msg = input("You: ")
    if human_msg == "0":
        break

    message.append(HumanMessage(human_msg))
    res = model.invoke(message)
    print("Bot: ", res.content)

    message.append(AIMessage(res.content))
    print(message)


# types of prompting: simple(giving a ques), sys+user prompt(setting behavior then asking), template prompt(using placeholder inside prompts), structured output(output in json/bullet or fixed format)