# DE Learning Agent 🤖

A personal AI-powered Data Engineering learning assistant built with Python and Google Gemini.

## What it does
- Explains Data Engineering concepts in simple terms
- Relates concepts to Java/Spring Boot background
- Acts as a personal DE mentor available 24/7
- Supports both terminal and browser UI

## Tech Stack
- Python 3.9
- Google Gemini API (gemini-2.0-flash-lite)
- Streamlit (UI)
- python-dotenv (environment management)

## Project Structure
de-learning-agent/

├── agent.py      # Gemini AI brain

├── app.py        # Streamlit UI

├── main.py       # Terminal interface

├── tools.py      # Agent tools

├── .env          # API keys (not pushed)

└── .gitignore    # Git ignore rules


## How to Run

### Terminal version
```bash
source venv/bin/activate
python3 main.py
```

### Browser UI version
```bash
source venv/bin/activate
streamlit run app.py
```

## Setup
```bash
# Clone the repo
git clone https://github.com/15ranjan/de-learning-agent.git

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install google-genai streamlit python-dotenv

# Add your API key
echo "GEMINI_API_KEY=your-key-here" > .env

# Run
python3 main.py
```

## Author
Sudhanshu Ranjan