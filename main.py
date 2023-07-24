import speech_recognition as sr

def assistant() -> None:
    while True:
        text = detection("dinleniyor (tüm sesler)", phrase_time_limit=4)

        if "hey kapsül" in text.lower():
            print("anahtar kelime tespit edildi: ", text)

            text = detection("dinleniyor (prompt)", timeout=5, phrase_time_limit=5)

            print("prompt: ", text)

        else:
            print("anahtar kelime tespit edilemedi...", text)

def detection(info: str, **kwargs) -> str:
    print(info)
    audio = r.listen(source, **kwargs)

    print("tanımlanıyor...")
    return r.recognize_google(
         audio, language="tr-TR"
    ) 

with sr.Microphone() as source:
    r = sr.Recognizer()
    while True:
        try:
            assistant()
        except Exception as e:
            print("Error:",type(e), e)