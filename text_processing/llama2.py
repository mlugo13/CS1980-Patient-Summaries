import subprocess

packages_to_install = ["transformers", "einops", "accelerate", "langchain", "bitsandbytes"]

for package in packages_to_install:
    subprocess.run(["pip3", "install", "-q", package])

#login to huggingface
subprocess.run(["huggingface-cli", "login"])

subprocess.run(["pip3", "install", "-q", "sentencepiece"])

from langchain import HuggingFacePipeline
from transformers import AutoTokenizer
import transformers
import torch

model = "meta-llama/Llama-2-7b-chat-hf"

tokenizer = AutoTokenizer.from_pretrained(model)

pipeline = transformers.pipeline(
    "text-generation", #task
    model=model,
    tokenizer=tokenizer,
    torch_dtype=torch.bfloat16,
    trust_remote_code=True,
    device_map=0,
    max_length=500,
    do_sample=True,
    top_k=10,
    num_return_sequences=1,
    eos_token_id=tokenizer.eos_token_id
)

llm = HuggingFacePipeline(pipeline = pipeline, model_kwargs
= {'temperature':0})

from langchain import PromptTemplate,  LLMChain

template = """
              Identify whether or not the pharmasist introduced themselves to the patient. If they did, print out yes. if not, just print no.
              ```{text}```
           """

prompt = PromptTemplate(template=template, input_variables=["text"])

llm_chain = LLMChain(prompt=prompt, llm=llm)

text = " Hi, my name is Mark and I'm the intern pharmacist today. Are you miss Jordan Davis? I am. Great."

print(llm_chain.invoke(text))