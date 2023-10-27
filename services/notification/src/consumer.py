import logging
from aiokafka import AIOKafkaConsumer
import asyncio
from config import KAFKA_BOOTSTRAP_SERVERS, CONSUMER_GROUP, USER_CREATED_TOPIC, USER_CREATING_TOPIC


async def get_consumer():
    consumer = AIOKafkaConsumer(
        USER_CREATED_TOPIC, USER_CREATING_TOPIC,
        bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
        group_id=CONSUMER_GROUP)
    try:
        await consumer.start()
        yield consumer
    except:
        logging.error('Error while consuming message')
    finally:
        await consumer.stop()
