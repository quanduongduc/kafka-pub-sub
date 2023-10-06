from confluent_kafka import Consumer
from config import *
from mailer.email_service import send_account_created_email

consumer_config = {
    'bootstrap.servers': KAFKA_BOOTSTRAP_SERVERS,
    'group.id': CONSUMER_GROUP,
    'auto.offset.reset': 'earliest'
}

consumer = Consumer(consumer_config)
topics = [USER_CREATED_TOPIC, USER_CREATING_TOPIC]
consumer.subscribe(topics)
