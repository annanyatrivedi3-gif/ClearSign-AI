from fastapi import APIRouter
from pydantic import BaseModel

from backend.services.risk_engine import analyze_risks, calculate_score
from backend.services.ai_explainer import generate_explanation

router = APIRouter(prefix="/analyze", tags=["Analysis"])


class DocumentInput(BaseModel):
    text: str


@router.post("/")
def analyze_doc(payload: DocumentInput):
    # 1. Detect risks
    risks = analyze_risks(payload.text)

    # 2. Calculate overall risk score
    score = calculate_score(risks)

    # 3. Generate human-friendly explanation
    explanation = generate_explanation(risks)

    # 4. Return structured response
    return {
        "summary": "ClearSign AI risk analysis",
        "risk_score": score,
        "risk_count": len(risks),
        "ai_explanation": explanation,
        "risks": risks
    }
