# 🤖 Mridul AI News

<p align="center">
  <strong>Personalized AI News Aggregation, Summarization & Delivery Platform</strong>
</p>

<p align="center">
  Collect AI news • Summarize with a local LLM • Personalize • Search • Email
</p>

---

## 📌 Overview

**Mridul AI News** is an AI-powered news aggregation platform designed to automatically collect recent artificial intelligence news, process and summarize the content using a local Large Language Model (LLM), personalize article ranking according to a user profile, and deliver a daily news digest through email.

The project also provides a **Streamlit web dashboard** where users can browse and search the collected AI news.

The goal is to reduce the time required to manually monitor multiple AI news sources while still giving the user relevant and concise information.

---

## ✨ Key Features

| Feature | Description |
|---|---|
| 📰 **AI News Collection** | Collects recent AI-related articles and video content from configured sources |
| 🤖 **AI Summarization** | Generates concise article summaries using a local LLM |
| 🧠 **Personalized Ranking** | Ranks articles according to the user's interests and preferences |
| 📧 **Email Digest** | Generates and sends a personalized AI news digest |
| 🔎 **News Search** | Search articles by title or summary |
| 🌐 **Original Sources** | Open the original article directly from the dashboard |
| 🗄️ **PostgreSQL Storage** | Stores collected articles and generated digests |
| 💻 **Streamlit Dashboard** | Provides an interactive web interface |
| ⏰ **Daily Automation** | Can be executed automatically using Windows Task Scheduler |
| 🔐 **Environment Security** | Keeps email credentials outside the source code using `.env` |

---

# 🧠 How the System Works

```text
                    AI NEWS SOURCES
                          │
                          ▼
                 ┌─────────────────┐
                 │     Scrapers    │
                 │ Collect Articles│
                 └────────┬────────┘
                          │
                          ▼
                 ┌─────────────────┐
                 │   PostgreSQL    │
                 │     Database    │
                 └────────┬────────┘
                          │
                          ▼
                 ┌─────────────────┐
                 │   Local LLM     │
                 │ Ollama + Llama  │
                 └────────┬────────┘
                          │
              ┌───────────┴───────────┐
              ▼                       ▼
       ┌──────────────┐        ┌──────────────┐
       │ Digest Agent │        │Curator Agent │
       │ AI Summary   │        │ AI Ranking   │
       └───────┬──────┘        └──────┬───────┘
               │                      │
               └──────────┬───────────┘
                          ▼
                 ┌─────────────────┐
                 │ Personalized    │
                 │ News Digest     │
                 └────────┬────────┘
                          │
                 ┌────────┴────────┐
                 ▼                 ▼
        ┌────────────────┐  ┌────────────────┐
        │ Streamlit      │  │ Gmail / SMTP   │
        │ Dashboard      │  │ Email Delivery │
        └────────────────┘  └────────────────┘
```

---

# 🔄 Application Workflow

### 1. Collect

The configured scrapers collect recent AI-related content.

### 2. Store

Collected articles are stored in a PostgreSQL database.

### 3. Summarize

The application uses a local LLM through Ollama to generate concise summaries.

### 4. Personalize

The Curator Agent uses the user's profile to evaluate and rank the available articles.

### 5. Generate Digest

The Email Agent prepares a personalized digest containing the selected articles.

### 6. Deliver

The digest can be sent through Gmail SMTP.

### 7. Explore

The Streamlit dashboard allows the user to search and read the latest collected news.

---

# 🤖 AI Components

The project currently uses a **local LLM**, so the core AI processing does not require a paid OpenAI API.

### Local AI Stack

```text
Ollama
   ↓
Llama 3.2 3B
   ↓
Python Application
   ↓
AI Summarization + Ranking + Email Generation
```

### Digest Agent

The Digest Agent generates:

- A concise article title
- A short summary
- Important information from the source content
- A readable explanation for the user

### Curator Agent

The Curator Agent evaluates articles using information from the user profile, including:

- Areas of interest
- Technical background
- Expertise level
- Content preferences
- Technical value
- Novelty
- Practical usefulness

Each article receives a relevance score and ranking.

### Email Agent

The Email Agent generates a personalized introduction and prepares the selected articles for the email digest.

---

# 👤 Personalization

The application uses a configurable user profile.

Example profile information includes:

```text
Name
Background
Expertise Level
Interests
Content Preferences
```

This allows the same news collection system to produce a digest tailored to a particular user.

---

# 💻 Web Dashboard

The project includes an interactive **Streamlit dashboard**.

The dashboard currently provides:

- Latest AI news
- AI-generated summaries
- Source information
- Search by title or summary
- Links to original articles

### Start the dashboard

```bash
uv run streamlit run dashboard.py
```

Streamlit will display a local URL in the terminal, for example:

```text
http://localhost:8503
```

---

# 📧 Personalized Email Digest

The project can generate and send an automated AI news digest through Gmail SMTP.

A typical digest contains:

```text
Personalized Greeting
        ↓
AI-generated Introduction
        ↓
Ranked AI Articles
        ↓
Article Summaries
        ↓
Original Article Links
```

The email functionality is integrated into the main daily pipeline.

---

# ⏰ Automation

The application can be scheduled to run automatically using **Windows Task Scheduler**.

The scheduled command is:

```bash
uv run python main.py
```

This allows the news collection and email process to run without manually starting the pipeline every day.

---

# 🛠️ Technology Stack

### Programming

- Python

