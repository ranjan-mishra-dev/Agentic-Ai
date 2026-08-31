from dotenv import load_dotenv
load_dotenv()

from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
llm = HuggingFacePipeline.from_model_id(
    model_id="google/gemma-2-2b-it",
    task="text-generation",
    pipeline_kwargs=dict(
        max_new_tokens=512,
        do_sample=False,
        repetition_penalty=1.03,
    )
)

model = ChatHuggingFace(llm=llm)
res = model.invoke('who is ceo of google')

print(res.content)
print(model)

# // also i got to know about gated vs ungated and quantized model