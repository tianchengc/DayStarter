# SparkDay ✨  
**The start you deserve, every day.**

---

## 🌟 What Is SparkDay?

SparkDay is a fully autonomous **AI Agent** that brightens your day with a short, uplifting message and a matching image, delivered via email and displayed on a beautifully animated website.

Built with **LangChain** and **OpenAI**, SparkDay uses AI to analyze historical events or world news and generate motivational content, helping people start their day with courage and positivity.

---

## 🧠 How It Works

- **No login or account required** – users just subscribe with their email.
- **Daily Content Generation Pipeline**:
  1. **Fetch News or Events**: Scrape or retrieve historical or recent news for today's date.
  2. **LangChain AI Agent Analysis**:  
     - Use OpenAI LLM via LangChain to generate an uplifting, human-like message.
  3. **Image Selection**:  
     - Search Unsplash, MidJourney community images, or generate using GenAI.
  4. **Content Delivery**:
     - Update the website with the new message and image.
     - Send the content to all subscribers by email.

---

## 🛠️ Architecture Overview

1. **Frontend (Vite + React + TypeScript)**
   - Single-page animated site with daily message and background image.
   - Simple email subscription form.

2. **Backend (Python + FastAPI + LangChain)**
   - LangChain-powered AI Agent to generate daily positive messages.
   - Scheduler to run daily content generation.
   - Email service using SMTP (Gmail, SendGrid, etc.).
   - Database for managing subscribers and daily content.

3. **Deployment**
   - Self-hosted on **DigitalOcean Droplet VM** (UI + API + Scheduler).
   - Nginx reverse proxy to serve UI and API securely.

---

## 🚀 Live Demo
_Stay tuned… deployment coming soon._  
Or run locally by following the steps below.

---

## 🧑‍💻 Local Development

### Prerequisites

- Node.js 18+
- Python 3.10+
- PostgreSQL (or SQLite for dev)
- OpenAI API Key
- Unsplash API Key (optional)
- SMTP Credentials (Gmail, SendGrid, etc.)

### Setup Instructions

```bash
git clone https://github.com/yourusername/sparkday.git
cd sparkday