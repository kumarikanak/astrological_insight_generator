# Astrological Insight Generator

A modular, LLM-powered service that generates **daily horoscope insights** based on the user's zodiac sign. Supports multiple languages (English and Hindi) and combines rule-based templates, retrieval from a zodiac corpus, and generative LLM output.

---

## Features

- Generates daily horoscope insights in English or Hindi.
- Uses zodiac personality traits for contextually accurate horoscopes.
- Optional vector-store-based retrieval for enriched content.
- Modular design for easy updates and extensions.
- Caching to optimize repeated requests.

---

## Installation

### 1. Clone the repository
```bash
git clone https://github.com/kumarikanak/astrological_insight_generator.git
cd astrological_insight_generator

### 2. Create and activate a virtual environment
```bash
conda create -n myenv python=3.10 -y
conda activate myenv

### 3. Install dependencies
```bash
pip install -r requirements.txt


## Running the Service
Start the FastAPI server:
```bash
uvicorn app.main:app --reload


## API Example
Request
```bash
curl -X POST "http://127.0.0.1:8000/insight" \
-H "Content-Type: application/json" \
-d '{
  "name": "Priya",
  "birth_date": "1993-09-09",
  "birth_place": "Delhi, India",
  "birth_time": "01:30",
  "language": "hi"
}'




