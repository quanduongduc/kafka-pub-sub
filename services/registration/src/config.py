from typing import Any, Optional

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    KAFKA_BOOTSTRAP_SERVERS: Optional[str] = "kafka:29092"
    USER_CREATING_TOPIC: Optional[str] = "user.creating.key"
    USER_CREATED_TOPIC: Optional[str] = "user.created.key"

    class Config:
        env_file = ".env"


settings = Settings()
