import os
import anthropic
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

FRAMEWORKS = {
    "danielson": """The Danielson Framework for Teaching focuses on four domains:
1. Planning and Preparation
2. Classroom Environment  
3. Instruction
4. Professional Responsibilities
Score each domain 1-4: 1=Unsatisfactory, 2=Basic, 3=Proficient, 4=Distinguished""",

    "niet": """The NIET Teaching Standards evaluate:
1. Classroom Management
2. Standards & Objectives
3. Motivating Students
4. Presenting Instructional Content
5. Lesson Structure & Pacing
6. Activities & Materials
7. Questioning & Discussion
8. Student Understanding
9. Problem Solving
10. Assessment
Score each area 1-5: 1=Ineffective to 5=Highly Effective""",

    "general": """Evaluate this classroom observation across:
1. Instruction Quality
2. Student Engagement
3. Classroom Management
4. Learning Objectives
Score each area 1-10."""
}

def evaluate_observation(observation_notes: str, framework: str = "general", teacher_name: str = "Teacher") -> dict:
    framework_prompt = FRAMEWORKS.get(framework, FRAMEWORKS["general"])
    
    prompt = f"""You are an expert instructional coach evaluating a classroom observation.

Teacher: {teacher_name}
Framework: {framework.upper()}

{framework_prompt}

Observation Notes:
{observation_notes}

Provide a structured evaluation with:
1. Scores for each domain/area
2. Key strengths observed
3. Areas for growth
4. Specific, actionable recommendations
5. Overall summary

Be specific, evidence-based, and constructive."""

    message = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=1024,
        messages=[{"role": "user", "content": prompt}]
    )
    
    return {
        "teacher": teacher_name,
        "framework": framework,
        "evaluation": message.content[0].text,
        "tokens_used": message.usage.input_tokens + message.usage.output_tokens
    }