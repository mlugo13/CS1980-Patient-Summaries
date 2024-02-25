import subprocess
import importlib.util
spec = importlib.util.find_spec("whisper")
whisper_installed = spec is not None
#installs whisper if not installed, you may need to replace pip3 with pip depending on your python version
if not whisper_installed:
    subprocess.run(["pip3", "install", "-U", "openai-whisper"])
import whisper

def whisper_read(filename):
    model = whisper.load_model("base")
    result = model.transcribe("../samples/" + filename)
    return result

filename = input("Please enter mp3/mp4/wav file to be transcribed: ")
transcript = whisper_read(filename)

txt_file = open("transcribed_audio/" + filename[0:filename.find('.')] + "_transcript.txt", "w")
txt_file.write(transcript["text"])
txt_file.close()