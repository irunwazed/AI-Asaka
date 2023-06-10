
import openai
import os
import json

# Mengatur API key
openai.api_key = os.getenv('OPENAI-KEY')
CHARACTER_NAME = os.getenv('CHARACTER-NAME', "Asaka") 
CHARACTER_HISTORY = os.getenv('CHARACTER-PATH-HISTORY', "./character/asaka/history.json") 
CHARACTER_INFO = os.getenv('CHARACTER-PATH-INFO', "./character/asaka/info.txt") 

conversation = []

def save_history(conversation):
    conversation.pop(0)
    conversation.pop(0)
    # conversation.pop(0)
    # conversation.pop(0)

    while len(conversation) > 50:
        conversation.pop(0)
        
    json_object = json.dumps(conversation, indent=4)
    # Writing to sample.json
    with open(CHARACTER_HISTORY, "w") as outfile:
        outfile.write(json_object)
    
def getPrompt():
    characterInfo = ''
    with open(CHARACTER_INFO, 'r') as file:
        characterInfo = file.read().rstrip()

    # system, assistant, user
    conversation = [
        {"role": "system", "content": characterInfo},
        {"role": "assistant", "content": "Halo nama saya "+CHARACTER_NAME+"! Apa yang bisa saya bantu?."}
    ]

    arr = json.load(open(CHARACTER_HISTORY))
    for i in arr:
        conversation.append(i)
    return conversation

    
# Fungsi untuk mengirim pesan dan mendapatkan respons
def send_message(message):
    response = 'Maaf bisa ulangi?'
    try:
        conversation = getPrompt()
        conversation.append({'role': 'user', 'content': message})
        responseAi = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=conversation,
            max_tokens=128,
            temperature=1,
            top_p=0.9
        )
        response = responseAi['choices'][0]['message']['content']
        conversation.append({'role': 'assistant', 'content': response})
        save_history(conversation)
    except:
        print("error: can't connect to Asaka")

    return response

# def add(message):
#     conversation = getPrompt()
#     conversation.append({'role': 'user', 'content': message})
#     conversation.append({'role': 'assistant', 'content': 'halo juga'})
#     save_history(conversation)

# while True:
#     message = input("masukkan :")
#     add(message)

# save_history()
# arr = json.load(open(CHARACTER_HISTORY))
# # print(arr)

# conversation.append({'role': 'user', 'content': 'message'})
# save_history()
# arr = json.load(open(CHARACTER_HISTORY))
# # print(arr)

