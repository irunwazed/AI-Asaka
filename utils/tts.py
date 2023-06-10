
from playsound import playsound
import pyttsx3
import torch
import winsound
import os

from gtts import gTTS
import edge_tts
import asyncio

import ffmpeg_downloader as ffdl
import subprocess as sp

print("TTS CLASS")
def coba_tts():
    print("aka")

def play_mp3(name):
    if os.path.exists(name+'.wav'):
        os.remove(name+".wav")
    sp.run([ffdl.ffmpeg_path, '-i', name+'.mp3', name+'.wav'])
    winsound.PlaySound(name+".wav", winsound.SND_FILENAME)
    os.remove(name+".mp3")

async def edge_tts_main(text, voice = 'id-ID-ArdiNeural') -> None:
    # VOICE = "id-ID-GadisNeural"
    # en-ZA-LukeNeural
    OUTPUT_FILE = "output.mp3"
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save(OUTPUT_FILE)
    
    play_mp3("output")

def edgetts_tts(text, lang = 'ID'):
    voice_index = 0
    if lang == 'EN':
        voice_index = 1
    elif lang == 'JA':
        voice_index = 2

    VOICE = ["id-ID-ArdiNeural", "en-US-ChristopherNeural", "ja-JP-KeitaNeural"]
    asyncio.run(edge_tts_main(text, VOICE[voice_index]))

def pyttsx3_tts(text):
    engine = pyttsx3.init()

    # rate = engine.getProperty("rate")
    # voice = engine.getProperty("voice")
    # print(voice)

    engine.setProperty("rate", 140)

    engine.say(text)
    engine.runAndWait()

def google_tts(text, language = 'id'):
    # # Initialize gTTS with the text to convert
    speech = gTTS(text=text, lang=language)

    # # Save the audio file to a temporary file
    speech_file = 'output.mp3'
    speech.save(speech_file)

    # playsound(speech_file)
    
    play_mp3("output")
   


def silero_tts(tts, language = 'en', model = 'v3_en', speaker = 'en_1'):
    try:
        device = torch.device('cpu')
        torch.set_num_threads(4)
        local_file = 'v3_en.pt'
        
        # if not os.path.isfile(local_file):
        #     torch.hub.download_url_to_file(f'https://models.silero.ai/models/tts/{language}/{model}.pt',
        #                                 local_file)  

        model = torch.package.PackageImporter(local_file).load_pickle("tts_models", "model")
        model.to(device)

        sample_rate = 48000

        audio_paths = model.save_wav(text=tts,
                                    speaker=speaker,
                                    sample_rate=sample_rate)

        winsound.PlaySound("test.wav", winsound.SND_FILENAME)
    except:
        print("error create sound")
