from pydantic_settings import BaseSettings  # importe la classe de base


class Settings(BaseSettings):
    # Informations de l'application
    APP_NAME: str = "IoT Equipment API"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = True

    # Base de données
    DATABASE_URL: str  # obligatoire - pas de valeur par défaut

    # Sécurité JWT
    SECRET_KEY: str    # obligatoire - pas de valeur par défaut
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config:
        env_file = ".env"  # dit à Pydantic où lire les variables


# Instance unique réutilisable dans tout le projet
settings = Settings()