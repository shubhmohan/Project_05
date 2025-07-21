
class CommandRouter:
    def __init__(self, search_handler, news_handler, gpt_func, speak_func):
        self.search_handler = search_handler
        self.news_handler = news_handler
        self.gpt_func = gpt_func
        self.speak = speak_func

    def route(self, user_command):
        command = user_command.lower()

        if "open" in command or "play" in command or "search" in command:
            self.search_handler.search(command)

        elif "news" in command:
            self.news_handler.fetch_top_news()

        elif "what" in command or "who" in command or "define" in command or "tell me" in command:
            self.speak("Thinking, Master...")
            response = self.gpt_func(command)
            self.speak(response)

        else:
            self.speak("Sorry Master, I didn't understand. Please try again.")
