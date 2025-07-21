# Project_05
<h1 align="center">🎙️ Millow: AI Voice Assistant</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11+-blue.svg" />
  <img src="https://img.shields.io/badge/Made%20with-%E2%9D%A4-red.svg" />
  <img src="https://img.shields.io/badge/Platform-Windows-green.svg" />
  <img src="https://img.shields.io/badge/Author-Shubh%20Mohan-blueviolet.svg" />
</p>

> 🔊 Millow is a modular, real-time AI-powered voice assistant that responds to your voice, plays background music, answers questions using ChatGPT, fetches news, searches the web, and much more — all while being interruptible and interactive!

---

## 🚀 Features

| Category | Feature |
|---------|---------|
| 🎤 Voice Control | Wake word activation ("Millow") |
| 💬 Speech Engine | Uses `pyttsx3` with dynamic voice, rate, and gender support |
| 🗣️ Speak Interrupt | Stop speech mid-sentence using voice commands like "Stop Millow" |
| 🎵 Background Music | Fade music in/out while speaking with smooth volume transition |
| 🌐 Web Control | Commands like "Open YouTube", "Play Music", "Search Google" |
| 🧠 AI Powered | Integrates ChatGPT (`gpt-3.5-turbo`) to answer complex queries |
| 📰 News Updates | Real-time news fetching using NewsAPI |
| 🎯 Modular Design | Each feature is class-based and independently upgradable |

---

## 🧠 Tech Stack

- **Python 3.11+**
- `pyttsx3` for TTS
- `speech_recognition` for voice input
- `pygame` for audio & music
- `webbrowser` for command execution
- `openai` for GPT integration
- `requests` for News API

---

## 🗂️ Folder Structure

Project_05/ <br>
├── main.py <br>
├── millow_tts.py <br>
├── millow_listener.py <br>
├── web_search_handler.py <br>
├── command_router.py <br>
├── news_fetcher.py <br>
├── assets/ <br>
│ └── bg_music.mp3 <br>
├── README.md <br>
└── requirements.txt <br>


---

## ⚙️ Setup Instructions

1. **Clone the repo**  
   ```bash
   git clone https://github.com/shubhmohan/Project_05.git
   cd Project_05
2. Install dependencies <br>
   ```bash
   pip install -r requirements.txt
3. Add your API Keys <br>
  • Set your OpenAI API Key in ```main.py ``` <br>
  • Set your NewsAPI key in ```news_fetcher.py``` <br>

4. Run it
   ```bash
   python main.py 

 --- 

## 🧪 Example Commands 

```bash
 "Millow"                     --> Wake the assistant
"Open YouTube"              --> Opens YouTube in browser
"Play Music"                --> Plays background music
"Tell me a joke"            --> Uses GPT to answer
"What's the latest news?"   --> Fetches top headlines
"Stop Millow"               --> Interrupts speech
```
---

## 🌟 Show your support
If you liked the project, drop a ⭐ star on the repo. It really helps and motivates more upgrades.

---

## 🧑‍💻About Me
Shubh Mohan <br>
💼 Aspiring AI/ML Engineer | 🎓 Tech Enthusiast | 🛠️ Passionate Python Developer <br>

📫 GitHub:shubh_mohan | LinkedIn: www.linkedin.com/in/shubh-mohan-3ab78336a
