# 🚀 SparkDay Backend – AI Agent Engine for Daily Positivity

This is the **backend service** of SparkDay – a fully autonomous AI agent designed to deliver daily uplifting messages and images to email subscribers and display them on the website.

## ✨ Key Functions

1. **Subscriber Management**
   - Collects and stores subscriber emails via API.

2. **AI Agent Content Generation**
   - Retrieves daily historical events or trending news.
   - Uses **LangChain + OpenAI** to generate a positive message.
   - Finds or generates a matching inspirational image (Unsplash, MidJourney, or GenAI).

3. **Daily Content Delivery**
   - Compiles the message and image for email and website display.
   - Sends daily emails to all subscribers via SMTP.

4. **Public API**
   - Exposes API endpoints for:
     - Subscribing users.
     - Fetching the latest daily message.

5. **Scheduling & Automation**
   - Runs the content generation and delivery pipeline on a daily schedule.

---

## 🛠️ Features

- ✅ FastAPI-powered REST API
- ✅ LangChain + OpenAI-powered AI Agent
- ✅ SMTP Email Delivery (Gmail, SendGrid, etc.)
- ✅ PostgreSQL / SQLite Database Support
- ✅ Cron or APScheduler Automation Support
- ✅ Modular, Extendable, and Easy to Maintain
- ✅ Environment Variable Configuration

---

## 🗂️ File Structure Overview

backend/
├── app/
│   ├── init.py
│   ├── main.py                # FastAPI app and routes setup
│
│   ├── core/
│   │   ├── config.py          # Environment variables and config loader
│   │   └── scheduler.py       # Daily automation scheduler
│
│   ├── services/
│   │   ├── news_fetcher.py    # Fetch today’s events or news
│   │   ├── ai_agent.py        # LangChain + OpenAI positive message generator
│   │   ├── image_finder.py    # Find or generate relevant image
│   │   ├── email_service.py   # SMTP email sending
│   │   └── message_compiler.py # Assemble daily content
│
│   ├── models/
│   │   ├── database.py        # Database connection setup
│   │   ├── subscriber.py      # Subscriber table model
│   │   └── daily_message.py   # Daily message table model
│
│   ├── api/
│   │   ├── init.py
│   │   ├── routes.py          # API route handlers
│   │   └── schemas.py         # Pydantic validation models
│
│   ├── utils/
│   │   ├── logger.py          # Logging utilities
│   │   └── email_validator.py # Email format validation
│
│   └── tasks/
│       └── daily_runner.py    # Cron/CLI entry point for daily tasks
│
├── requirements.txt
├── .env.example               # Example environment variable definitions
└── README.md

---

## ⚙️ Environment Variables (`.env`)

OPENAI_API_KEY=your_openai_api_key
SMTP_HOST=smtp.gmail.com
SMTP_PORT=465
SMTP_USER=your_email@gmail.com
SMTP_PASS=your_smtp_app_password
DATABASE_URL=sqlite:///./data.db  # or your PostgreSQL connection string

---

## 🚀 How to Run

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run API Locally**
```uvicorn app.main:app --reload```