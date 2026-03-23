from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from typing import List
from backend.database import get_session
from backend.models import Lead

router = APIRouter(prefix="/api/leads", tags=["Leads"])

@router.get("/", response_model=List[Lead])
def get_leads(session: Session = Depends(get_session)):
    statement = select(Lead)
    leads = session.exec(statement).all()
    return leads

@router.post("/", response_model=Lead)
def create_lead(lead: Lead, session: Session = Depends(get_session)):
    session.add(lead)
    session.commit()
    session.refresh(lead)
    return lead

@router.get("/{lead_id}/ai-summary")
def get_lead_ai_summary(lead_id: int, session: Session = Depends(get_session)):
    lead = session.get(Lead, lead_id)
    if not lead:
        raise HTTPException(status_code=404, detail="Lead no encontrado")
    
    # Mock AI logic
    summary = f"📌 **Resumen IA para {lead.name}**\n\n- **Empresa**: {lead.company}\n- **Estado**: {lead.status}\n- **Acción recomendada**: Enviar correo introductorio con el plan Pro. El valor estimado es de ${lead.value:,.2f}."
    return {"summary": summary}
