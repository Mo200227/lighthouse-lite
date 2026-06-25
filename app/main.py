from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from app.evaluator import evaluate_observation

app = FastAPI(
    title="Lighthouse Lite",
    description="AI-powered classroom observation evaluator using Claude",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class ObservationRequest(BaseModel):
    teacher_name: str = "Teacher"
    observation_notes: str
    framework: str = "general"

class EvaluationResponse(BaseModel):
    teacher: str
    framework: str
    evaluation: str
    tokens_used: int

@app.get("/")
def root():
    return {
        "message": "Lighthouse Lite - AI Classroom Observation Evaluator",
        "frameworks": ["general", "danielson", "niet"],
        "docs": "/docs"
    }

@app.get("/frameworks")
def get_frameworks():
    return {
        "frameworks": {
            "general": "General classroom evaluation across 4 areas",
            "danielson": "Danielson Framework for Teaching (4 domains)",
            "niet": "NIET Teaching Standards (10 areas)"
        }
    }

@app.post("/evaluate", response_model=EvaluationResponse)
def evaluate(request: ObservationRequest):
    if not request.observation_notes.strip():
        raise HTTPException(status_code=400, detail="Observation notes cannot be empty")
    
    if request.framework not in ["general", "danielson", "niet"]:
        raise HTTPException(status_code=400, detail="Framework must be: general, danielson, or niet")
    
    result = evaluate_observation(
        observation_notes=request.observation_notes,
        framework=request.framework,
        teacher_name=request.teacher_name
    )
    
    return result