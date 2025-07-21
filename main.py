# main.py

import openai
from tts import Millow_TTS
from web_search_handler import WebSearchHandler
from news_fetcher import NewsFetcher
from command_router import CommandRouter
from listener import MillowListener

# API Keys
openai.api_key = "YOUR_OPENAI_KEY"
news_api_key = "3dfced98481646a3b6f7617f3b3fc518"

# Modules
tts = Millow_TTS()
speak = tts.speak
search_handler = WebSearchHandler(speak_func=speak)
news_handler = NewsFetcher(speak_func=speak, api_key=news_api_key)
listener = MillowListener(wake_word="millow")

# GPT
def ask_gpt(question):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": question}]
        )
        return response.choices[0].message.content
    except Exception as e:
        print("[GPT ERROR]", e)
        return "Sorry, I couldn't think properly."

# Command Router
router = CommandRouter(
    search_handler=search_handler,
    news_handler=news_handler,
    gpt_func=ask_gpt,
    speak_func=speak
)

# Continuous Loop
if __name__ == "__main__":
    speak("Hello Master, I am Millow. Say 'Millow' to wake me up!")

    while True:
        if listener.listen_for_wake_word():
            speak("Yes Master?")
            user_command = listener.listen_command()
            if user_command:
                router.route(user_command)

