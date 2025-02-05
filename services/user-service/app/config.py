from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://mj:mjpass@host.docker.internal:5432/mva_user_service"
    SECRET_KEY: str = "63d6f576c27dda398024310eb8dd10f9350530c97dbde1568b4976dbc1f6da64"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES : int = 30
    KAFKA_BOOTSTRAP_SERVERS: str = "kafka:9092"

    class Config:
        env_file = ".env"
settings = Settings()