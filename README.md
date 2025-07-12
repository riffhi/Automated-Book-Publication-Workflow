# 📚 Automated Book Publication Workflow

A full-stack system that automates the rewriting, reviewing, and versioning of web-based book chapters using AI agents, human feedback, and reinforcement learning.

---

## 🚀 Features

- 🔍 **Web Scraper**: Extracts chapter content and screenshots from public book pages.
- ✍️ **AI Writer & Reviewer**: Uses simulated AI agents to rewrite and refine content.
- 🧠 **Human-in-the-Loop**: Captures user voice input to guide reward-based learning.
- 📈 **RL-Based Reward System**: Computes reward scores based on novelty, readability, and feedback.
- 💾 **ChromaDB Versioning**: Stores multiple rewritten versions with semantic search support.
- 🎙️ **Voice Support**: Uses microphone input and text-to-speech for human interaction.

---

## 🧱 Tech Stack

- **Python** 3.13
- **Playwright** for web scraping
- **BeautifulSoup4** for HTML parsing
- **SpeechRecognition + PyAudio** for voice input
- **pyttsx3** for text-to-speech
- **textstat** for readability metrics
- **ChromaDB** for vector-based versioning
- **Reinforcement Learning** (simulated with reward functions)

---


---

## 🛠 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/automated-book-workflow.git
cd automated-book-workflow
```
### 2.Install Dependencies
```bash
pip install -r requirements.txt
playwright install
```

### 3.Run the app
```bash
python main.py
```

Example URL to test on
https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_1

