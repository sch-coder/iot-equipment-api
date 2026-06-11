from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

# Crée le moteur de connexion à PostgreSQL
engine = create_engine(settings.DATABASE_URL)

# Crée une fabrique de sessions
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Classe de base pour tous les modèles SQLAlchemy
Base = declarative_base()


# Fonction générateur - fournit une session par requête
def get_db():
    db = SessionLocal()  # ouvre une session
    try:
        yield db          # donne la session à la route
    finally:
        db.close()        # ferme TOUJOURS la session