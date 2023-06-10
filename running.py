import keyboard
from dotenv import load_dotenv
load_dotenv()

from utils.openai import *
from utils.audio import *
from utils.subtitle import *
from utils.translate import *
from utils.tts import *

if __name__ == "__main__":
    try:
        print("Press and Hold Right Shift to record audio")
        while True:
            if keyboard.is_pressed('RIGHT_SHIFT'):
                message = speech_to_text()
                # message = input("masukkan :")
                if message == '':
                    continue

                generate_subtitle("input.txt", message)
                response = send_message(message)
                generate_subtitle("output.txt", response)

                detect = detect_google(response)
                edgetts_tts(response, detect)
                print("You   : "+message)
                print("Asaka : "+response)

                
                generate_subtitle("input.txt", '')
                generate_subtitle("output.txt", '')
                

    except:
        print("Stop")
