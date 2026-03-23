from typing import Optional
from sqlmodel import SQLModel, Field
from datetime import datetime

class Lead(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    company: str
    email: str = Field(unique=True)
    phone: Optional[str] = None
    status: str = "Nuevo"  # Nuevo, Contactado, Calificado, Perdido

    value: float = 0.0
    created_at: datetime = Field(default_factory=datetime.utcnow)

class Deal(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    lead_id: int = Field(foreign_key="lead.id")
    stage: str = "Pipeline"  # Pipeline, Contacted, Proposal, Negotiation, Closed Won, Closed Lost
    amount: float = 0.0
    probability: int = 0  # 0-100
    created_at: datetime = Field(default_factory=datetime.utcnow)
