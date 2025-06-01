from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://curro:1@localhost:5432/empresa"  # Cambia por tu URL de conexión

# Crea la base de datos y las clases ORM
engine = create_engine(DATABASE_URL, echo=True)

# Crea una base de datos declarativa
Base = declarative_base()

# Crea una sesión para interactuar con la base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
