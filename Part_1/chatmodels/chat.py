from dotenv import load_dotenv
load_dotenv()

from langchain.chat_models import init_chat_model

model = init_chat_model('gpt-5.4-mini')
# res = model.invoke("where is mumbai")

print(model)