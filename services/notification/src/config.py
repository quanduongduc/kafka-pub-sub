import os
from dotenv import load_dotenv

load_dotenv()

# Load individual environment variables
APP_NAME = "dukwan"
SMTP_SERVER = os.environ.get("SMTP_SERVER")
SMTP_PORT = os.environ.get("SMTP_PORT")
SMTP_USERNAME = os.environ.get("SMTP_USERNAME")
SMTP_PASSWORD = os.environ.get("SMTP_PASSWORD")
MAIL_DEFAULT_SENDER = f'"{APP_NAME}" <example@example.com>'

KAFKA_BOOTSTRAP_SERVERS = os.environ.get(
    'KAFKA_BOOTSTRAP_SERVERS', "kafka:29092")

# kafka topic
CONSUMER_GROUP = os.environ.get('CONSUMER_GROUP', "group.notification")
USER_CREATING_TOPIC = 'user.creating.key'
USER_CREATED_TOPIC = 'user.created.key'

# Check if all required environment variables are set
if SMTP_SERVER is None or SMTP_PORT is None or SMTP_USERNAME is None or SMTP_PASSWORD is None:
    print("One or more required environment variables are missing.")
