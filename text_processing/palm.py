import google.generativeai as palm
import asyncio
from pyppeteer import launch

API_KEY = "AIzaSyBjRfI0lBWU37_4IZ2y1hMqJhYgtAeGQy0"
palm.configure(api_key = API_KEY)

def summarize(text, model):
    prompt = "Summarize this conversation between a practitioner and a patient who is recieving information about a new medication they are being perscribed"

    completion = palm.generate_text(
        model=model,
        prompt=prompt,
        #higher value -> more variability
        temperature=1,
        #max character output
        max_output_tokens=600
    )

    return completion.result

models = [
    m for m in palm.list_models() if "generateText" in m.supported_generation_methods
]
model = models[0].name
print("using model: ", model)

data = ""
with open('text_samples/osce1_transcript.txt', 'r') as file:
    data = file.read().rstrip()
#print(data)

summary_string = summarize(data, model)
print(summary_string)