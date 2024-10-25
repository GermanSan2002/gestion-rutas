import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings  # Cambia la importación a pydantic-settings

# Cargar variables de entorno desde el archivo .env
load_dotenv()

class Settings(BaseSettings):
    GOOGLE_MAPS_API_KEY: str = os.getenv("GOOGLE_MAPS_API_KEY")
    DATABASE_URL: str = os.getenv("DATABASE_URL")
    REDIS_URL: str = os.getenv("REDIS_URL", "redis://localhost:6379/0")  # URL de Redis por defecto

    class Config:
        env_file = ".env"
        extra = "ignore"

# Instancia única de Settings para uso en todo el proyecto
settings = Settings()
