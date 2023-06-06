

from dotenv import load_dotenv
load_dotenv()

from utils.openai import *

if __name__ == "__main__":
    try:
        print("Press and Hold Right Shift to record audio")
        while True:
            message = input("You :")
            response = send_message(message)
            print("Asaka : "+response)
    except:
        print("Stop")
