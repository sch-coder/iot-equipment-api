from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database import Base


class Equipment(Base):
    __tablename__ = "equipements"

    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String, nullable=False)
    type = Column(String, nullable=False)
    localisation = Column(String, nullable=False)
    statut = Column(String, default="actif")
    date_creation = Column(DateTime(timezone=True), server_default=func.now())

    # Clé étrangère → relie l'équipement à son propriétaire
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    # Relation → permet d'accéder à user.equipements
    owner = relationship("User", back_populates="equipements")