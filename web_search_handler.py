import webbrowser
import pygame

class WebSearchHandler:
    def __init__(self, speak_func):
        """
        :param speak_func: A function to convert text-to-speech (like MillowTTS.speak)
        """
        self.speak = speak_func
        self.music_file = "path_to_your_music_file.mp3"  # Optional local file

    def openai_answer(self, question, openai_api):
        try:
            response = openai_api.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": question}
                ]
            )
            return response.choices[0].message.content
        except Exception as e:
            self.speak("Sorry, I couldn't get a response from GPT.")
            print("[OpenAI ERROR]", e)
            return "Something went wrong."

    def search(self, say):
        say = say.lower()

        commands = {
            "open youtube": "https://www.youtube.com",
            "open gmail": "https://mail.google.com",
            "open instagram": "https://www.instagram.com",
            "open facebook": "https://www.facebook.com",
            "open linkedin": "https://www.linkedin.com",
            "open x": "https://www.x.com",
            "play sorry sorry": "https://youtu.be/az2KIZbS47Y?si=f_4AeI7t2yg8x4zo",
            "play bhojpuri songs": "https://youtube.com/playlist?list=RDaz2KIZbS47Y&playnext=1"
        }

        for key, url in commands.items():
            if key in say:
                self.speak(f"Opening {key.replace('open ', '').replace('play ', '')} for My Master.")
                webbrowser.open(url)
                return

        if "play music" in say:
            self._play_local_music()
        elif "search" in say:
            self._generic_google_search(say)
        else:
            self.speak("I'm not sure what you want me to do, Master.")

    def _play_local_music(self):
        try:
            pygame.mixer.init()
            pygame.mixer.music.load(self.music_file)
            pygame.mixer.music.play()
            self.speak("Playing music for My Master.")
        except Exception as e:
            self.speak("Sorry, I can't play music right now.")
            print("[Music ERROR]", e)

    def google_search(self, say):
        query = say.replace("search", "").strip()
        if query:
            self.speak(f"Searching Google for {query}")
            webbrowser.open(f"https://www.google.com/search?q={query}")
        else:
            self.speak("What should I search, Master?")
