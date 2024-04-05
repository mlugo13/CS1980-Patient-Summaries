# CS1980-Patient-Summaries

### Samples
contains mp3/mp4/wav and other audio/video files to use as sample input.

### Text Processing
currently has a palm file with sample summarization code. Not very functional (better computer?)
requirements.txt has the dependancies to run it

there is a llama2 sample file in google collab, but trying to run in on large inputs needs more ram usage
https://colab.research.google.com/drive/12WHXcR4LTz27YXd5UQ6_EYSWint7nPfq?usp=sharing

Working: Replicate API
https://colab.research.google.com/drive/1zW8KBMTM-5A8nQtNR56GuEqRiESB_dfN?usp=sharing
needs toekn from replicate, currently seems to be working without any space constraints, needs testing locally

### Whisper
currently has a whisperReader.py file that takes in audio/video from the samples folder and writes 
the transcription in a single line that goes to the text_samples folder
has a whisperX.py file that isn't currently functional. But a working whisperX file can be run
on google collab notebook using this link:
https://colab.research.google.com/drive/1jbywLUXtz--b-47n_oZV1gkAh9Ou38KP?usp=sharing
have to go to runtime>change runtime type>T4 GPU
also have to put sample files into the files section on the left every time
speaker recognition doesn't seem to be super accurate

Both the whisper and text processing files have (Marlon)'s authentification token, from huggingface

### Grading

Demo grading file in google collab:
https://colab.research.google.com/drive/19frvTdkotre1146K0wllVx4xNM8uCb8t?usp=sharing
