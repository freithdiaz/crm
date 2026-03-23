import os
import sys

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

import seed_db
from sqlmodel import Session, select
from backend.models import Lead

print("Vaciando tabla Lead...")
with Session(seed_db.engine) as session:
    results = session.exec(select(Lead)).all()
    for row in results:
        session.delete(row)
    session.commit()
    print("Tabla Lead vaciada.")

seed_db.seed_data()
print("Base de datos reseteada con éxito.")

