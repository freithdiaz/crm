from fastapi import APIRouter, Depends, HTTPException, Body
from sqlmodel import Session, select
from typing import List
from backend.database import get_session
from backend.models import Deal

router = APIRouter(prefix="/api/deals", tags=["Deals"])

@router.get("/", response_model=List[Deal])
def get_deals(session: Session = Depends(get_session)):
    statement = select(Deal)
    deals = session.exec(statement).all()
    return deals

@router.put("/{deal_id}/stage")
def update_deal_stage(deal_id: int, stage: str = Body(..., embed=True), session: Session = Depends(get_session)):
    deal = session.get(Deal, deal_id)
    if not deal:
        raise HTTPException(status_code=404, detail="Trato no encontrado")
    deal.stage = stage
    session.add(deal)
    session.commit()
    session.refresh(deal)
    return {"message": "Etapa actualizada", "deal_id": deal_id, "new_stage": stage}
