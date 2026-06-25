# Lighthouse Lite 🏫

AI-powered classroom observation evaluator built with Claude API and FastAPI.

## What it does
Paste classroom observation notes and select an evaluation framework — Claude analyzes the observation and returns structured scores, strengths, areas for growth, and actionable recommendations.

## Frameworks Supported
- **Danielson Framework** (4 domains)
- **NIET Teaching Standards** (10 areas)
- **General** (4 areas)

## Tech Stack
- Python / FastAPI
- Anthropic Claude API (claude-haiku-4-5)
- Deployed on Render

## Setup
1. Clone the repo
2. Create a `.env` file using `.env.example` as a template
3. Add your Anthropic API key
4. Install dependencies: `pip install -r requirements.txt`
5. Run: `uvicorn app.main:app --reload`
6. Visit `http://localhost:8000/docs` to try it

## API Endpoints
- `GET /` — Project info
- `GET /frameworks` — List available frameworks
- `POST /evaluate` — Evaluate a classroom observation