### Artificial Intelligence

- Ollama
- Llama 3.2 3B
- Pydantic

### Database

- PostgreSQL

### Web Interface

- Streamlit

### Email

- Gmail SMTP
- Python `smtplib`

### Configuration

- Python-dotenv

### Package Management

- UV

### Data Collection

- RSS / configured news scrapers

---

# 📁 Project Structure

```text
mridul_project/
│
├── app/
│   ├── agent/
│   │   ├── curator_agent.py
│   │   ├── digest_agent.py
│   │   └── email_agent.py
│   │
│   ├── database/
│   │   └── ...
│   │
│   ├── profiles/
│   │   └── user_profile.py
│   │
│   ├── scrapers/
│   │   └── ...
│   │
│   ├── services/
│   │   ├── email.py
│   │   ├── process_email.py
│   │   └── ...
│   │
│   ├── config.py
│   └── daily_runner.py
│
├── dashboard.py
├── main.py
├── pyproject.toml
├── uv.lock
├── .gitignore
└── README.md
```

---

# 🚀 Installation

## Prerequisites

Make sure the following are installed:

- Python 3.12+
- PostgreSQL
- Ollama
- UV
- Git

---

## 1. Clone the repository

```bash
git clone https://github.com/mridul2213/mridul_project.git
cd mridul_project
```

---

## 2. Install Python dependencies

The project uses UV for dependency management.

```bash
uv sync
```

---

## 3. Install the local LLM

Make sure Ollama is installed and running.

Then download the model:

```bash
ollama pull llama3.2:3b
```

You can verify the model with:

```bash
ollama list
```

---

## 4. Configure PostgreSQL

Create the PostgreSQL database required by the application and make sure the database configuration used by the project points to your local PostgreSQL installation.

---

## 5. Configure environment variables

Create a `.env` file in the project root.

Example:

```env
MY_EMAIL=your_email@gmail.com
APP_PASSWORD=your_gmail_app_password
```

The `.env` file should remain local.

**Never upload `.env` to GitHub.**

---

# ▶️ Running the Application

## Run the complete AI news pipeline

From the project directory:

```bash
uv run python main.py
```

The pipeline performs:

```text
News Collection
      ↓
Article Processing
      ↓
AI Summarization
      ↓
AI Ranking
      ↓
Personalized Digest
      ↓
Email Delivery
```

---

## Run the dashboard

Open another terminal in the project directory:

```bash
uv run streamlit run dashboard.py
```

Then open the local URL provided by Streamlit.

---

# 🔐 Security

Sensitive credentials are intentionally kept outside the source code.

The project uses:

```text
.env
```

for private configuration such as the Gmail App Password.

The repository's `.gitignore` excludes `.env`.

### Never commit:

```text
.env
```

or any:

- Passwords
- API keys
- Access tokens
- Private credentials
- Service-account files

---

# 📸 Screenshots

Add screenshots of your working application here.

Recommended screenshots:

### Dashboard

```text
docs/images/dashboard.png
```

### Search

```text
docs/images/search.png
```

### Email Digest

```text
docs/images/email-digest.png
```

> Screenshots can be added later without changing the application itself.

---

# 🎯 Project Objectives

The project focuses on building an end-to-end intelligent news platform that combines:

- Automated data collection
- Natural Language Processing
- Local Large Language Models
- Personalized content ranking
- Database management
- Web application development
- Automated email delivery

The system is designed to reduce information overload by presenting relevant AI developments in a concise and personalized format.

---

# 🔮 Future Improvements

Planned or possible improvements include:

- 📊 News analytics dashboard
- 🏷️ Automatic topic/category classification
- ⭐ Article importance scoring
- 🔖 Save/bookmark articles
- 👤 Multiple user profiles
- 🎯 Improved personalization
- 🔍 Advanced filtering
- 📈 Trending AI topics
- 🧠 Improved ranking consistency
- 📱 Responsive dashboard
- ☁️ Cloud deployment
- 🐳 Docker-based deployment
- 🔄 More news sources
- 📰 Improved article deduplication

---

# 🧪 Project Demonstration

A simple demonstration can be performed in two parts.

### Part 1 — AI News Pipeline

Run:

```bash
uv run python main.py
```

The application collects news, processes it with the local LLM, ranks the articles, and sends the digest.

### Part 2 — Web Dashboard

Run:

```bash
uv run streamlit run dashboard.py
```

Then demonstrate:

1. Latest AI news
2. Search
3. AI-generated summaries
4. Original article links

---

# 👨‍💻 Author

## Mridul

**B.Tech Computer Science & Engineering**  
**AI & Data Science**

GitHub:  
https://github.com/mridul2213

---

# 📄 Project Attribution

This repository contains modifications and extensions based on an existing AI news aggregation project.

The original project's license and attribution requirements should be preserved and followed. This repository documents the additional development, configuration, personalization, dashboard, local-LLM processing, and email automation work performed for this version.

---

## ⭐ Project Status

**Current status:** Working prototype / active development

Core functionality currently includes:

- ✅ AI news collection
- ✅ PostgreSQL storage
- ✅ Local LLM summarization
- ✅ Personalized article ranking
- ✅ Email digest generation
- ✅ Gmail email delivery
- ✅ Streamlit dashboard
- ✅ News search
- ✅ Daily automation support

---

<p align="center">
  <strong>Built with Python • Ollama • Llama 3.2 • PostgreSQL • Streamlit</strong>
</p>

