from googletrans import Translator

def translate_to_en(message):
    try:
        detect = detect_google(message)
        # tts = translate_google(message, f"{detect}", "JA")
        tts_en = translate_google(message, f"{detect}", "EN")
        return tts_en
    except:
        print("error translate")
        return message

def translate_to_id(message):
    try:
        detect = detect_google(message)
        # tts = translate_google(message, f"{detect}", "JA")
        tts_en = translate_google(message, f"{detect}", "ID")
        return tts_en
    except:
        print("error translate")
        return message


def translate_google(text, source, target):
    try:
        translator = Translator()
        result = translator.translate(text, src=source, dest=target)
        return result.text
    except:
        print("Error translate")
        return text
    
def detect_google(text):
    try:
        translator = Translator()
        result = translator.detect(text)
        return result.lang.upper()
    except:
        print("Error detect")
        return 'ID'