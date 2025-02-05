from pydantic import BaseSettings
from dotenv import load_dotenv
import os
class Settings(BaseSettings):
    DATABASE_URL: str = f"postgresql://{os.getenv("DATABASE_USER")}:{os.getenv("DATABASE_PASSWORD")}@host.docker.internal:5432/mva_user_service"
    SECRET_KEY: str = os.getenv("SECRET_KEY")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES : int = 30
    KAFKA_BOOTSTRAP_SERVERS: str = "kafka:9092"

    class Config:
        env_file = ".env"
settings = Settings()