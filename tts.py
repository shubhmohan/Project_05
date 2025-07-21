import pyttsx3
import speech_recognition as sr
import threading
import pygame
import time

class Millow_TTS:
    def __init__(self, rate=150, voice_pref="english", gender="female", name="Millow", music_path="bg_music.mp3", music_volume=0.5):
        self.engine = pyttsx3.init()
        self.recognizer = sr.Recognizer()
        self.interrupted = False
        self.interrupt_command = ["stop", "shut up", "wait", "cancel", "stop it", "shut it"]

        # Voice setup
        self.set_voice(voice_pref, gender)
        self.engine.setProperty('rate', rate)
        self.engine.connect('started-word', self.on_word)

        # Background music
        self.music_path = music_path
        self.music_volume = music_volume
        if music_path:
            pygame.mixer.init()
            pygame.mixer.music.load(music_path)
            pygame.mixer.music.set_volume(music_volume)

    def set_voice(self, voice_pref="zira", gender="female"):
        voices = self.engine.getProperty('voices')
        for voice in voices:
            if "zira" in voice.name.lower():
                self.engine.setProperty('voice', voice.id)
                print(f"[MillowTTS] ✅ Using voice: {voice.name}")
                return
        print("[MillowTTS] ⚠️ Preferred voice not found, using default.")

    def on_word(self, name, location, length):
        if self.interrupted:
            print("[MillowTTS] 🔕 Interrupted by user.")
            self.engine.stop()

    def listen_for_interrupt(self):
        print("[MillowTTS] 🎤 Listening for interrupt commands...")
        try:
            with sr.Microphone() as source:
                self.recognizer.adjust_for_ambient_noise(source)
                audio = self.recognizer.listen(source, timeout=5)
                command = self.recognizer.recognize_google(audio).lower()
                print(f"[Interrupt] You said: {command}")
                for word in self.interrupt_command:
                    if word in command:
                        self.interrupted = True
                        return
        except sr.WaitTimeoutError:
            print("[MillowTTS] ⏱️ No voice input detected.")
        except sr.UnknownValueError:
            print("[MillowTTS] ❓ Could not understand.")
        except sr.RequestError:
            print("[MillowTTS] ❌ Recognition service error.")
        except Exception as e:
            print("[MillowTTS ERROR]", e)

    def fade_bg_music(self, fade_out=True):
        if self.music_path and pygame.mixer.music.get_busy():
            steps = 10
            for i in range(steps):
                factor = i / steps
                vol = self.music_volume * (1 - factor) if fade_out else factor * self.music_volume
                pygame.mixer.music.set_volume(vol)
                time.sleep(0.05)
            pygame.mixer.music.set_volume(0.05 if fade_out else self.music_volume)

    def speak(self, text):
        """Speak with interrupt and background music fading."""
        self.interrupted = False

        # Start music if not already playing
        if self.music_path and not pygame.mixer.music.get_busy():
            pygame.mixer.music.play(-1)

        self.fade_bg_music(fade_out=True)

        # Start interrupt listening thread
        interrupt_thread = threading.Thread(target=self.listen_for_interrupt)
        interrupt_thread.daemon = True
        interrupt_thread.start()

        print(f"[MillowTTS] 🗣️ Speaking: {text}")
        self.engine.say(text)
        self.engine.runAndWait()

        interrupt_thread.join(timeout=6)  # Wait for interrupt listener to complete
        self.fade_bg_music(fade_out=False)

