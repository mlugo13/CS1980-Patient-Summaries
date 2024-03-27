import sys
import subprocess
import os
import importlib.util
import re
from getpass import getpass
import replicate

spec = importlib.util.find_spec("whisper")
whisper_installed = spec is not None
#installs whisper if not installed, you may need to replace pip3 with pip depending on your python version
if not whisper_installed:
    subprocess.run(["pip3", "install", "-U", "openai-whisper"])
import whisper

model = whisper.load_model("base")
prompts = ["Does the student introduce themselves?: ", 
           "Does the student ask the patient about allergies?: ", 
           "Does the student tell the patients how much medication to take?: "]

def format_text(long_string):
    # Define a regular expression pattern to match the end of a sentence
    sentence_end_pattern = r'(?<=[.!?]) +'
    # Use the pattern to split the string into sentences
    sentences = re.split(sentence_end_pattern, long_string)
    # Join the sentences with a newline character
    new_string = '\n'.join(sentences)

    return new_string

def whisper_read():
    filename = input("Please enter mp3/mp4/wav file to be transcribed: ")
    text = model.transcribe("../samples/" + filename,fp16=False)["text"];
    out = format_text(text)

    txt_file = open(filename[0:filename.find('.')] + "_transcript.txt", "w")
    txt_file.write(out)
    txt_file.close()
    return text

cont = True
while(cont):
    REPLICATE_API_TOKEN = input("What is your Replicate API token?: ")
    os.environ["REPLICATE_API_TOKEN"] = REPLICATE_API_TOKEN

    transcription = whisper_read()

    count = 1;
    for prompt in prompts:
        print("\n" + str(count) +") " + prompt)
        for event in replicate.stream(
            "meta/llama-2-70b-chat",
            input={
                "debug": False,
                "top_p": 1,
                "prompt": "yes or no, " + prompt + transcription,
                "temperature": 0.5,
                "system_prompt": "you are a auto grader analyzing a conversation betweena pharmacist student and a mock patient",
                "max_new_tokens": 100,
                "min_new_tokens": -1,
                "prompt_template": "[INST] <<SYS>>\n{system_prompt}\n<</SYS>>\n\n{prompt} [/INST]",
                "repetition_penalty": 1.15
            },
        ):
            print(str(event), end="")
        count+=1
    
    s = input("\nWould you like to grade another interaction (yes/no)?: ")
    if(s.lower() != "yes"):
        cont=False 