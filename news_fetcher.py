import requests

class NewsFetcher:
    def __init__(self, speak_func, api_key):
        self.speak = speak_func
        self.api_key = api_key
        self.base_url = "https://newsapi.org/v2/top-headlines"
        self.country = "in"  # You can change this

    def fetch_top_news(self, category="general", max_headlines=3):
        url = f"{self.base_url}?country={self.country}&category={category}&apiKey={self.api_key}"

        try:
            response = requests.get(url)
            data = response.json()

            if data["status"] == "ok":
                headlines = data["articles"][:max_headlines]
                if not headlines:
                    self.speak("No news found, Master.")
                    return

                self.speak(f"Here are the top {len(headlines)} headlines:")
                for article in headlines:
                    self.speak(article["title"])
            else:
                self.speak("Sorry, I couldn't fetch the news.")
        except Exception as e:
            self.speak("An error occurred while fetching the news.")
            print("[News ERROR]", e)
