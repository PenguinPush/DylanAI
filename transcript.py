import io
from pydub import AudioSegment
import speech_recognition as sr
import whisper
import queue
import tempfile
import os
import threading
import click
import torch
import numpy as np
import openai
import glob
from scipy.io.wavfile import write

openai.api_key = "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"

@click.command()
@click.option("--model", default="base", help="Model to use", type=click.Choice(["tiny","base", "small","medium","large"]))
@click.option("--device", default=("cuda" if torch.cuda.is_available() else "cpu"), help="Device to use", type=click.Choice(["cpu","cuda"]))
@click.option("--english", default=True, help="Whether to use English model",is_flag=True, type=bool)
@click.option("--verbose", default=False, help="Whether to print verbose output", is_flag=True,type=bool)
@click.option("--energy", default=1000, help="Energy level for mic to detect", type=int)
@click.option("--dynamic_energy", default=True, is_flag=True, help="Flag to enable dynamic energy", type=bool)
@click.option("--pause", default=0.3, help="Pause time before entry ends", type=float)
@click.option("--save_file",default=False, help="Flag to save file", is_flag=True,type=bool)

def main(model, english,verbose, energy, pause,dynamic_energy,save_file,device):
    #there are no english models for large
    if model != "large" and english:
        model = model + ".en"
    audio_model = whisper.load_model(model).to(device)
    audio_queue = queue.Queue()
    result_queue = queue.Queue()
    threading.Thread(target=record_audio,
                     args=(audio_queue, energy, pause, dynamic_energy, save_file, temp_dir)).start()
    threading.Thread(target=transcribe_forever,
                     args=(audio_queue, result_queue, audio_model, english, verbose, save_file)).start()

    while True:
        text = result_queue.get()
        print(text)
        transcript = open("transcript.txt", "a")
        transcript.write(text + "\n")


def record_audio(audio_queue, energy, pause, dynamic_energy, save_file, temp_dir):
    #load the speech recognizer and set the initial energy threshold and pause threshold
    r = sr.Recognizer()
    r.phrase_threshold = 0.5
    r.pause_threshold = 0.5
    r.non_speaking_duration = 0.5

    with sr.Microphone(sample_rate=16000) as source:
        print("Model Loaded!")
        i = 0
        while True:
            audio = r.listen(source, phrase_time_limit=5, )
            data = io.BytesIO(audio.get_wav_data())
            filename = (f"temp{i}.wav")
            audio_data = filename
            write(filename, 16000, np.frombuffer(audio.frame_data))
            audio_queue.put_nowait(audio_data)

            i += 1

def transcribe_forever(audio_queue, result_queue, audio_model, english, verbose, save_file):
    highest_i = 0
    while True:
        if os.path.exists(filename) and highest_i < i:
            highest_i = i
            audio_file = open(filename, "rb")
            result = openai.Audio.transcribe("whisper-1", audio_file)
            predicted_text = result["text"]
            result_queue.put_nowait(predicted_text)

if __name__ == "__main__":
    i = 0
    temp_dir = tempfile.mkdtemp()
    filename = (f"temp{i}.wav")
    for tempfilename in glob.glob("./temp*"):
        os.remove(tempfilename)
    main()