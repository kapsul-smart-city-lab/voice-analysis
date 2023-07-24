import speech_recognition as sr


class Listener:
    def __init__(self, callback: callable=print) -> None:
        self.callback = callback

    def listen(self) -> None:
        self.recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            self.microfone = source
            while True:
                text = self.audio_to_text("dinleniyor (tüm sesler)", phrase_time_limit=4)

                if "hey kapsül" in text.lower():
                    print("anahtar kelime tespit edildi: ", text)

                    text = self.audio_to_text("dinleniyor (prompt)",
                                        timeout=5, phrase_time_limit=5)

                    self.callback(text)

                else:
                    print("anahtar kelime tespit edilemedi...", text)

    def audio_to_text(self, info: str, **kwargs) -> str:
        print(info)
        audio = self.recognizer.listen(self.microfone, **kwargs)

        print("tanımlanıyor...")
        return self.recognizer.recognize_google(
            audio, language="tr-TR"
        ) 


def prompt_catcher():
    listener = Listener()

    while True:
        try:
            listener.listen()
        except Exception as e:
            print("Error:",type(e), e)


if __name__ == "__main__":
    prompt_catcher()