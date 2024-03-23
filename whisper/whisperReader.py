#pip install openai-whisper
#MacOS <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED]>
#     to fix: Run Install Certificates.command Macintosh HD/Application/Python3.11
import subprocess
import importlib.util
import re

spec = importlib.util.find_spec("whisper")
whisper_installed = spec is not None
#installs whisper if not installed, you may need to replace pip3 with pip depending on your python version
if not whisper_installed:
    subprocess.run(["pip3", "install", "-U", "openai-whisper"])
import whisper

model = whisper.load_model("base")

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

    txt_file = open("transcribed_audio/" + filename[0:filename.find('.')] + "_transcript.txt", "w")
    txt_file.write(out)
    txt_file.close()
    return out


cont = True
while(cont):
    whisper_read()
    print("Finished Transcribing")
    s = input("Would you like to contine? Yes or No\n")
    if(s.lower() != "yes"):
        cont=False 