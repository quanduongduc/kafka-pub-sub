from pydantic import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "sledgehammer"
    SMTP_SERVER: str
    SMTP_PORT: int
    SMTP_USERNAME: str
    SMTP_PASSWORD: str
    MAIL_DEFAULT_SENDER: str
    KAFKA_BOOTSTRAP_SERVERS: str = "kafka:29092"
    NOTI_CONSUMER_GROUP: str = "group.notification"
    MAILER_CONSUMER_GROUP: str = "group.mailer"
    USER_CREATING_TOPIC: str = 'user.creating.key'
    USER_CREATED_TOPIC: str = 'user.created.key'


settings = Settings()
