import os
import sys

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

import seed_db
from sqlmodel import Session, select
from backend.models import Lead, Deal

print("Vaciando tablas...")
with Session(seed_db.engine) as session:
    # Delet Deals first
    deals = session.exec(select(Deal)).all()
    for d in deals:
        session.delete(d)
        
    leads = session.exec(select(Lead)).all()
    for row in leads:
        session.delete(row)
    session.commit()
    print("Tablas vaciadas.")


seed_db.seed_data()
print("Base de datos reseteada con éxito.")

