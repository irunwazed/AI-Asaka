import openai
import pyaudio
import wave
import keyboard
import os

# function to get the user's input audio
def record_audio():
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    WAVE_OUTPUT_FILENAME = "input.wav"
    try:
        p = pyaudio.PyAudio()
        stream = p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)
        frames = []
        # print("Recording...")
        print("\rYou [Recording] : \n", end="", flush=True)

        while keyboard.is_pressed('RIGHT_SHIFT'):
            data = stream.read(CHUNK)
            frames.append(data)
        # print("Stopped recording.")
        stream.stop_stream()
        stream.close()
        p.terminate()
        wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()
    except:
        print("error: record_audio")
        return 0

    return WAVE_OUTPUT_FILENAME

def transcribe_audio(file):
    try:
        audio_file= open(file, "rb")
        transcript = openai.Audio.transcribe("whisper-1", audio_file)
        print(transcript.text)
        return transcript.text
    except:
        print("error : transcribe_audio")
        return ''


def speech_to_text():
    try:
        return transcribe_audio(record_audio())
    except:
        return ''

    