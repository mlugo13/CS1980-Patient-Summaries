import google.generativeai as palm
import asyncio
from pyppeteer import launch

API_KEY = "AIzaSyBjRfI0lBWU37_4IZ2y1hMqJhYgtAeGQy0"
palm.configure(api_key = API_KEY)

def summarize(text, model):
    prompt = ("I have text that is a conversation between a mdedical practitioner and a patient. I want you to summaraize and identify the key points that were discussed. Include details like what the main medicine the convesation was about, and the key point the patient should know for safely using that medicine")

    completion = palm.generate_text(
        model=model,
        prompt=prompt,
        #higher value -> more variability
        #temperature=0,
        #max character output
        max_output_tokens=800
    )

    return completion.result

models = [
    m for m in palm.list_models() if "generateText" in m.supported_generation_methods
]
model = models[0].name
print("using model: ", model)

data = ""
with open('text_samples/osce2_transcript.txt', 'r') as file:
    data = file.read().rstrip()

summary_string = summarize(data, model)
print(summary_string)