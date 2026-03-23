import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from sqlmodel import Session
from backend.database import engine, create_db_and_tables
from backend.models import Lead

def seed_data():
    with Session(engine) as session:
        leads = session.query(Lead).all()
        if leads:
            print("Datos ya sembrados.")
            return

        print("Sembrando datos de prueba...")
        sample_leads = [
            Lead(name="Carlos Ramos", company="Tech Solutions", email="carlos@techsol.com", phone="555-0199", status="Nuevo", value=15000.0),
            Lead(name="Laura Castro", company="Innovate Inc", email="laura@innovate.com", phone="555-0188", status="Calificado", value=45000.0),
            Lead(name="Roberto Díaz", company="DataFlow", email="roberto@dataflow.com", phone="555-0177", status="Contactado", value=8000.0),

            Lead(name="Sofia Morales", company="CloudNine", email="sofia@cloudnine.com", phone="555-0166", status="Perdido", value=0.0),
        ]

        
        for lead in sample_leads:
            session.add(lead)
        session.commit()
        print("¡Datos sembrados con éxito!")

if __name__ == "__main__":
    create_db_and_tables()
    seed_data()
