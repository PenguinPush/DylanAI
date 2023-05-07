import subprocess

import speech_recognition as sr
import whisper
import queue
import tempfile
import os
import threading
import numpy as np
import openai
import glob
from scipy.io.wavfile import write

import menu_main
from categorization import categorize
from macros import read_info
from chat import chat
from menu_main import main_menu

openai.api_key = "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"

class Variables:
    i = 0
    filename = (f"temp{i}.wav")
    wav_checked = False

def main(model, english,verbose, energy, pause,dynamic_energy,save_file,device):
    audio_model = whisper.load_model(model).to(device)
    audio_queue = queue.Queue()
    result_queue = queue.Queue()
    threading.Thread(target=record_audio,
                     args=(audio_queue, energy, pause, dynamic_energy, save_file, temp_dir)).start()
    threading.Thread(target=transcribe_forever,
                     args=(audio_queue, result_queue, audio_model, english, verbose, save_file)).start()

    while True:
        text = result_queue.get()
        Variables.latestText = text
        if text == "" or text == " ":
            print()
        else:
            print("\n" + text)
            categories = categorize(text)
            #chat(text)

            for key, item in categories.items():
                read_info(key, item, text)
                print(f"{key}: {item}")


def record_audio(audio_queue, energy, pause, dynamic_energy, save_file, temp_dir):
    #load the speech recognizer and set the initial energy threshold and pause threshold
    r = sr.Recognizer()
    r.phrase_threshold = 0.5
    r.pause_threshold = 0.5
    r.non_speaking_duration = 0.5

    with sr.Microphone(sample_rate=32000) as source:
        print("Model Loaded!")
        while True:
            audio = r.listen(source, phrase_time_limit=5)
            data = np.frombuffer(audio.frame_data, np.int16).flatten().astype(np.float32) / 32768.0
            Variables.filename = (f"temp{Variables.i}.wav")
            audio_data = Variables.filename
            write(Variables.filename, 32000, data)
            audio_queue.put_nowait(audio_data)

            try:
                os.remove(f"temp{Variables.i - 2}.wav")
            except OSError:
                pass

            Variables.i += 1
            Variables.wav_checked = False

def transcribe_forever(audio_queue, result_queue, audio_model, english, verbose, save_file):
    Variables.wav_checked = True
    while True:
        if os.path.exists(Variables.filename) and Variables.wav_checked == False:
            Variables.wav_checked = True
            audio_file = open(Variables.filename, "rb")
            result = openai.Audio.transcribe("whisper-1", audio_file)
            predicted_text = result["text"]
            result_queue.put_nowait(predicted_text)

if __name__ == "__main__":

    main_menu()


    temp_dir = tempfile.mkdtemp()
    for tempfilename in glob.glob("./temp*"):
        os.remove(tempfilename)

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Please wait. Calibrating microphone...")
        r.adjust_for_ambient_noise(source, duration=5)

    main(model="base", device="cuda", english=True, verbose=False, energy=1000, dynamic_energy=True, pause=0.3, save_file=False)