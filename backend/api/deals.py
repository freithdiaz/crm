from fastapi import APIRouter, Depends, HTTPException, Body
from sqlmodel import Session, select
from typing import List, Annotated
from backend.database import get_session
from backend.models import Deal

# Type alias for dependency injection
SessionDep = Annotated[Session, Depends(get_session)]

router = APIRouter(prefix="/api/deals", tags=["Deals"])

@router.get("/", response_model=List[Deal])
def get_deals(session: SessionDep):
    statement = select(Deal)
    deals = session.exec(statement).all()
    return deals

@router.put("/{deal_id}/stage")
def update_deal_stage(session: SessionDep, deal_id: int, stage: str = Body(..., embed=True)):
    deal = session.get(Deal, deal_id)
    if not deal:
        raise HTTPException(status_code=404, detail="Trato no encontrado")
    deal.stage = stage
    session.add(deal)
    session.commit()
    session.refresh(deal)
    return {"message": "Etapa actualizada", "deal_id": deal_id, "new_stage": stage}
