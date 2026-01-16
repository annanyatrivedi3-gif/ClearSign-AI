from fastapi import APIRouter
from pydantic import BaseModel
from backend.services.risk_engine import analyze_risks

router = APIRouter(prefix="/analyze", tags=["Analysis"])

class DocumentInput(BaseModel):
    text: str

@router.post("/")
def analyze_doc(payload: DocumentInput):
    risks = analyze_risks(payload.text)

    return {
        "summary": "ClearSign AI risk analysis",
        "risk_count": len(risks),
        "risks": risks
    }
