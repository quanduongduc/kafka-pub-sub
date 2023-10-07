from typing import Any, Optional
from pydantic import validator

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    KAFKA_BOOTSTRAP_SERVERS: Optional[str] = "kafka:29092"
    USER_CREATING_TOPIC: Optional[str] = "user.creating.key"
    USER_CREATED_TOPIC: Optional[str] = "user.created.key"

    CELERY_APP_NAME: Optional[str] = 'registration'
    CELERY_BROKER_PORT: Optional[str] = "6379"
    CELERY_BROKER_HOST: Optional[str] = "redis"

    CELERY_BROKER_URL: Optional[str] = None
    CELERY_RESULT_BACKEND: Optional[str] = None

    @validator("CELERY_BROKER_URL", "CELERY_RESULT_BACKEND")
    def validate_celery_urls(cls, value, values):
        if value is not None:
            return value
        broker_url = f"redis://{values['CELERY_BROKER_HOST']}:{values['CELERY_BROKER_PORT']}"
        return broker_url

    class Config:
        env_file = ".env"


settings = Settings()
