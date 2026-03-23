import sys
import os

# Add current directory to path
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from backend.database import create_db_and_tables

if __name__ == "__main__":
    print("Creando base de datos y tablas...")
    create_db_and_tables()
    print("¡Base de datos inicializada con éxito!")
