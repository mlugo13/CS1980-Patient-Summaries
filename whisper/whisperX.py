import subprocess
import importlib.util

spec = importlib.util.find_spec("whisperx")
whisperx_installed = spec is not None

#installs whisperx if not installed, you may need to replace pip3 with pip depending on your python version
if not whisperx_installed:
    subprocess.run(["pip3", "install", "--quiet", "git+https://github.com/m-bain/whisperx.git"])

import whisperx
import gc

device = "cpu"
batch_size = 16 # reduce if low on GPU mem
compute_type = "int8" # change to "int8" if low on GPU mem (may reduce accuracy) (try float16?)

audio_file = "../samples/osce2.mp3"

model = whisperx.load_model("base", device, compute_type=compute_type)
audio = whisperx.load_audio(audio_file)
result = model.transcribe(audio, batch_size=batch_size)
print(result["segments"])

#NOT CURRENTLY WORKING

