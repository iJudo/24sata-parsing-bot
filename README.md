# 24satahr Parsing Bot 

A robust asynchronous Telegram bot designed to automatically parse news articles from the Croatian news portal 
[24sata.hr](https://www.24sata.hr), process and summarize them using Google GenAI, store them in an SQLite database, 
and deliver them to users on demand or via scheduled background updates.

---

##  Key Features

* **Automated Web Scraping:** Pulls the latest news articles from 24sata.hr using `BeautifulSoup` and `lxml`. Incorporates `fake-useragent` to rotate HTTP headers and bypass basic anti-scraping blocks.
* **AI-Powered Summarization:** Integrates with the official Google GenAI SDK (`google-genai`) to generate intelligent summaries, translations, or analytical descriptions of parsed news items.
* **Asynchronous Architecture:** Built on `aiogram 3`, providing high performance, non-blocking network operations, and instant command responses.
* **Reliable Data Persistence:** Uses `aiosqlite` for asynchronous interaction with a lightweight SQLite database (`news.sqlite3`).
* **Background Scheduler:** Powered by `apscheduler` to run periodic scraping tasks automatically at specified intervals without blocking the main bot loop.

---

## ⚙ Tech Stack

* **Language:** Python 3.10+ (tested on Python 3.14)
* **Telegram Framework:** `aiogram` (v3)
* **Parsing & Scraping:** `BeautifulSoup4`, `lxml`, `fake-useragent`, `requests` / `aiohttp`
* **AI / LLM:** Google GenAI (`google-genai`)
* **Database:** SQLite with `aiosqlite`
* **Task Scheduling:** `apscheduler`
* **Environment Management:** `python-dotenv`

---

##  Project Architecture & File Structure

```text
24sata-parsing-bot/
│
├── main.py              # Application entry point (initializes bot, database, and scheduler)
├── bot.py               # Telegram bot handlers, routers, and command logic
├── db.py                # Database management module (SQLite connection and queries)
├── ai_description.py    # Integration with Google GenAI API for content processing
├── requirements.txt     # List of project dependencies
├── .env                 # Secret environment variables (not tracked in git)
└── news.sqlite3         # SQLite database file (created automatically on first run)