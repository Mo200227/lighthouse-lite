# Lighthouse Lite

An API that evaluates classroom observation notes with Claude and returns scores, strengths, areas for growth, and recommendations. Built with FastAPI and the Anthropic API.

**Live demo:** https://lighthouse-lite.onrender.com/docs
(Hosted on Render's free tier, so the first request after idle time can take about 30–60 seconds.)

## What it does

You send observation notes, a teacher name, and a framework. The service builds a prompt around that framework's rubric, calls Claude (`claude-haiku-4-5`), and returns the evaluation along with the token count for the call.

## Frameworks

| Value | Rubric | Scale |
|---|---|---|
| `danielson` | Danielson Framework for Teaching (4 domains) | 1–4 |
| `niet` | NIET Teaching Standards (10 areas) | 1–5 |
| `general` | Instruction, engagement, management, objectives (4 areas) | 1–10 |

## API

| Method | Path | Description |
|---|---|---|
| GET | `/` | Service info |
| GET | `/frameworks` | List available frameworks |
| POST | `/evaluate` | Evaluate an observation |

### Example

```bash
curl -X POST https://lighthouse-lite.onrender.com/evaluate \
  -H "Content-Type: application/json" \
  -d '{
    "teacher_name": "Ms. Rivera",
    "framework": "danielson",
    "observation_notes": "Students entered quietly and started the warm-up. Teacher posed open-ended questions, but a few students dominated discussion. Exit ticket was collected at the end."
  }'
```

Response shape:

```json
{
  "teacher": "Ms. Rivera",
  "framework": "danielson",
  "evaluation": "<Claude's scores, strengths, areas for growth, recommendations, and summary as text>",
  "tokens_used": 0
}
```

Invalid input (empty notes or an unknown framework) returns `400`.

## Run locally

1. Clone the repo and create a virtual environment
2. `pip install -r requirements.txt`
3. Copy `.env.example` to `.env` and add your `ANTHROPIC_API_KEY`
4. `uvicorn app.main:app --reload`
5. Open http://localhost:8000/docs

## Tech stack

Python, FastAPI, Pydantic, Anthropic API (`claude-haiku-4-5`), deployed on Render.

## Limitations

- The evaluation is free-form text, not parsed into structured fields.
- Scores are model-generated and not validated against human raters. This is a prototype, not a replacement for a trained observer.
- No authentication or rate limiting, and CORS is open.
