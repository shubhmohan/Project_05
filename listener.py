# millow_listener.py

import speech_recognition as sr

class MillowListener:
    def __init__(self, wake_word="millow" or "milo"):
        self.wake_word = wake_word.lower()
        self.recognizer = sr.Recognizer()

    def listen_for_wake_word(self):
        """Continuously listens until wake word is spoken"""
        with sr.Microphone() as source:
            print("[Millow Listener] 🎧 Waiting for wake word...")
            self.recognizer.adjust_for_ambient_noise(source)

            while True:
                try:
                    audio = self.recognizer.listen(source, timeout=5)
                    query = self.recognizer.recognize_google(audio).lower()
                    print(f"[Wake Listener] Heard: {query}")
                    wake_words = ["millow", "milo", "millo", "mellow"]  # Add variants here
                    if any(w in query for w in wake_words):
                        return True
                except sr.WaitTimeoutError:
                    continue
                except sr.UnknownValueError:
                    continue
                except Exception as e:
                    print("[Millow Listener ERROR]", e)

    def listen_command(self):
        """Listens for the command after wake word is detected"""
        with sr.Microphone() as source:
            print("[Millow Listener] 🎤 Listening for your command...")
            self.recognizer.adjust_for_ambient_noise(source)
            try:
                audio = self.recognizer.listen(source, timeout=6)
                command = self.recognizer.recognize_google(audio).lower()
                print(f"[Command Listener] 🎙️ You said: {command}")
                return command
            except Exception as e:
                print("[Command Listener ERROR]", e)
                return ""
